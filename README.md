# Honor Poster Skill

## 中文

`honor-poster-skill` 是一个用于制作 51Talk 风格个人喜报的 Codex Skill。它适合用于销售达标、月度销冠、目标完成、新人通过培训、团队荣誉表彰等场景，把用户提供的人物照片、姓名、组别、语言、个人称号和月份/主题，转化成一张完整的高质感竖版喜报。

这个 skill 的核心不是套用固定模板，而是保持稳定的“喜报 DNA”，再根据不同月份、节日或主题调整视觉元素。也就是说，主题会影响颜色、材质、道具、背景动势和 Toki 的动作，但不会改变海报类型。比如 `6月 618 销冠` 应该是一张带有 618 氛围的销冠喜报，而不是电商促销海报。

## 输出标准

- 输出尺寸固定为 `3508px x 4961px`。
- 输出格式为 PNG。
- 支持中文和英文排版。
- 支持同月多人统一排版，也支持不同主题使用不同设计。
- 默认风格强度为 `强冲刺感`，但视觉元素必须按主题判断。

## 核心原则

### 1. 喜报 DNA 优先

每张海报都必须首先像“个人喜报/荣誉海报”，而不是广告、活动海报或产品宣传图。必须保留这些核心信息：

- 主标题
- 祝贺/达标文案
- 人物照片
- 姓名
- 组别
- 个人称号
- 51Talk logo
- Toki IP
- 销售激励语或荣誉表达

### 2. 主题决定元素，不决定海报类型

主题只用于选择视觉语言，例如色彩、动势、道具、材质、季节感、节日氛围和 Toki 动作。红金、光效、丝带、烟花、金属字、618 数字、奖杯、金币等都只是可选元素，不能每张海报固定使用。

### 3. 人物照片必须保持原图

用户提供的人物照片是锁定的原始照片层。默认不让 ImageGen 重绘人物，不换脸，不美颜，不改变发型、衣服、表情、身形或身份。不主动抠图，除非用户明确要求。

### 4. Toki 必须遵守 IP 比例

Toki 可以根据主题改变动作、道具、服装和位置，但必须严格参考三视图比例：矮胖、头身一体、三角梨形、大眼睛、红圆鼻、短圆四肢、顶部弯冠。不能生成瘦高、长手长脚或普通人形玩偶。

### 5. 51Talk logo 固定品牌位置

默认使用 `assets/51talk-logo-reference.png` 的圆角透明 logo，放在左上角品牌区。不要默认放中间，除非用户明确要求或同月统一模板已经确认这样设计。

## 使用方式

### 新主题/新月份第一次制作

当你要开始一个新主题、新月份或新视觉方向时，请写 `这是新的。`，并提供完整资料：

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

Skill 会根据 `月份/主题` 生成主标题、祝贺文案、销售激励语、Toki 动作和主题视觉。

### 同一个月份/主题的下一个人

如果不是新主题，只需要提供会变化的人物资料：

```text
个人照：已附
姓名：陈健雄
组别：MYC-CC01Team
语言：中文
个人称号：最牛气冲天的TL
是否同月统一排版：是
```

如果 `是否同月统一排版` 为 `是`，后续人员会沿用该月已经确定的构图、标题系统、Toki 角色、人物窗口和信息节奏，只替换照片与个人文字。

## 输入字段说明

| 字段 | 说明 |
| --- | --- |
| 个人照 | 必填。用于放入海报的人物照片，默认保持原图。 |
| 姓名 | 必填。必须准确显示在海报中。 |
| 组别 | 必填。例如 `MYC-CC01Team`、`MY-SS01Team`。 |
| 语言 | 必填。填写 `中文` 或 `英文`。英文版会调整文字密度，避免字太小。 |
| 个人称号 | 必填。例如 `最佳稳单之星`、`最专业销售达人`。属于个人信息区，不作为主标题。 |
| 月份/主题 | 新主题必填。用于生成主标题、视觉方向、祝贺语和激励语。 |
| 是否同月统一排版 | 必填。填写 `是` 或 `否`。 |

## 示例

### 中文喜报

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

预期方向：生成一张“销冠喜报”，可以带少量 618 数字、冠军奖杯、销售登峰感或电商节氛围，但不能变成满减促销图。

### 英文喜报

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

预期方向：生成英文版 target-hit achievement poster。英文文字较长时应调整版式密度，而不是把文字缩得很小。

## 交付前检查

生成海报前后应确认：

- 尺寸是 `3508px x 4961px`。
- 海报首先像个人喜报，而不是促销广告。
- 标题、姓名、组别、个人称号、祝贺语清晰可读。
- 主题元素服务于荣誉表达，没有盖过人物和达标信息。
- 人物照片没有被 AI 改脸、改身形或重绘。
- Toki 符合三视图比例。
- 51Talk logo 在左上角品牌区。
- 中文和英文排版都整齐可看。

