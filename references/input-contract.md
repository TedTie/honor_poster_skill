# Input Contract

## New Campaign

Treat the request as a new campaign when the user says `这是新的`, provides a new month/theme, or explicitly asks for a new design direction.

Required fields:

- portrait,
- name,
- team,
- language: `中文` or `英文`,
- personal title: normally starts with `最佳`,
- month/theme,
- same-month unified layout: `是` or `否`.

Generate or infer from the month/theme:

- campaign title,
- target achievement congratulation,
- sales motivational copy,
- Toki action, prop, and location,
- restrained theme elements,
- style intensity, defaulting to `强冲刺感`.

## Continuation

If the user does not say this is new, keep:

- month/theme,
- layout continuity decision,
- style intensity,
- campaign title system,
- achievement congratulation,
- motivational line,
- background visual DNA,
- Toki role if same-month unified layout is `是`,
- poster size.

Ask only for missing variable data that blocks output.

## Campaign Copy Rules

Generate title and copy from the month/theme, not from the personal title.

For example:

- Theme: `6月 618 销冠`
- Campaign title: `618 销冠荣耀`
- Subtitle/theme strip: `六月战绩登峰`
- Congratulation badge: `热烈祝贺`
- Motivational line: `六月销冠，实力登峰`
- Person title: `最牛气冲天的TL` stays near the person's name.

## Language Rules

Chinese:

- Keep title large and bold.
- Keep name and personal title visually strong.
- Use neat centered alignment unless the design concept clearly calls for asymmetry.
- Prefer compact, powerful copy over long lines.

English:

- Translate or rewrite copy naturally instead of literal word stacking.
- Use fewer lines and wider text boxes.
- Reduce density before reducing font size.
- Avoid extremely small footer-style main information.

## Suggested Copy Patterns

Chinese campaign titles:

- `618 销冠荣耀`
- `六月战绩登峰`
- `一飞冲天`
- `目标达成`
- `销售精英荣耀时刻`

Chinese motivational lines:

- `六月销冠，实力登峰`
- `战绩破浪，冲刺赢得高峰`
- `一鼓作气向前，业绩再攀新峰`
- `专业成就信任，冲刺赢得高峰`

English equivalents:

- `Sales Champion Glory`
- `Target Achieved`
- `Skyrocket Success`
- `Congratulations on hitting the target`
- `Professional focus wins lasting trust`
