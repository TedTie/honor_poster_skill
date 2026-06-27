# Design System

## Visual DNA

The user likes high-impact honor posters with:

- red-gold celebration palettes,
- 3D metallic titles,
- flowing ribbons and light trails,
- circular medal/photo frames,
- fireworks, coins, trophies, stages, and upward motion,
- 51Talk yellow-blue logo treatment,
- readable name/team/title hierarchy.

Dynamic references should influence movement, depth, and material richness, not make the poster chaotic.

## Layout Logic

Default vertical hierarchy:

1. Brand/logo.
2. Main art title.
3. Month/theme strip or subtitle.
4. Portrait in medal/circular/hero frame.
5. Congratulation badge.
6. Name.
7. Personal title.
8. Team.
9. Motivational line.

When same-month unified layout is `是`, keep these positions stable for the month. When `否`, vary composition by theme and person.

## ImageGen Usage

Use ImageGen for:

- background scene,
- art typography,
- 3D materials,
- ribbons, light trails, trophies, coins, seasonal motifs,
- Toki theme pose when proportions are explicitly constrained.

Avoid relying on ImageGen for:

- exact names,
- team codes,
- long congratulation copy,
- dense Chinese or English details.

For art typography, generate isolated text assets on a flat chroma-key background or clean background, then remove the background and composite.

## Portrait Treatment

- Inspect the portrait first.
- Fit by face and subject safety, not by fixed top/center crop.
- In circular frames, keep the face, hair, shoulders, and key pose intact.
- If the photo has lots of empty background, crop tighter before masking.
- Do not redraw the person unless the user asks for illustration or retouching.

## Text Hierarchy

- Main title: art typography, largest, visually dominant.
- Name: second-largest exact text, high contrast.
- Personal title: strong, readable, usually gold or white-gold.
- Team: clean sans-serif, smaller but clear.
- Motivational line: one or two lines max.

If copy is too long, rewrite it shorter before shrinking.

## 51Talk Logo

If no official logo asset is provided, recreate a simple yellow rounded rectangle with blue `51Talk` text as a placeholder-like brand mark. Do not invent extra official taglines unless the user provides them.
