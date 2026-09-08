# 参与贡献

欢迎问题报告、文档改进、跨平台安装反馈、脱敏示例与代码 PR。请使用中文或英文清楚描述问题。

## 报告问题

提供 Skill 版本、客户端/系统/浏览器/Python 版本、复现步骤、期望与实际表现，以及最小脱敏 JSON。不要提交真实票据、预订码、证件、手机号或密钥。只提供截图而没有数据时，也请说明输入字段。

## 开发约定

- 保留平台无关的 `trip.json → Python 渲染器 → HTML / ICS` 分工；宿主适配放在文档或独立薄适配层。
- 不把某个模型 API、付费服务或服务端作为基础依赖。
- 不改变用户确认后才定稿的工作流。
- 数据格式变更同时更新 `references/trip-schema.md`，说明旧数据迁移方式。
- 使用原生 HTML/CSS/JS 与 Python 标准库；引入新依赖前先说明必要性与许可。
- 新示例必须去除个人信息，所有第三方素材必须补来源、作者、许可证与修改说明。

## 提交 PR

Fork 后创建功能分支；在 PR 说明问题、改动后行为和验证结果。聚焦一个主题，避免混入无关格式化。修改文档时检查本地链接；修改功能时补覆盖实际风险的测试。

最小验证（仓库根目录）：

```bash
python3 scripts/validate_trip.py examples/demo-trip.json
python3 scripts/package_trip.py examples/demo-trip.json --out-dir output/review
python3 scripts/build_ics.py examples/demo-trip.json --traveler traveler-a -o output/review/traveler-a.ics
```

涉及界面的改动应在桌面和手机宽度检查切日、完成状态、清单、提醒选择、网络失败及减少动态效果设置。涉及 ICS 的改动应实际导入目标日历，核对时区和通知设置；在 PR 中说明测过哪些客户端。

## 贡献许可

提交贡献意味着你有权提供这些内容，并同意以本项目 MIT 许可证授权自己的贡献。第三方内容仍按原许可保留声明；请不要将来源不明的图片或代码标为原创。
