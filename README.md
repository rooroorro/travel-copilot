# ✈️ Travel Copilot

**把旅行想法、PDF 和零散笔记，变成真正能带着走的互动行程。**

Turn travel ideas and existing itineraries into reviewed plans, interactive HTML companions, and personal calendar reminders.

**v1.1.0 · MIT · Python + 原生 HTML/CSS/JS · 平台无关 Agent Skill**

[开始安装](docs/installation.md) · [体验 Demo](docs/demo.md) · [架构](docs/architecture.md) · [版本说明](docs/releases/v1.1.0.md) · [参与贡献](CONTRIBUTING.md)

## 从计划到出发

1. **提供素材**：说出目的地、日期、同行人，或上传已有行程。文件解析使用所在 Agent 的能力。
2. **行程体检**：梳理交通衔接、预约、缓冲、准备事项与天气备选，和你讨论遗漏。
3. **确认定稿**：保留已确定的安排，将确认后的计划冻结为 `trip.json`。
4. **视觉导演**：推荐 5–8 个目的地相关的视觉方向，选择后形成 `creative_brief.json`。
5. **随身行程**：生成 HTML，查看时间轴、Now/Next、地图、清单与导航，按同行人导出 ICS。

## 现在可以做什么

| 能力 | v1.1.0 状态 |
| --- | --- |
| 行程整理、审查、讨论和定稿 | 由 Skill 指导 Agent 执行 |
| 通用单文件 HTML | 基础渲染器提供 5 个主题、时间轴、Now/Next、本地完成状态 |
| 地图故事与导航 | Leaflet + OpenStreetMap；地图与外部导航需要联网 |
| 同行人提醒 | 浏览器按身份和优先级导出 ICS；Python 提供命令行导出 |
| Visual Director | 已有工作流；视觉模板仍为实验性日本主题，存在固定路线和日期文案 |
| 跨平台 | 共用同一数据结构和脚本；安装方式随客户端变化，未逐一实机认证 |

**视觉模板的范围**：`build_visual_html.py` 能注入行程与 brief，但不能把任意设计意图自动转成新页面。通用旅行建议先用 `build_html.py`。原包未包含完整的 Tokyo Neon × Kyoto Zen 展示页及其 brief；本仓库不会将其写成已附带的 Demo。详见[已知限制](docs/known-limitations.md)。

## 先看 Demo

下载或解压本仓库，直接用浏览器打开 [examples/demo-trip.html](examples/demo-trip.html)。GitHub 文件页显示源码，下载后才能交互；[Demo 指南](docs/demo.md)提供完整操作步骤。

示例为 **东京 3 日城市漫游**，同行人使用“旅人 A / B / C”。用于说明产品交互，不代表真实预订或经过核验的出行方案。未嵌入第三方照片，无需申请地图 API Key。

## 安装

需要能读取 Skill 文件的 Agent；执行脚本建议 **Python 3.9+**，仅使用标准库，不需要安装 Python 包或 Node.js。查看 HTML 不需要 Python。

| 客户端 | 安装入口 |
| --- | --- |
| Claude Code | 将完整目录放到 `~/.claude/skills/travel-copilot/` |
| Codex | 将完整目录放到 `~/.agents/skills/travel-copilot/` |
| WorkBuddy | 技能 → 添加技能 → 导入本地技能包 |
| 通用 Agent Skills | 将完整目录交给客户端的 Skill 安装/导入入口 |

不要只复制 `SKILL.md`，脚本、模板和 references 也必须保留。[详细安装、Windows 和故障排查](docs/installation.md)。

## 这样开始

```text
请使用 Travel Copilot。三个人去成都四天，节奏轻松，熊猫基地必须去。
先帮我补全计划、检查交通和准备事项，等我确认行程后再推荐视觉方向并生成 HTML。
```

```text
这是我已经做好的旅行 PDF。请保留已订的航班和酒店，先检查缺漏，
有不确定的地方标出来。确认定稿后，生成可以发给同行朋友的互动行程和个人日历提醒。
```

## 手动生成

在仓库根目录运行；Windows 可将 `python3` 换为 `py -3`：

```bash
python3 scripts/validate_trip.py examples/demo-trip.json
python3 scripts/package_trip.py examples/demo-trip.json --out-dir output/demo
```

`output/demo/` 包含 HTML、通用 ICS、`trip.json` 和使用说明。`package_trip.py` 当前调用基础渲染器。

单独生成：

```bash
python3 scripts/build_html.py examples/demo-trip.json -o output/trip.html
python3 scripts/build_ics.py examples/demo-trip.json --traveler traveler-a -o output/my-reminders.ics
```

先创建 `output/`（上面的打包命令会创建它）。更多内容见[架构与命令](docs/architecture.md)。

## 分享与提醒

把 HTML 发给同行朋友，每个人选择身份后导出自己的 ICS，再导入日历并检查时间、时区和通知设置。HTML 本身不提供关页后的后台推送或电话提醒。行程变更后，旧日历不会自动同步，需清理旧版本并重新导入，避免重复提醒。

文字和内嵌行程可离线查看；地图、远程照片与外部导航依赖网络。本地状态依赖浏览器存储，文件移动、浏览器更换或清理数据可能导致状态丢失，同行人之间不会自动同步。

## 项目结构

```text
travel-copilot/
├── SKILL.md
├── README.md / LICENSE / NOTICE.md
├── CONTRIBUTING.md / CHANGELOG.md
├── scripts/                 # 原有校验器、HTML/ICS 渲染器与打包器
├── references/              # 行程、审查、视觉导演与跨平台规范
├── assets/                  # 主题配置
├── examples/                # 已脱敏的输入、HTML、ICS
└── docs/
    ├── installation.md / demo.md / architecture.md
    ├── known-limitations.md / license-audit.md / release-checklist.md
    ├── screenshots/         # 截图说明与归属记录
    └── releases/v1.1.0.md
```

## 开源与致谢

本项目代码和文档使用 [MIT License](LICENSE)。第三方库、地图数据、照片各自保留原许可，不因本项目采用 MIT 而改为 MIT。完整清单见 [NOTICE](NOTICE.md) 与[素材审核](docs/license-audit.md)。

感谢 [travel-plan-viz](https://github.com/zexuanw958-svg/travel-plan-viz) 和 [EasyItinerary](https://github.com/Dobidop/easyItinerary) 的设计启发。

欢迎提交问题、跨平台安装反馈、无个人信息的示例与改进 PR。先读 [CONTRIBUTING.md](CONTRIBUTING.md)。
