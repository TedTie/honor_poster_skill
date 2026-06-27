from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate honor poster PNG dimensions.")
    parser.add_argument("poster", type=Path)
    parser.add_argument("--width", type=int, default=3508)
    parser.add_argument("--height", type=int, default=4961)
    args = parser.parse_args()

    if not args.poster.exists():
        raise SystemExit(f"missing file: {args.poster}")

    img = Image.open(args.poster)
    if img.size != (args.width, args.height):
        raise SystemExit(f"wrong size: {img.size}, expected {(args.width, args.height)}")

    if args.poster.stat().st_size < 100_000:
        raise SystemExit(f"file unexpectedly small: {args.poster.stat().st_size} bytes")

    print(f"ok size={img.size} bytes={args.poster.stat().st_size}")


if __name__ == "__main__":
    main()
