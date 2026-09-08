# NOTICE / 第三方与致谢

## 项目本身

Travel Copilot 的代码与文档采用 [MIT](LICENSE)，沿用原包版权声明：Copyright (c) 2026 Travel Copilot contributors。

以下资源不因本项目使用 MIT 而改变原许可证。

## 运行时地图

| 资源 | 使用方式 | 许可 / 来源 |
| --- | --- | --- |
| Leaflet 1.9.4 | HTML 运行时从 unpkg 加载 JS/CSS，仓库未内置库源码 | [BSD-2-Clause 原文](https://raw.githubusercontent.com/Leaflet/Leaflet/v1.9.4/LICENSE)，Copyright 2010–2023 Volodymyr Agafonkin、2010–2011 CloudMade |
| OpenStreetMap 数据 | 运行时显示 OSM 地图瓦片 | © OpenStreetMap contributors；[ODbL 与署名说明](https://www.openstreetmap.org/copyright) |
| OSM 公共瓦片服务 | 联网地图请求 | [服务使用政策](https://operations.osmfoundation.org/policies/tiles/)，禁止批量预取/离线下载公共瓦片 |

地图控件应保留可见署名和版权链接。自定义打包 Leaflet 或改用其他地图服务时，需同时带上相应完整许可和服务署名。导航链接通往 Apple Maps、Google Maps 或高德；这些服务和商标不属于本项目，也不表示官方合作。

## 图像、字体与角色

本次公开 Demo 不包含第三方照片。模板使用系统字体回退，没有打包字体文件。HIKARI SVG 与纹理来自原包，原包描述为项目原创；本次保留该声明，但未独立证明完整创作历史。

原对话曾提及 Wikimedia Commons 图片；收到的压缩包没有这些照片、具体 File 页面、作者清单或对应 brief，无法逐项复核，也没有将它们纳入公开包。后续加入照片时按 [ATTRIBUTION 模板](docs/ATTRIBUTION-template.md)记录。官方旅游网站的图片也必须核实授权，不能仅因公开可见就自由复制。

## 设计启发

原包记载以下项目为设计启发：

- [zexuanw958-svg/travel-plan-viz](https://github.com/zexuanw958-svg/travel-plan-viz)（MIT）：单文件行程、结构化数据、地图与校验思路。
- [Dobidop/easyItinerary](https://github.com/Dobidop/easyItinerary)（MIT）：原生 Web 旅行交互理念。

原包声明 Travel Copilot 为重新实现；本次检查未做完整代码相似度或历史溯源审计，不将上述声明扩大为独立原创性保证。若后续引入上游实质代码，应保留其具体版权和完整许可。

核验范围及遗留事项见 [license-audit](docs/license-audit.md)。
