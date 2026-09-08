# v1.1.0 验证记录

日期：2026-09-08。执行环境：macOS、Python 3.12.3、Node.js v23.11.0。

## 已执行

- Demo JSON 校验：0 errors、0 warnings。
- 从脱敏 JSON 重新生成基础 HTML 与 ICS；完整旅行包生成成功。
- 检查 HTML 中 `trip-data` 与源 JSON 一致、公开 Demo 与渲染器输出一致。
- 检查错误坐标及重复事件 ID 被校验器拒绝。
- 检查 ICS 的 UTC 转换、旅行 TZID、CRLF、事件/提醒块闭合及同行人筛选；当前 Demo 默认导出 6 个 VEVENT。
- 两套模板的内联 JavaScript 通过 Node 语法检查。
- Python 源码通过 Python 3.9 语法级检查；这不等于在 Python 3.9 运行时实测。
- 本地 Markdown 文件链接检查，地图版权链接检查。
- ZIP 完整性检查、重复构建校验值一致、临时目录解压后独立运行检查通过；包内没有 `.git`、输出文件或缓存。
- 原包对照：`SKILL.md`、references、主题配置与主要业务脚本保持不变；变更为发布文档、匿名 Demo、OSM 署名链接和 ICS 写入兼容修正。

复现：

```bash
python3 tools/check_release.py
python3 tools/build_release.py --out-dir dist
```

Node 仅用于可选的 JavaScript 语法检查，不是运行 Skill 的依赖。检查脚本如找不到 Node，会明确标为跳过。

## 本地整理阶段未覆盖的验收

- 手机/桌面浏览器的完整交互与视觉截图。
- 地图瓦片在线可用性和真实断网操作。
- iOS / Android / Google Calendar 的 ICS 导入与实际通知。
- Claude Code / Codex / WorkBuddy 逐个平台的安装实测。
- 实验性视觉模板的跨目的地正确性；限制已记录。
- GitHub 远程仓库、推送、Draft Release 和在线 Demo 的实际发布。

这些项目未被上述静态/生成检查覆盖，不应写成“全平台测试通过”。