---

# Honor Poster Skill

## English

`honor-poster-skill` is a Codex Skill for creating 51Talk-style personal honor posters. It is designed for sales target achievements, monthly sales champions, target-hit celebrations, onboarding recognition, training-pass posters, and team honor announcements. It turns the user's portrait, name, team, language, personal title, and month/theme into a polished vertical recognition poster.

This skill is not a fixed-template generator. It preserves a consistent honor-poster DNA while adapting visual elements to each month, event, or theme. The theme may influence color, materials, props, background motion, and Toki's role, but it must not change the poster type. For example, `June 618 Sales Champion` should become a sales champion honor poster with restrained 618 cues, not an e-commerce discount banner.

## Output Standard

- Final size is always `3508px x 4961px`.
- Final format is PNG.
- Chinese and English layouts are supported.
- Same-month multi-person layout continuity is supported.
- Different themes can use different design directions.
- Default style intensity is `强冲刺感`, but all visual elements must be selected according to the theme.

## Core Principles

### 1. Honor DNA Comes First

Every poster must first read as a personal honor or recognition poster, not an ad, event flyer, or product poster. These elements must remain visible:

- main title,
- congratulation or target-hit copy,
- portrait,
- name,
- team,
- personal title,
- 51Talk logo,
- Toki IP,
- sales motivation or recognition message.

### 2. Theme Selects Elements, Not Poster Type

The theme selects the visual language: color, motion, props, materials, seasonality, event cues, and Toki's action. Red-gold palettes, strong lighting, ribbons, fireworks, metallic titles, 618 numerals, trophies, and coins are optional elements. They should not appear by default in every poster.

### 3. Preserve the Original Portrait

The supplied portrait is a locked original-photo layer. By default, ImageGen should not redraw, face-swap, beautify, restyle, reshape, or alter the person's identity. Do not cut out the person unless the user explicitly asks for it.

### 4. Keep Toki On-Model

Toki may change action, props, outfit, and placement according to the theme, but must strictly follow the three-view proportions: short, chubby, head-body-integrated, triangular pear-shaped, huge eyes, red round nose, short round limbs, and top curved crest. Do not make Toki tall, slim, long-limbed, or humanoid.

### 5. Keep the 51Talk Logo in the Brand Zone

Use `assets/51talk-logo-reference.png` as the default rounded transparent logo asset. Place it in the top-left brand zone by default. Do not center the logo unless the user explicitly requests it or an approved same-month master layout already uses that placement.

## How to Use

### First Poster of a New Month or Theme

When starting a new month, theme, or visual direction, include `This is new.` and provide the full set of details:

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

The skill will generate the campaign title, congratulation copy, sales motivational line, Toki action, and theme direction from the month/theme.

### Next Person in the Same Month or Theme

If the theme has not changed, provide only the variable person details:

```text
Portrait: attached
Name: Chen Jianxiong
Team: MYC-CC01Team
Language: Chinese
Personal title: Strongest Skyrocket TL
Same-month unified layout: yes
```

If `Same-month unified layout` is `yes`, later posters should keep the approved monthly composition, title system, Toki role, portrait window, and information rhythm while replacing only the portrait and person-specific text.

## Input Fields

| Field | Description |
| --- | --- |
| Portrait | Required. The person photo used in the poster. Keep it as the original photo by default. |
| Name | Required. Must be displayed exactly. |
| Team | Required. Examples: `MYC-CC01Team`, `MY-SS01Team`. |
| Language | Required. Use `Chinese` or `English`. English layouts need lower density and wider text zones. |
| Personal title | Required. Example: `Best Steady Sales Star`. It belongs in the personal info area, not as the main title. |
| Month/theme | Required for new themes. Used to generate the title, visual direction, congratulation copy, and motivational line. |
| Same-month unified layout | Required. Use `yes` or `no`. |

## Examples

### Chinese Poster

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

Expected direction: create a sales champion honor poster. It may use restrained 618 numerals, a champion trophy, a sales peak feeling, or light e-commerce festival cues, but it must not become a discount promotion banner.

### English Poster

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

Expected direction: create an English target-hit achievement poster. If the English text is longer, adjust layout density instead of shrinking important information into tiny text.

## Delivery Checklist

Before delivery, confirm:

- The final size is `3508px x 4961px`.
- The poster reads as personal recognition first, not a promotion ad.
- Title, name, team, personal title, and congratulation copy are readable.
- Theme elements support the honor message and do not overpower the person or achievement.
- The portrait has not been redrawn, reshaped, or altered by AI.
- Toki follows the three-view proportions.
- The 51Talk logo is in the top-left brand zone.
- Chinese or English layout is neat and readable.
