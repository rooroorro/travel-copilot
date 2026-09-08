# GitHub 发布手册

## 仓库信息

- Name：`travel-copilot`
- Visibility：Public
- Description：`Platform-agnostic Agent Skill for reviewed travel plans, interactive HTML itineraries and personal ICS reminders.`
- Website：等真实 Demo 部署成功后再填写。
- Topics：`agent-skills`, `travel`, `travel-planner`, `trip-planner`, `ai-agent`, `claude-code`, `codex`, `workbuddy`, `interactive-html`, `leaflet`, `icalendar`, `mobile-first`。

Topics 使用当前实际技术，不加入尚未使用的 MapLibre 等标签。

## 发布内容

README、LICENSE、NOTICE、CONTRIBUTING、CHANGELOG、安装指南、示例和 Release Notes 已随仓库提供。截图目录当前为规范结构，尚无实际截图。源代码与文档的验证结果见 [validation.md](validation.md)。

发布前审阅 `tools/release-files.txt`，其中列出的才是公开包内容。新增文件需手动加入清单，避免把私人输入或调试产物一起打包。

```bash
python3 tools/build_release.py --out-dir dist
```

生成 `dist/travel-copilot-v1.1.0.zip` 和 `dist/SHA256SUMS.txt`。ZIP 根目录为 `travel-copilot/`。不包含 `.git`、`output`、缓存或源 ZIP。已生成内容相同、运行环境相同时，重复打包应得到相同校验值。

## 通过 GitHub CLI 发布

以下需要已安装 Git 与 [GitHub CLI](https://cli.github.com/)、完成 `gh auth login`，并有目标仓库权限。在仓库根目录执行。本项目仓库为 `rooroorro/travel-copilot`；先把 Git 身份占位符替换为实际值；不要在聊天或仓库中粘贴 Token。

若本地尚未初始化 Git，执行 `git init -b main`。本地整理阶段已初始化 `main`。若代码由网页上传，建议克隆远程仓库后再继续开发，避免独立的初始提交历史。

```bash
git config user.name '你的提交署名'
git config user.email '你选择公开的邮箱或 GitHub noreply 邮箱'
git add .
git diff --cached --stat
git commit -m "Prepare Travel Copilot v1.1.0 open-source release"
```

先检查目标仓库是否已存在：

```bash
gh repo view rooroorro/travel-copilot
```

仅在目标尚不存在时创建并推送：

```bash
gh repo create rooroorro/travel-copilot --public --source . --remote origin --push --description "Platform-agnostic Agent Skill for reviewed travel plans, interactive HTML itineraries and personal ICS reminders."
```

如仓库已存在，先读取远程内容并检查分支关系，不能直接覆盖或强推。已有 `origin` 时也应检查它指向哪里。

```bash
gh repo edit rooroorro/travel-copilot --add-topic agent-skills,travel,travel-planner,trip-planner,ai-agent,claude-code,codex,workbuddy,interactive-html,leaflet,icalendar,mobile-first
```

确认推送的是最终文件，重新打包，创建同一提交的版本标签，再准备 Draft Release：

```bash
python3 tools/build_release.py --out-dir dist
git tag -a v1.1.0 -m "Travel Copilot v1.1.0"
git push origin v1.1.0
gh release create v1.1.0 dist/travel-copilot-v1.1.0.zip dist/SHA256SUMS.txt --repo rooroorro/travel-copilot --verify-tag --draft --title "Travel Copilot v1.1.0" --notes-file docs/releases/v1.1.0.md
```

若同名 tag / Release 已存在，先检查内容，不删除或强制替换已发布版本。核对 Draft 的附件、说明和标签后，可以发布：

```bash
gh release edit v1.1.0 --repo rooroorro/travel-copilot --draft=false
gh release view v1.1.0 --repo rooroorro/travel-copilot
```

GitHub CLI 官方参考：[创建仓库](https://cli.github.com/manual/gh_repo_create)、[仓库 Topics](https://cli.github.com/manual/gh_repo_edit)、[创建 Release](https://cli.github.com/manual/gh_release_create)。

## 不使用命令行

在 GitHub 创建 Public 空仓库（不勾选自动添加 README/License），通过网页上传这里整理好的文件和文件夹内容，保留根目录结构。随后在 Releases 新建 `v1.1.0`，粘贴本地 Release Notes，并附上 ZIP 与 SHA256SUMS。不要把 ZIP 当作仓库唯一文件。

发布后检查 README 链接和 Demo 下载，用干净目录解压附件运行基础生成命令。成功后记录真实仓库 URL、Release URL 与 tag commit；本文件本身不证明远程已发布。
