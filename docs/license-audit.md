# 许可与素材审核记录

审核日期：2026-09-08。对象：用户提供的 `travel-copilot-v1.1.0.zip` 及本次整理输出。

## 审核结果

| 项目 | 发现与处理 |
| --- | --- |
| MIT LICENSE | 原包已包含标准 MIT 文本，保留原有 2026 contributors 版权声明 |
| Python 依赖 | 渲染/校验/打包脚本仅使用标准库，无第三方 Python 包 |
| Leaflet | 实际 CDN 引用 1.9.4，官方 LICENSE 为 BSD-2-Clause，已在 NOTICE 记录 |
| OSM | 原地图只有纯文字署名；补上 copyright 链接并保留 contributors |
| 第三方照片 | ZIP 中无照片文件，Demo heroImage 为空；没有可核验的日本图片清单 |
| 字体 | CSS 字体家族为本机回退名称，未发现字体文件或字体 CDN |
| HIKARI / 纹理 | 原包内 SVG 与内联纹理，沿用原包的原创声明；未独立核验创作历史 |
| 致谢项目 | 两个上游仓库公开标示 MIT；记为设计启发，不声称通过代码来源审计 |
| 公开数据 | Demo 人名和 ID 改为旅人 A/B/C，说明时间地点为示例；未发现票据、证件或 API 密钥 |
| 缓存 | ZIP 中 Python `__pycache__` 未收入公开仓库 |

## 一手来源

- [Leaflet 1.9.4 LICENSE](https://raw.githubusercontent.com/Leaflet/Leaflet/v1.9.4/LICENSE)
- [OpenStreetMap copyright](https://www.openstreetmap.org/copyright)
- [OSM 瓦片服务政策](https://operations.osmfoundation.org/policies/tiles/)
- [travel-plan-viz](https://github.com/zexuanw958-svg/travel-plan-viz)
- [EasyItinerary](https://github.com/Dobidop/easyItinerary)

## 边界

这是本包的文件/引用检查和官方来源核对，没有取得缺失照片的作者与许可证据，也没有证明每行代码的独立创作历史。因此只能报告上述具体结果，不能称“全部第三方素材已完全清权”。公开包不纳入缺失素材，未来新增内容按 `ATTRIBUTION-template.md` 补证据。
