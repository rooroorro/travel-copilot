# Changelog

软件版本与用户行程的 `meta.version` 独立。此记录基于收到的 v1.1.0 压缩包；没有更早版本的可核验变更记录。

## 1.1.0 — 开源发布准备

### 原包已有

- 平台无关的旅行整理、审查、讨论和定稿工作流。
- `trip.json`、基础校验器、通用 HTML、ICS 与旅行包生成脚本。
- Visual Director 工作流、brief 注入渲染器及实验性日本视觉模板。

### 本次开源整理

- 完善 README、四类宿主安装指南、架构、贡献说明、Demo 和截图目录规范。
- 保留 MIT 许可证，扩充第三方 NOTICE、来源审核和素材归属模板。
- 补充地图的 OpenStreetMap 版权页面链接。
- ICS 文件写入改用 Python 3.9 支持的方式，保持输出不变。
- Demo 同行人改为匿名样例，并说明非真实预订；重新生成 HTML / ICS。
- 发布包排除 `__pycache__`、个人行程输出和开发缓存，提供 SHA-256 校验。
- 明确视觉模板、日历和平台验证边界。

### 发布状态

本地文件准备不等于已发布 GitHub Release。实际发布记录以仓库的 Releases 页面为准。[v1.1.0 Release Notes](docs/releases/v1.1.0.md)。
