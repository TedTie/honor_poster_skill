# Honor Poster Skill

## 中文说明

`honor-poster-skill` 用于制作 51Talk 风格的个人喜报、销售达标喜报、销冠喜报、新人欢迎海报和荣誉表彰海报。它的重点不是固定模板，而是把用户提供的月份/主题、人物资料、语言、个人称号和是否同月统一排版，转化成一张完整的高冲击感海报。

这个 skill 默认输出 `3508px x 4961px` 的 PNG 海报。它会优先使用 ImageGen 生成整体视觉：艺术标题、红金流动感、3D 金属质感、奖章/舞台/卡片式人物窗口、Toki IP、光效、丝带和主题元素。人物照片则作为锁定的原始照片层处理，原则上不让 ImageGen 重绘、换脸、美颜、改变衣服、改变发型或改变身形。

## 适用场景

- 个人销售达标喜报
- 月度销冠或销售冠军海报
- 目标达成、冲刺成功、荣誉表彰海报
- 新人欢迎、培训通过、团队表扬海报
- 中文或英文版喜报
- 同月多人统一排版的系列喜报
- 不同月份/主题使用不同设计语言的主题喜报

## 核心设计规则

- 海报尺寸固定为 `3508px x 4961px`。
- 51Talk logo 默认放在左上角品牌区。
- 使用 `assets/51talk-logo-reference.png` 作为默认圆角透明 logo 资产。
- Toki 必须参考 `assets/toki-three-view-reference.png` 的三视图比例。
- Toki 可以根据主题改变动作、服装、道具和位置，但不能改变矮胖梨形比例。
- 个人照片必须保持原图，不主动抠图，不重绘人物，不改变人物长相。
- 主标题、主题字、祝贺字优先由 ImageGen 生成艺术字。
- 姓名、组别、个人称号等必须准确可读。
- 主题标题和激励语根据月份/主题生成，不使用个人称号来代替主题标题。
- 背景复杂度要受控，不能像促销广告一样堆满元素。

## 必填信息

新主题/新月份第一次制作时，请提供：

```text
这是新的。

个人照：已附
姓名：刘丹
组别：MYC-CC01Team
语言：中文
个人称号：最专业销售达人
月份/主题：6月一飞冲天
是否同月统一排版：是
```

如果是同一个月份/主题的下一个人，只需要提供：

```text
个人照：已附
姓名：陈健雄
组别：MYC-CC01Team
语言：中文
个人称号：最牛气冲天的TL
是否同月统一排版：是
```

如果要换主题、换月份或换整体设计方向，请重新写 `这是新的。`

## 字段说明

`个人照`  
用于放入海报的人物照片。默认保留原图，不改变人物身份和外貌。

`姓名`  
海报中的人物姓名，必须准确。

`组别`  
例如 `MYC-CC01Team`、`MY-SS01Team`，必须准确。

`语言`  
支持 `中文` 或 `英文`。英文版会调整排版密度，避免文字过小。

`个人称号`  
例如 `最专业销售达人`、`最佳稳单之星`、`最牛气冲天的TL`。它属于个人信息区，不作为主标题。

`月份/主题`  
用于生成海报主标题、主题视觉、祝贺语和销售激励语。例如 `6月 618 销冠`、`June Target Hit`、`夏季冲刺`。

`是否同月统一排版`  
选择 `是` 时，同月后续人员保持同一套构图、主题、Toki 角色、标题系统和信息节奏，只替换人物和文字。选择 `否` 时，可以根据人物与主题重新设计排版。

## 推荐工作流

1. 用户提供新主题资料和人物照片。
2. Skill 生成主题标题、祝贺语和销售激励语。
3. ImageGen 生成完整海报视觉和艺术字，并预留可替换的人物照片窗口。
4. 原始人物照片作为锁定图层放入窗口，不让 ImageGen 修改人物。
5. 检查人物是否对齐、文字是否清晰、Toki 是否符合比例、logo 是否在左上角。
6. 输出 `3508px x 4961px` PNG。
7. 如果同月统一排版为 `是`，后续人员沿用该月母版节奏。

## 示例请求

```text
使用 honor-poster-skill 做一张喜报。

这是新的。
个人照：已附
姓名：Nur Azzatul
组别：MY-CC01Team
语言：英文
个人称号：Best Steady Sales Star
月份/主题：June Target Hit
是否同月统一排版：否
```

```text
使用 honor-poster-skill 做一张喜报。

这是新的。
个人照：已附
姓名：陈健雄
组别：MYC-CC01Team
语言：中文
个人称号：最牛气冲天的TL
月份/主题：6月 618 销冠
是否同月统一排版：否
```

## 输出检查

每张海报交付前需要确认：

- 尺寸是 `3508px x 4961px`。
- logo 在左上角，且使用圆角品牌资产。
- 人物没有被 AI 重绘或改变。
- 人物头部没有被裁掉。
- 标题、姓名、组别、个人称号和祝贺文案清晰可读。
- 主题标题和激励语来自月份/主题。
- Toki 是矮胖梨形比例，不是瘦高普通卡通。
- 整体像个人喜报，不像促销广告。

