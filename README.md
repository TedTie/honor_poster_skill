# Honor Poster Skill

## 中文

`honor-poster-skill` 是一个用于制作 51Talk 风格个人喜报的 Codex Skill。它帮助用户把人物照片、姓名、组别、语言、个人称号和月份/主题，整理成一张适合发布的竖版荣誉海报。

这个 skill 的目标是稳定产出“个人喜报”，而不是普通活动图或促销图。它会保留喜报应有的核心结构：标题、人物照片、姓名、组别、个人称号、祝贺文案、品牌标识和 Toki IP；同时根据不同月份、节日或主题调整整体视觉方向。

## 适合制作

- 销售达标喜报
- 月度销冠喜报
- 目标完成喜报
- 新人培训通过海报
- 团队荣誉表彰海报
- 中文或英文版个人喜报
- 同月多人统一排版的系列喜报

## 输出规格

| 项目 | 规格 |
| --- | --- |
| 尺寸 | `3508px x 4961px` |
| 格式 | PNG |
| 语言 | 中文 / 英文 |
| 主要生成方式 | ImageGen 整体视觉生成 + 原始人物照片保留 |

## 使用方式

开始一个新月份、新主题或新视觉方向时，请提供完整资料，并写明 `这是新的。`

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

如果是同一个月份或主题的下一位人员，只需要提供会变化的信息：

```text
个人照：已附
姓名：陈健雄
组别：MYC-CC01Team
语言：中文
个人称号：最牛气冲天的TL
是否同月统一排版：是
```

## 输入字段

| 字段 | 是否必填 | 说明 |
| --- | --- | --- |
| 个人照 | 是 | 用于海报的人物照片。 |
| 姓名 | 是 | 海报中显示的人名。 |
| 组别 | 是 | 例如 `MYC-CC01Team`。 |
| 语言 | 是 | `中文` 或 `英文`。 |
| 个人称号 | 是 | 例如 `最佳稳单之星`、`最专业销售达人`。 |
| 月份/主题 | 新主题必填 | 用于生成标题、祝贺语和整体视觉方向。 |
| 是否同月统一排版 | 是 | `是` 表示同月后续人员沿用同一套排版；`否` 表示可重新设计。 |

## 设计方向

Skill 会根据主题判断适合的色彩、动势、材质、道具和 Toki 表现方式。不同主题可以有不同风格，但成品始终应保持个人荣誉喜报的识别度。

人物照片默认保持原图，不重绘、不换脸、不改变人物外貌。Toki 和 51Talk logo 会使用仓库中的参考资产，以保持品牌一致性。

---

# Honor Poster Skill

## English

`honor-poster-skill` is a Codex Skill for creating 51Talk-style personal honor posters. It turns a portrait, name, team, language, personal title, and month/theme into a polished vertical recognition poster.

The goal of this skill is to consistently produce personal achievement posters, not generic campaign graphics or promotion ads. Each poster keeps the essential recognition structure: title, portrait, name, team, personal title, congratulation copy, brand mark, and Toki IP, while adapting the visual direction to the selected month or theme.

## Best For

- Sales achievement posters
- Monthly sales champion posters
- Target-hit celebration posters
- Newcomer or training-pass posters
- Team recognition posters
- Chinese or English personal honor posters
- Same-month multi-person poster series

## Output Specs

| Item | Spec |
| --- | --- |
| Size | `3508px x 4961px` |
| Format | PNG |
| Language | Chinese / English |
| Main method | ImageGen full-poster visual generation + preserved original portrait |

## How To Use

When starting a new month, theme, or visual direction, provide the full details and mark it as new:

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

For the next person in the same month or theme, provide only the changing details:

```text
Portrait: attached
Name: Chen Jianxiong
Team: MYC-CC01Team
Language: Chinese
Personal title: Strongest Skyrocket TL
Same-month unified layout: yes
```

## Input Fields

| Field | Required | Description |
| --- | --- | --- |
| Portrait | Yes | The person photo used in the poster. |
| Name | Yes | The displayed person name. |
| Team | Yes | Example: `MYC-CC01Team`. |
| Language | Yes | `Chinese` or `English`. |
| Personal title | Yes | Example: `Best Steady Sales Star`. |
| Month/theme | Required for new themes | Used to generate the title, congratulation copy, and visual direction. |
| Same-month unified layout | Yes | `yes` keeps the same monthly layout; `no` allows a new design. |

## Design Direction

The skill chooses color, motion, materials, props, and Toki treatment according to the theme. Different themes may look different, but the final output should always read as a personal honor poster.

The original portrait is preserved by default: no face redraw, face swap, or identity change. Toki and the 51Talk logo use the bundled reference assets to keep brand consistency.
