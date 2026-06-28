---
name: honor-poster-skill
description: Use when creating 51Talk-style personal achievement, honor, sales target, onboarding, or celebration posters that need a locked original portrait, name, team, Chinese or English layout, Toki IP, ImageGen art typography, same-month layout continuity, campaign-level copy, and 3508x4961 PNG output.
---

# Honor Poster Skill

## Overview

Create polished personal honor posters for 51Talk-style sales achievements. Use ImageGen as the primary art director for the poster environment, title treatment, frame system, Toki, and motion effects. Treat the supplied portrait as a locked original-photo layer: do not redraw, beautify, face-swap, cut out, or alter the person unless the user explicitly asks for it.

## Default Poster Contract

- Output size: always `3508 x 4961` PNG unless the user explicitly changes it.
- Required first poster inputs for a new campaign: portrait, name, team, language, personal title (`最佳...` or equivalent), month/theme, and same-month layout yes/no.
- Required same-campaign inputs: portrait, name, team, language, personal title, and same-month layout yes/no.
- If the user says `这是新的`, start a new campaign/theme. Otherwise carry forward the previous campaign/month settings.
- Default style intensity: `强冲刺感`.
- Use Chinese or English according to `语言`. English needs wider, lower-density text blocks; never shrink text until it becomes decorative dust.

Read when needed:

- `references/input-contract.md` for input parsing and carry-over rules.
- `references/design-system.md` for layout, typography, ImageGen, language, and complexity rules.
- `references/toki-ip.md` before generating or editing any Toki element.
- `references/quality-checklist.md` before delivery.

Use bundled visual references when creating poster prompts:

- `assets/toki-three-view-reference.png`: visual reference for Toki's fixed IP proportions and core features.
- `assets/51talk-logo-reference.png`: default rounded transparent 51Talk logo asset for poster placement.
- `assets/51talk-logo-original.png`: original rectangular logo backup/reference; use only if the user asks for the uncropped version.

## Workflow

1. Parse whether this is a new campaign or a continuation.
2. Separate campaign-level text from person-level text.
   - Campaign-level: main title, subtitle/theme, congratulation badge, motivational sales line, visual motif, and Toki role.
   - Person-level: portrait, name, team, personal title.
3. Generate campaign-level title and copy from the month/theme, not from the personal title. The personal title belongs in the person information area.
4. Draft a compact design direction: honor-poster hierarchy, restrained theme elements, Toki action, portrait-window shape, top-left logo placement, and whether layout should be reused.
5. Prepare ImageGen prompts for a complete poster frame/environment, not a blank background. The ImageGen design should include premium art typography, photo-window/frame, foreground depth, ribbons/light trails, Toki, and enough negative space for readable information.
6. Reserve the portrait area as a chroma-key window (`#00FF00`) or clearly removable placeholder when local locked-photo compositing is needed.
7. Do not ask ImageGen to regenerate the person's face/body. Place the original portrait underneath or inside the generated window as locked pixels.
8. Inspect the result. If the original portrait does not fit the generated frame, revise the generated frame/window or adjust the original photo's proportional placement. Do not solve it by redrawing or cutting out the person.
9. Use scripts or code-assisted compositing only for locked portrait placement, transparent window removal, final exact text fixes, size export, small logo correction, or validation. These local layers must match the generated art style and must not look like simple rectangles, plain circles, or default fonts.
10. Save final user-facing files under the current workspace `outputs/` directory.

## Production Rules

- Prefer an ImageGen-first workflow: the main poster should be one integrated generated design, not a locally assembled layout.
- Highest portrait rule: preserve the supplied portrait. Do not use ImageGen to reinterpret, repaint, beautify, face-swap, change expression, change hairstyle, change clothing, slim the body, or alter identity.
- Do not cut out/remove the portrait background unless the user explicitly asks. Use the original photo as a rectangular, rounded-rectangle, oval, arch, magazine-card, medal, stage-screen, or premium photo-window layer.
- Allowed portrait operations: non-destructive proportional scaling, photo-window masking, slight rotation if part of the frame, and optional subtle color/brightness matching. Do not change facial features or body shape.
- Generate main title, short subtitle, congratulation badge, and theme text as ImageGen art typography when possible.
- For exact information text that ImageGen may misspell, first try a targeted ImageGen text-region edit. Use local text only as last-mile correction, and style it to blend into the poster.
- Do not build the main visual from simple local shapes, generic rounded boxes, flat panels, or ordinary system-font typography.
- Run portrait fitting before any mask or edit guidance. Never use a fixed crop that may cut the head.
- Keep the 51Talk logo in the top-left brand zone by default. Use the bundled rounded transparent logo asset when compositing or as the prompt reference. Do not center it unless the user explicitly requests it or an approved same-month master layout already uses that placement.
- Toki is proportion-locked but not template-locked. Recreate Toki from the IP proportion rules each time, with pose/props/location selected for the current theme.
- Same-month unified layout means keep the same composition, background, title system, Toki role, frame, and information rhythm; only swap variable person data.

## Common Mistakes

- Reusing the last poster's Toki pose, location, or prop when the new theme calls for a different role.
- Letting 618, shopping, coupons, gifts, fireworks, ribbons, city lights, trophies, coins, and slogans all appear at once. A honor poster needs focus.
- Using the personal title as the main campaign title or motivational line.
- Treating local code shapes and fonts as the poster design instead of using ImageGen for the whole visual.
- Letting ImageGen recreate the person and accidentally changing their face, body, clothing, or expression.
- Cutting out the person from the original photo when the user wanted the original portrait preserved.
- Using ImageGen for long text without checking, causing wrong names, tiny copy, or scrambled Chinese.
- Cropping a portrait by fixed percentages and cutting the head or shoulders.
- Making English layouts by simply shrinking text.
- Letting Toki become tall, bean-shaped, humanoid, or long-limbed.
- Reusing a fixed template when the user did not request same-month unified layout.
- Recreating the 51Talk logo from memory when the bundled logo asset is available.

## Reusable Scripts

- `scripts/portrait_safe_crop.py`: preflight original-photo placement and create a safe crop reference. This must not be used as permission to cut out or alter the person.
- `scripts/validate_poster.py`: verify final PNG dimensions and basic file health.

## Delivery Format

Show the rendered image inline when possible, link the final PNG from `outputs/`, and mention:

- final size verification,
- generated campaign title/copy,
- whether this poster becomes the same-month master layout,
- any remaining risk if ImageGen text or IP detail is not perfect.
