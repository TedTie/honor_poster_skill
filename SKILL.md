---
name: honor-poster-skill
description: Use when creating 51Talk-style personal achievement, honor, sales target, onboarding, or celebration posters that need a portrait, name, team, Chinese or English layout, Toki IP, ImageGen art typography, same-month layout continuity, and 3508x4961 PNG output.
---

# Honor Poster Skill

## Overview

Create polished personal honor posters for 51Talk-style sales achievements. Use ImageGen for dynamic red-gold / seasonal visual energy and art typography, then use deterministic compositing for accurate names, teams, titles, congratulatory copy, portrait placement, and 3508px x 4961px delivery.

## Default Poster Contract

- Output size: always `3508 x 4961` PNG unless the user explicitly changes it.
- Required first poster inputs for a new campaign: portrait, name, team, language, personal title `最佳____`, month/theme, same-month layout yes/no.
- Required same-campaign inputs: portrait, name, team, language, personal title, same-month layout yes/no.
- If the user says `这是新的`, start a new campaign/theme. Otherwise carry forward the previous month/theme, style, Toki treatment, and layout rules.
- Default style intensity: `强冲刺感`.
- Use Chinese or English according to `语言`. English needs wider, lower-density text blocks; never shrink text until it becomes decorative dust.

Read when needed:

- `references/input-contract.md` for input parsing and carry-over rules.
- `references/design-system.md` for layout, typography, ImageGen, and language rules.
- `references/toki-ip.md` before generating or editing any Toki element.
- `references/quality-checklist.md` before delivery.

## Workflow

1. Parse whether this is a new campaign or a continuation.
2. Draft a compact design direction: title, achievement copy, motivational line, Toki action, theme elements, and whether layout should be reused.
3. Use ImageGen for background, 3D art title, decorative motion elements, and Toki when needed. Do not rely on ImageGen for long or critical text.
4. Use scripts or code-assisted compositing for portrait fitting, exact text, final size, and export.
5. Inspect the rendered poster before delivery. If the portrait is cropped badly, title text is wrong, Toki proportions drift, or text is too small/misaligned, revise before showing the user.
6. Save final user-facing files under the current workspace `outputs/` directory.

## Production Rules

- Prefer a hybrid workflow: ImageGen for visual richness, local compositing for accuracy.
- Generate main art typography as separate transparent/cutout assets when the user wants "art text" or references premium Chinese posters.
- For exact information text, render locally with reliable fonts and strong hierarchy: name, team, title, congratulation, month/theme.
- Run portrait fitting before circular/medal masking. Never use a fixed crop that may cut the head.
- Preserve user-provided portrait identity. Do not beautify, redraw, or replace the person's face unless explicitly requested.
- Same-month unified layout means keep the same composition, background, title system, Toki placement, frame, and info panel; only swap variable person data.

## Reusable Scripts

- `scripts/portrait_safe_crop.py`: create a square/circle-ready portrait crop using background and skin-tone heuristics, then save a preview.
- `scripts/validate_poster.py`: verify final PNG dimensions and basic file health.

## Common Mistakes

- Using ImageGen for all text, causing wrong names, tiny copy, or scrambled Chinese.
- Cropping a portrait by fixed percentages and cutting the head or shoulders.
- Making English layouts by simply shrinking text.
- Letting Toki become tall, bean-shaped, humanoid, or long-limbed.
- Reusing a fixed template when the user did not request same-month unified layout.

## Delivery Format

Show the rendered image inline when possible, link the final PNG from `outputs/`, and mention:

- final size verification,
- generated title/copy,
- whether this poster becomes the same-month master layout,
- any remaining risk if ImageGen text or IP detail is not perfect.
