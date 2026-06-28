---
name: honor-poster-skill
description: Use when creating 51Talk-style personal achievement, honor, sales target, onboarding, or celebration posters that need a portrait, name, team, Chinese or English layout, Toki IP, ImageGen art typography, same-month layout continuity, and 3508x4961 PNG output.
---

# Honor Poster Skill

## Overview

Create polished personal honor posters for 51Talk-style sales achievements. Use ImageGen as the primary art director for the poster environment, frame system, Toki, motion effects, and art typography. Treat the user's supplied portrait as a locked original-photo layer: do not redraw, beautify, face-swap, cut out, or otherwise alter the person unless the user explicitly asks for it.

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
3. Prepare ImageGen prompts for a complete poster frame/environment, not a blank background. The ImageGen design should include a premium photo window, medal frame, foreground ribbons, shadows, and lighting that can hold the original portrait naturally.
4. Do not ask ImageGen to regenerate the person's face/body. Generate the scene with a reserved portrait area, placeholder photo zone, or frame design, then place the original portrait into that area as locked pixels.
5. Generate short art text with ImageGen when possible: main title, subtitle, congratulation badge, and theme label. Keep exact variable text short and explicit.
6. Inspect the result. If the original portrait does not fit the generated frame, revise the ImageGen frame/environment or adjust the original photo's scale/crop. Do not solve it by redrawing the person.
7. Use scripts or code-assisted compositing only for placing the locked original photo, final exact text fixes, size export, small logo correction, or checking portrait crop. These local layers must match the generated art style and must not look like simple rectangles, plain circles, or default fonts placed on top.
8. Save final user-facing files under the current workspace `outputs/` directory.

## Production Rules

- Prefer an ImageGen-first workflow: the main poster should be one integrated generated design, not a locally assembled layout.
- Highest portrait rule: preserve the supplied portrait. Do not use ImageGen to reinterpret, repaint, beautify, face-swap, change expression, change hairstyle, change clothing, slim the body, or alter identity.
- Do not cut out/remove the portrait background unless the user explicitly asks. Prefer using the original photo as a rectangular, rounded-rectangle, oval, arch, or premium photo-window layer inside a generated frame.
- Allowed portrait operations: non-destructive proportional scaling, crop for framing, slight rotation if part of the frame, and optional subtle color/brightness matching. Do not change facial features or body shape.
- Generate main title, short subtitle, congratulation badge, and theme text as ImageGen art typography when possible.
- For exact information text that ImageGen may misspell, first try a targeted ImageGen text-region edit. Use local text only as a last-mile correction, and style it to blend into the poster.
- Do not build the main visual from simple local shapes, generic rounded boxes, flat panels, or ordinary system-font typography.
- Run portrait fitting before any mask or edit guidance. Never use a fixed crop that may cut the head.
- Preserve user-provided portrait identity and original photo pixels. Do not beautify, redraw, or replace the person's face unless explicitly requested.
- Same-month unified layout means keep the same composition, background, title system, Toki placement, frame, and info panel; only swap variable person data.

## Reusable Scripts

- `scripts/portrait_safe_crop.py`: preflight original-photo placement and create a safe crop reference. This must not be used as permission to cut out or alter the person.
- `scripts/validate_poster.py`: verify final PNG dimensions and basic file health.

## Common Mistakes

- Treating local code shapes and fonts as the poster design instead of using ImageGen for the whole visual.
- Letting ImageGen recreate the person and accidentally changing their face, body, clothing, or expression.
- Cutting out the person from the original photo when the user wanted the original portrait preserved.
- Using ImageGen for long text without checking, causing wrong names, tiny copy, or scrambled Chinese.
- Placing a portrait into a generated empty hole after the fact when ImageGen should have designed the frame around the person.
- Using plain system fonts, flat panels, or simple circles that make the poster look like a template.
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
