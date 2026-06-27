# Input Contract

## New Campaign

Treat the request as a new campaign when the user says `这是新的`, provides a new month/theme, or explicitly asks for a new design direction.

Required fields:

- `个人照`
- `姓名`
- `组别`
- `语言`: `中文` or `英文`
- `个人称号`: normally starts with `最佳`
- `月份/主题`
- `是否同月统一排版`: `是` or `否`

Generate or infer:

- Poster title.
- Target achievement congratulation.
- Sales motivational copy.
- Toki action, prop, and theme elements.
- Style intensity, defaulting to `强冲刺感`.

## Continuation

If the user does not say this is new, keep:

- month/theme,
- layout continuity decision,
- style intensity,
- title system,
- background visual DNA,
- Toki proportions and role,
- poster size.

Ask only for missing variable data that blocks output.

## Language Rules

Chinese:

- Keep title large and bold.
- Keep name and personal title visually strong.
- Use neat centered alignment unless the design concept clearly calls for asymmetry.

English:

- Translate or rewrite copy naturally instead of literal word stacking.
- Use fewer lines and wider text boxes.
- Reduce density before reducing font size.
- Avoid extremely small footer-style main information.

## Suggested Copy Patterns

Chinese title examples:

- `一飞冲天`
- `销售荣耀`
- `达标之星`
- `冲刺封神`
- `荣耀登峰`

Chinese motivational line examples:

- `专业成就信任，冲刺赢得高峰`
- `稳中突破，向目标全速进发`
- `每一次成交，都是实力的证明`
- `今日达标，是实力；持续达标，是王者`

English equivalents:

- `Target Achieved`
- `Sales Glory`
- `Skyrocket Success`
- `Congratulations on hitting the target`
- `Professional focus wins lasting trust`
