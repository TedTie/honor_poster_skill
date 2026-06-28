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

Dynamic references should influence movement, depth, and material richness, not make the poster chaotic. The finished poster must feel like a single designed image, not a background with local boxes and text pasted on top.

## ImageGen-First Principle

Use ImageGen to create the main poster as an integrated composition. The portrait, title, frame, ribbons, lighting, Toki, and information zones should be planned together.

Avoid this weak workflow:

1. Generate an empty background.
2. Paste the portrait into a blank circle.
3. Add flat rectangles and local fonts.

Prefer this workflow:

1. Inspect and prepare the portrait as a subject reference.
2. Prompt ImageGen for the complete poster composition, with the person placed naturally inside a premium medal/photo feature.
3. Ask ImageGen to render short art text directly: main title, subtitle, theme strip, congratulation badge.
4. Inspect aesthetic fit and revise with ImageGen until the whole image feels professional.
5. Only then use local compositing for exact final text if absolutely necessary.

## Layout Logic

Default vertical hierarchy, but with visual freedom:

1. Brand/logo.
2. Main art title.
3. Month/theme strip or subtitle.
4. Portrait in medal/circular/hero frame.
5. Congratulation badge.
6. Name.
7. Personal title.
8. Team.
9. Motivational line.

When same-month unified layout is `是`, keep the generated composition system stable for the month: same camera language, title treatment, portrait feature, Toki role, and information rhythm. When `否`, vary composition by theme and person.

## ImageGen Usage

Use ImageGen for:

- whole-poster key visual,
- portrait-integrated frame or medal design,
- art typography for short important text,
- 3D materials,
- ribbons, light trails, trophies, coins, seasonal motifs,
- Toki theme pose when proportions are explicitly constrained.

Avoid relying on ImageGen for:

- long dense text,
- small footer information,
- multi-line team/person details that must be exact,
- dense Chinese or English details.

For short text, prefer ImageGen art typography inside the whole poster. If exact text is wrong, try a localized ImageGen edit first. If local text correction is needed, match the generated material, lighting, shadow, outline, and perspective.

## Professional Finish Rules

- No obvious flat UI rectangles unless they are generated as part of the poster's material system.
- No default-looking system fonts for main visual text.
- No plain circular photo hole unless the circle is part of a rich medal/trophy frame generated with lighting and depth.
- No large blank gray photo background unless it is intentionally integrated.
- Use overlapping ribbons, foreground depth, light trails, glow, perspective, and frame shadows to connect the portrait with the scene.
- Let the title and portrait compete as the two strongest elements; do not make either feel pasted.

## Portrait Treatment

- Inspect the portrait first.
- Use the portrait as an ImageGen subject/reference when possible so the generated frame and light interact with the person.
- Fit by face and subject safety, not by fixed top/center crop.
- In medal or hero frames, keep the face, hair, shoulders, and key pose intact.
- If the photo has lots of empty background, crop tighter before using it as a reference.
- Do not redraw the person's identity unless the user asks for illustration or retouching.

## Text Hierarchy

- Main title: ImageGen art typography, largest, visually dominant.
- Name: second-largest exact text, high contrast.
- Personal title: strong, readable, usually gold or white-gold.
- Team: clean sans-serif, smaller but clear.
- Motivational line: one or two lines max.

If copy is too long, rewrite it shorter before shrinking.

## 51Talk Logo

If no official logo asset is provided, recreate or prompt a simple yellow rounded rectangle with blue `51Talk` text as a brand mark. Keep it visually integrated, not floating like a generic label. Do not invent extra official taglines unless the user provides them.