---

# Honor Poster Skill

## English Guide

`honor-poster-skill` creates 51Talk-style personal honor posters, sales achievement posters, sales champion posters, onboarding posters, and recognition posters. It is not a fixed-template poster generator. It turns the user's month/theme, person details, language, personal title, and same-month layout choice into a polished high-impact poster.

The default output is a `3508px x 4961px` PNG poster. The skill uses ImageGen as the primary visual designer for the full poster: art typography, red-gold motion, 3D metallic materials, medal/stage/card portrait windows, Toki IP, lighting, ribbons, and theme symbols. The supplied portrait is treated as a locked original-photo layer and should not be redrawn, face-swapped, beautified, restyled, or reshaped by ImageGen.

## Use Cases

- Personal sales target achievement posters
- Monthly sales champion posters
- Target-hit, sprint-success, and honor recognition posters
- Newcomer welcome or training-pass posters
- Chinese or English honor posters
- Same-month multi-person poster series
- Different monthly themes with different design directions

## Core Design Rules

- Poster size is fixed at `3508px x 4961px`.
- The 51Talk logo is placed in the top-left brand zone by default.
- Use `assets/51talk-logo-reference.png` as the default rounded transparent logo asset.
- Toki must follow the proportions in `assets/toki-three-view-reference.png`.
- Toki may change pose, outfit, prop, and placement according to the theme, but must keep the short chubby pear-shaped IP proportions.
- The portrait must remain the original photo. Do not cut out, redraw, beautify, or alter the person's identity.
- Main title, theme words, and congratulation words should be generated as ImageGen art typography when possible.
- Name, team, and personal title must be exact and readable.
- Campaign titles and motivational copy must come from the month/theme, not from the personal title.
- Background complexity must be controlled; the result should feel like a personal honor poster, not a crowded promotion ad.

## Required Inputs

For the first poster of a new campaign/month, provide:

```text
This is new.

Portrait: attached
Name: Liu Dan
Team: MYC-CC01Team
Language: Chinese
Personal title: Most Professional Sales Talent
Month/theme: June Skyrocket Success
Same-month unified layout: yes
```

For the next person in the same month/theme, provide only:

```text
Portrait: attached
Name: Chen Jianxiong
Team: MYC-CC01Team
Language: Chinese
Personal title: Strongest Skyrocket TL
Same-month unified layout: yes
```

If the month, theme, or overall design direction changes, start again with `This is new.`

## Field Guide

`Portrait`  
The person's photo used in the poster. By default, the original photo is preserved without identity or appearance changes.

`Name`  
The person's displayed name. It must be exact.

`Team`  
For example `MYC-CC01Team` or `MY-SS01Team`. It must be exact.

`Language`  
Use `Chinese` or `English`. English layouts need lower text density and wider text zones to avoid tiny copy.

`Personal title`  
For example `Best Steady Sales Star`, `Most Professional Sales Talent`, or `Strongest Skyrocket TL`. This belongs in the personal information area, not as the main campaign title.

`Month/theme`  
Used to generate the campaign title, visual motif, congratulation line, and sales motivational copy. Examples: `June Target Hit`, `June 618 Sales Champion`, `Summer Sprint`.

`Same-month unified layout`  
When `yes`, later posters in the same month keep the same composition, theme, Toki role, title system, and information rhythm while swapping the person photo and text. When `no`, the layout can vary by person and theme.

## Recommended Workflow

1. The user provides a new theme and portrait.
2. The skill generates the campaign title, congratulation line, and sales motivational copy.
3. ImageGen creates the integrated poster visual and art typography with a replaceable portrait window.
4. The original portrait is placed into the window as a locked photo layer.
5. Check portrait alignment, text readability, Toki proportions, and top-left logo placement.
6. Export a `3508px x 4961px` PNG.
7. If same-month unified layout is `yes`, reuse the approved monthly layout rhythm for later people.

## Example Requests

```text
Use honor-poster-skill to create an achievement poster.

This is new.
Portrait: attached
Name: Nur Azzatul
Team: MY-CC01Team
Language: English
Personal title: Best Steady Sales Star
Month/theme: June Target Hit
Same-month unified layout: no
```

```text
Use honor-poster-skill to create an achievement poster.

This is new.
Portrait: attached
Name: Chen Jianxiong
Team: MYC-CC01Team
Language: Chinese
Personal title: Strongest Skyrocket TL
Month/theme: June 618 Sales Champion
Same-month unified layout: no
```

## Output Checklist

Before delivery, confirm:

- The size is `3508px x 4961px`.
- The logo is in the top-left corner and uses the rounded brand asset.
- The person has not been redrawn or altered by AI.
- The head is not cropped.
- Title, name, team, personal title, and congratulation copy are readable.
- Campaign title and motivational copy are based on the month/theme.
- Toki keeps the short chubby pear-shaped proportions.
- The poster reads as a personal honor poster, not a promotion ad.
