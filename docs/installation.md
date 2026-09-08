# 安装 Travel Copilot

安装的是整个 `travel-copilot` 文件夹。其根目录应直接包含 `SKILL.md`、`scripts/`、`references/`、`assets/`；不要多嵌套一层同名文件夹。

## 下载

从项目 Release 下载 `travel-copilot-v1.1.0.zip` 并解压；也可使用 GitHub 的 Code → Download ZIP。后者通常解压为 `travel-copilot-main`，安装时将目录名改为 `travel-copilot`。本说明不假定仓库已上线。

## Claude Code

个人安装位置：`~/.claude/skills/travel-copilot/`。仅当前项目使用则放入 `<项目>/.claude/skills/travel-copilot/`。

macOS / Linux 可在源仓库根目录外建立链接，下面路径必须换为自己实际的绝对路径：

```bash
mkdir -p ~/.claude/skills
ln -s /absolute/path/to/travel-copilot ~/.claude/skills/travel-copilot
```

如果目标已存在，先检查旧版本并备份，不要强制覆盖。也可以直接复制整个文件夹。安装后输入 `/travel-copilot` 或说明“请使用 Travel Copilot 帮我规划旅行”。此处针对 Claude Code；Claude 网页版的自定义技能入口与权限取决于产品版本。

来源：[Claude Code 官方 Skills 文档](https://code.claude.com/docs/en/skills)。

## Codex

个人安装位置：`~/.agents/skills/travel-copilot/`；项目安装位置：`<项目>/.agents/skills/travel-copilot/`。

```bash
mkdir -p ~/.agents/skills
ln -s /absolute/path/to/travel-copilot ~/.agents/skills/travel-copilot
```

Codex CLI / IDE 可以通过 `/skills` 查看或使用 `$travel-copilot` 指定技能；桌面入口随版本变化，也可直接说明技能名。若未出现，重新打开会话/客户端。原包 README 使用 `~/.codex/skills` 示例；本指南采用当前官方文档中的 `.agents/skills` 路径。不要在多个目录安装重复副本。

来源：[OpenAI 官方 Skills 文档](https://developers.openai.com/codex/skills/)。这是本地 Skill 安装，不表示项目已上架插件市场。

## WorkBuddy

进入 **技能 → 添加技能 → 导入本地技能包**，选择下载的包或按客户端提示选择解压后的目录。安装后在已安装技能中确认 `travel-copilot` 已启用，在对话中请求使用它。若导入提示结构不正确，检查 `SKILL.md` 所在层级，按当前客户端的导入格式重新选择文件夹。

不推测隐藏安装路径，也不要求更改数据结构。脚本执行、文件读取和联网权限由 WorkBuddy 所在环境决定。

来源：[WorkBuddy 官方技能说明](https://www.codebuddy.cn/docs/workbuddy/From-Beginner-to-Expert-Guide/Function-Description/Skills-Market)。此流程依官方文档整理，未在该客户端实机验证本包。

## Windows

无需创建符号链接。将整个目录复制到用户目录下对应的 `.claude\skills\travel-copilot` 或 `.agents\skills\travel-copilot`。在 PowerShell 输入 `$HOME` 可确认用户目录。命令中的 `python3` 换成 `py -3`；用 `py -3 --version` 检查 Python。

## 通用 Agent Skills / 仅聊天环境

遵循 [Agent Skills 目录标准](https://agentskills.io/specification)，通过宿主的导入入口安装整个目录。标准统一文件格式，不保证每个宿主具备文件解析、浏览器或执行权限。

| 环境能力 | 使用方式 |
| --- | --- |
| 能读文件、运行 Python | 读取 Skill，按既有脚本生成行程包 |
| 能读文件但不能执行 | 产出 `trip.json`，转到具备 Python 的环境运行 |
| 仅文本聊天 | 粘贴行程文本与 Skill 指令；产出结构化数据，不声称已生成文件 |

## 验证安装

要求 Agent 报出它读取的 `SKILL.md` 路径，然后先审查一个草稿行程。未确认行程前不应直接输出最终版本。需要检查脚本时，在仓库目录运行：

```bash
python3 scripts/validate_trip.py examples/demo-trip.json
python3 scripts/package_trip.py examples/demo-trip.json --out-dir output/demo
```

若显示找不到脚本，确认复制了整个目录，且执行时位于仓库根目录。若找不到 Python，安装 Python 3.9 或更新版本；脚本不依赖 pip 包。上述官网入口核验于 2026-09-08，客户端 UI 可能变化。
