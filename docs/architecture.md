# 架构与执行入口

## 不变的跨平台边界

Agent 负责读取材料、调研、审查和与用户确认。`trip.json` 保存行程事实；`creative_brief.json` 保存视觉选择；Python 脚本生成文件。所有宿主共用这些文件和脚本，不增加服务端、账号、数据库或专属模型 API。

```text
用户输入 → Agent 整理 / 审查 / 讨论 → 用户定稿 → trip.json
                                             ├─ build_html.py → 通用 HTML
                                             ├─ build_ics.py → ICS
                                             └─ + creative_brief.json
                                                → build_visual_html.py
                                                → 实验性视觉 HTML
```

## 脚本

| 文件 | 输入 | 输出 / 范围 |
| --- | --- | --- |
| `scripts/validate_trip.py` | trip JSON | 基本字段、ID、坐标等检查；不是完整旅行可行性验证 |
| `scripts/build_html.py` | trip JSON | 基础互动 HTML，五个主题 |
| `scripts/build_visual_html.py` | trip JSON + brief | 将数据注入 `visual_template.html`；日本主题实验模板 |
| `scripts/build_ics.py` | trip JSON | ICS；`--traveler` 过滤同行人，默认 P0/P1 |
| `scripts/package_trip.py` | trip JSON | 先校验，再输出基础 HTML、ICS、JSON、中文说明 |

通用命令见 README。视觉渲染仅在已有与模板匹配的 brief 时使用：

```bash
python3 scripts/build_visual_html.py trip.json creative_brief.json -o trip-visual.html
```

brief 至少应有非空 `phases`，每项包含 `id`、`label`、`days`、`palette` 和 `heroImage`；还使用 `name`、`tagline`、`visualStory`、`assets`。这是当前模板读取的字段，不是已验证的通用 brief schema。不要将任意设计描述当作可直接执行的布局指令。

数据格式详见 [trip-schema](../references/trip-schema.md)，平台能力降级详见 [platform-compatibility](../references/platform-compatibility.md)。

## 分享与网络

HTML 内嵌 `trip-data`，基础浏览器交互为原生 JavaScript。地图通过 CDN 加载 Leaflet 1.9.4，并请求 OpenStreetMap 瓦片。导航链接交给外部地图服务。没有应用服务端，不等于没有网络请求：CDN、地图和照片服务仍可收到常规请求信息。

核心离线使用不需要打包地图瓦片；不得通过批量下载 OSM 公共瓦片实现离线地图。当前模板中的照片 URL 如存在仍需联网。完整离线图片打包尚未实现。

## 提醒

ICS 是导出快照，不是订阅。提醒可用性取决于接收日历对时区、VALARM 和通知权限的支持。浏览器侧可以勾选 P2；当前 Python 导出器不会为普通 P2 行程事件生成提醒，即使 `--priorities` 包含 P2。见[已知限制](known-limitations.md)。
