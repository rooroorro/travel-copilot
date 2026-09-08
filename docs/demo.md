# Demo 展示指南

## 包含的示例

- [demo-trip.json](../examples/demo-trip.json)：东京 3 日示例，旅人 A/B/C，8 个活动、2 项清单、2 条显式提醒。
- [demo-trip.html](../examples/demo-trip.html)：基础渲染器生成的互动页面。
- [demo-reminders.ics](../examples/demo-reminders.ics)：默认 P0/P1 范围的通用提醒样例。

示例日期、地点、时间仅供交互演示，未核验交通和营业信息，不代表预订或真实出行。HTML 页眉中的 `v1.0` 为行程数据版本；Skill 软件版本为 `v1.1.0`。

## 本地打开

下载仓库后双击 HTML，并选择现代浏览器打开。GitHub 的文件页不会直接运行 HTML。如果文件预览阻止脚本，可在仓库目录运行：

```bash
python3 -m http.server 8000 --bind 127.0.0.1
```

然后打开 `http://127.0.0.1:8000/examples/demo-trip.html`。这只用于本机预览，结束时在终端按 Ctrl+C。

## 一分钟演示顺序

1. 浏览首页，说明“上传材料 → 审查 → 确认 → 互动行程”。
2. 切到 Day 2，滚动浅草、秋叶原、涩谷时间轴；联网可观察地图跟随。
3. 标记一个活动完成、勾选准备清单，刷新检查本机状态。
4. 打开提醒设置，选择旅人 A，勾选优先级，导出 ICS。
5. 提醒观众：日历需自行导入；导出不会自动创建系统日历事件。

不在示例旅行日期内时，Now/Next 显示“当前不在行程日期内”是预期行为。不要为截图伪造实时行程状态。

## 截图与 GIF

使用 [screenshots/README.md](screenshots/README.md) 的画面列表和归属要求。当前仓库先提供目录和截图规范；没有将聊天中的图片链接或未审查的真实行程作为截图发布。

## 在线展示（可选）

仓库公开后，可在 GitHub Pages 设置中选择 `main` 的根目录发布静态内容，Demo 路径为 `/travel-copilot/examples/demo-trip.html`。仅在 Pages 已显示成功部署后，才将实际 URL 加入 README 与仓库 Website。此处是部署说明，不代表 Demo 已上线。

公开前确认仓库只包含示例。不要将真实预订码、证件或同行人资料放入公开站点。
