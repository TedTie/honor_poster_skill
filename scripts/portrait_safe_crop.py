from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw


def detect_subject_and_face(photo: Image.Image) -> tuple[tuple[int, int, int, int], tuple[int, int]]:
    small_w = 900
    small = photo.resize((small_w, int(photo.height * small_w / photo.width)), Image.Resampling.BILINEAR).convert("RGB")
    arr = np.asarray(small).astype(np.int16)
    h, w, _ = arr.shape

    border = np.concatenate(
        [
            arr[:35].reshape(-1, 3),
            arr[-35:].reshape(-1, 3),
            arr[:, :35].reshape(-1, 3),
            arr[:, -35:].reshape(-1, 3),
        ]
    )
    bg = np.median(border, axis=0)
    diff = np.abs(arr - bg).sum(axis=2)
    non_bg = diff > 58

    ys, xs = np.where(non_bg)
    if len(xs) < 200:
        subject = (0, 0, photo.width, photo.height)
    else:
        x0, x1 = np.percentile(xs, [1, 99])
        y0, y1 = np.percentile(ys, [1, 99])
        sx = photo.width / w
        sy = photo.height / h
        subject = (int(x0 * sx), int(y0 * sy), int(x1 * sx), int(y1 * sy))

    rgb = np.asarray(photo.convert("RGB")).astype(np.int16)
    r, g, b = rgb[:, :, 0], rgb[:, :, 1], rgb[:, :, 2]
    skin = (
        (r > 95)
        & (g > 55)
        & (b > 35)
        & (r > g + 8)
        & (r > b + 18)
        & ((np.maximum.reduce([r, g, b]) - np.minimum.reduce([r, g, b])) > 28)
    )

    sx0, sy0, sx1, sy1 = subject
    upper_limit = sy0 + int((sy1 - sy0) * 0.42)
    region = skin[max(0, sy0) : max(0, upper_limit), max(0, sx0) : min(photo.width, sx1)]
    fys, fxs = np.where(region)

    if len(fxs) > 200:
        face = (max(0, sx0) + int(np.median(fxs)), max(0, sy0) + int(np.percentile(fys, 45)))
    else:
        face = ((sx0 + sx1) // 2, sy0 + int((sy1 - sy0) * 0.18))
    return subject, face


def safe_square_crop(photo: Image.Image) -> tuple[Image.Image, tuple[int, int, int, int], tuple[int, int]]:
    subject, face = detect_subject_and_face(photo)
    sx0, sy0, sx1, sy1 = subject
    face_x, face_y = face
    subject_w = sx1 - sx0
    subject_h = sy1 - sy0

    side = int(max(subject_w * 1.20, subject_h * 0.56, photo.width * 0.72))
    side = min(side, int(photo.width * 0.82), int(photo.height * 0.68))

    left = int(face_x - side * 0.50)
    top = int(face_y - side * 0.28)
    left = max(0, min(left, photo.width - side))
    top = max(0, min(top, photo.height - side))

    box = (left, top, left + side, top + side)
    return photo.crop(box), box, face


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a face-safe square portrait crop for honor posters.")
    parser.add_argument("input", type=Path)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--circle-preview", action="store_true")
    args = parser.parse_args()

    photo = Image.open(args.input).convert("RGB")
    crop, box, face = safe_square_crop(photo)
    if args.circle_preview:
        side = min(crop.size)
        mask = Image.new("L", (side, side), 0)
        d = ImageDraw.Draw(mask)
        d.ellipse((0, 0, side - 1, side - 1), fill=255)
        out = Image.new("RGBA", (side, side), (255, 255, 255, 0))
        out.paste(crop.resize((side, side), Image.Resampling.LANCZOS).convert("RGBA"), (0, 0), mask)
    else:
        out = crop

    args.out.parent.mkdir(parents=True, exist_ok=True)
    out.save(args.out)
    print(f"crop_box={box}")
    print(f"face={face}")
    print(f"output={args.out}")


if __name__ == "__main__":
    main()
