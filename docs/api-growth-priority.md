# ApiZero 接口增长优先级

生成时间：`2026-07-06T07:53:50+00:00`

这份表把全量接口按“现在适不适合拿出去拉新人”分层。站内已有调用量的接口优先看真实调用和错误率；没有调用量的接口先收录，不急着写大量内容。

## 执行规则

- `A-core`：马上主推，优先写 GitHub demo、CSDN/掘金教程、Postman/Apifox 示例。
- `A-verify`：有需求，但发文前必须用真实参数跑通 3-5 组示例。
- `B-support`：做补充内容，适合平台分发和长尾搜索。
- `C-caution`：只做排错、合规、边界说明，不作为拉新入口。
- `D-inventory`：先进入接口库，暂不投入内容产能。

## 当前应推接口

| 层级 | slug | 接口 | 已知调用 | 已知错误率 | 动作 | 推广角度 | 链接 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| A-core | weather | 彩云天气 | 17379 | 0.36% | 主推 | 免费天气 API；城市名直接查；适合小程序、网站天气模块、日报脚本。 | [demo/docs](https://apizero.cn/aidocs/weather) |
| A-core | qq | QQ 信息 | 577 | 3.29% | 主推 | QQ 头像昵称 API；适合头像展示、轻量用户资料补全、网页小工具。 | [demo/docs](https://apizero.cn/aidocs/qq) |
| A-core | moji-weather | 墨迹天气 | 441 | 3.17% | 主推 | 墨迹天气；和 weather 合并做天气专题，对比字段丰富度和使用场景。 | [demo/docs](https://apizero.cn/aidocs/moji-weather) |
| A-core | barcode-lookup | 商品条码查询-免费版 | 164 |  | 主推 | 免费商品条码查询；适合库存录入、电商资料补全、扫码工具。 | [demo/docs](https://apizero.cn/aidocs/barcode-lookup) |
| A-verify | barcode-gs1 | 商品条码查询PRO | 1805 | 14.13% | 验证后主推 | PRO 商品条码查询；发文前先用真实条码验证，降低新用户复制失败率。 | [demo/docs](https://apizero.cn/aidocs/barcode-gs1) |
| B-support | hot-baidu | 百度热搜榜 |  |  | 补充推广 | 百度热搜 API；适合公众号、AI 写作工具、热点选题池。 | [demo/docs](https://apizero.cn/aidocs/hot-baidu) |
| B-support | movie-box | 实时电影票房 |  |  | 补充推广 | 实时电影票房 API；适合影视数据看板和小项目教程。 | [demo/docs](https://apizero.cn/aidocs/movie-box) |
| B-support | whois | Whois 域名查询 |  |  | 补充推广 | Whois 域名查询；适合站长工具、域名监控、开发者脚本。 | [demo/docs](https://apizero.cn/aidocs/whois) |
| B-support | fund | 基金估值跟踪 |  |  | 补充推广 | 基金估值 API；适合 Python 自用脚本、看板、投资工具教程。 | [demo/docs](https://apizero.cn/aidocs/fund) |
| B-support | content-extract | 网页正文提取 |  |  | 补充推广 | 网页正文提取；适合 RAG、AI 摘要、内容采集前清洗。 | [demo/docs](https://apizero.cn/aidocs/content-extract) |
| B-support | bus-realtime | 实时公交到站 |  |  | 补充推广 | 实时公交 API；适合城市出行小程序、通勤提醒工具。 | [demo/docs](https://apizero.cn/aidocs/bus-realtime) |
| B-support | webmeta | 网页元数据提取 |  |  | 补充推广 | 网页 Meta 信息提取；适合链接预览、采集前预处理、站点分析。 | [demo/docs](https://apizero.cn/aidocs/webmeta) |
| B-support | ssl | SSL 证书检测 |  |  | 补充推广 | SSL 证书查询；适合站长工具、证书到期提醒。 | [demo/docs](https://apizero.cn/aidocs/ssl) |
| B-support | dns-lookup | DNS 查询 |  |  | 补充推广 | DNS 查询 API；适合开发者工具、域名诊断、运维脚本。 | [demo/docs](https://apizero.cn/aidocs/dns-lookup) |
| C-caution | video-parse | 全平台视频元数据解析服务 | 835 | 42.99% | 只做排错/合规指南 | 错误率高，暂不作为拉新入口；只讲合法使用、常见错误和可测试输入。 | [demo/docs](https://apizero.cn/aidocs/video-parse) |

## 下一步内容矩阵

1. 天气专题：`weather` + `moji-weather`，主打“免费天气 API / Python / Node.js / 小程序后端”。
2. 条码专题：`barcode-lookup` + `barcode-gs1`，主打“商品条码查询 API / 扫码录入 / 电商资料补全”。
3. 开发者工具专题：`whois`、`dns-lookup`、`ssl`、`webmeta`、`content-extract`，适合 GitHub Topic、掘金、V2EX、站长群。
4. 内容工具专题：`hot-baidu`、`movie-box`、`fund`，适合“AI 选题池 / 数据看板 / Python 小项目”。
5. 视频解析：只保留合法使用和错误排查，不在标题里承诺稳定生产可用。
