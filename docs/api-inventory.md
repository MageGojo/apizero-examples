# ApiZero 接口导出清单

生成时间：`2026-10-16T02:34:40+00:00`  
接口总数：`141`

数据源：

- Sitemap：https://apizero.cn/sitemap.xml
- 单接口 Markdown：https://apizero.cn/aidocs/{slug}/raw.md
- LLM 索引：https://apizero.cn/llms.txt

## 分类统计

| 分类 | 接口数 |
| --- | --- |
| AI 能力 | 6 |
| 内容娱乐 | 21 |
| 地理位置 | 4 |
| 开发工具 | 24 |
| 招中标 | 22 |
| 文档识别 | 14 |
| 生活服务 | 34 |
| 身份核验 | 10 |
| 金融数据 | 6 |

## 增长分层统计

| 增长层级 | 接口数 |
| --- | --- |
| A-core | 4 |
| A-verify | 1 |
| B-support | 15 |
| C-caution | 3 |
| D-inventory | 118 |

## 全量接口清单

免费额度列格式：`登录用户/匿名用户`，单位是每日次数。

| # | slug | 名称 | 分类 | 方法 | QPS | 免费额度 | 增长层级 | 文档 | 市场页 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | bus-realtime | 实时公交到站 | 生活服务 | POST | QPS 10 | 1000/500 | B-support | [文档](https://apizero.cn/aidocs/bus-realtime) | [市场](https://apizero.cn/marketplace/bus-realtime) |
| 2 | weather | 彩云天气 | 生活服务 | GET | QPS 3 | 2000/100 | A-core | [文档](https://apizero.cn/aidocs/weather) | [市场](https://apizero.cn/marketplace/weather) |
| 3 | barcode-gs1 | 商品条码查询PRO | 生活服务 | GET | 40 req/s | 5/2 | A-verify | [文档](https://apizero.cn/aidocs/barcode-gs1) | [市场](https://apizero.cn/marketplace/barcode-gs1) |
| 4 | gold | 黄金价格查询 | 金融数据 | GET | 3 req/s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/gold) | [市场](https://apizero.cn/marketplace/gold) |
| 5 | video-parse | 全平台视频元数据解析服务 | 内容娱乐 | GET | QPS 20 | 5/3 | C-caution | [文档](https://apizero.cn/aidocs/video-parse) | [市场](https://apizero.cn/marketplace/video-parse) |
| 6 | holiday | 中国法定节假日 | 生活服务 | GET | 3 req/s | 10000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/holiday) | [市场](https://apizero.cn/marketplace/holiday) |
| 7 | stock-trend | A股实时行情 | 金融数据 | POST | 3 req/s | 50/5 | B-support | [文档](https://apizero.cn/aidocs/stock-trend) | [市场](https://apizero.cn/marketplace/stock-trend) |
| 8 | company-search | 企业工商信息查询 | 身份核验 | GET | QPS 2 | 10/5 | D-inventory | [文档](https://apizero.cn/aidocs/company-search) | [市场](https://apizero.cn/marketplace/company-search) |
| 9 | movie-box | 实时电影票房 | 生活服务 | GET | 3 req/s | 20000/1000 | B-support | [文档](https://apizero.cn/aidocs/movie-box) | [市场](https://apizero.cn/marketplace/movie-box) |
| 10 | oil-price | 全国油价 | 生活服务 | POST | 3 req/s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/oil-price) | [市场](https://apizero.cn/marketplace/oil-price) |
| 11 | barcode-lookup | 商品条码查询-免费版 | 生活服务 | GET | 2 req/s | 200/20 | A-core | [文档](https://apizero.cn/aidocs/barcode-lookup) | [市场](https://apizero.cn/marketplace/barcode-lookup) |
| 12 | douyin-user | 抖音用户公开信息 | 内容娱乐 | GET | 3 req/s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/douyin-user) | [市场](https://apizero.cn/marketplace/douyin-user) |
| 13 | visits-counter | 访问量计数器 | 开发工具 | GET | 3 req/s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/visits-counter) | [市场](https://apizero.cn/marketplace/visits-counter) |
| 14 | moji-weather | 天气查询 | 生活服务 | GET | QPS 3 | 3000/1000 | A-core | [文档](https://apizero.cn/aidocs/moji-weather) | [市场](https://apizero.cn/marketplace/moji-weather) |
| 15 | express | 快递物流查询-免费版 | 生活服务 | GET | 1 req/s | 10/3 | D-inventory | [文档](https://apizero.cn/aidocs/express) | [市场](https://apizero.cn/marketplace/express) |
| 16 | oil-price-forecast | 今日油价 | 生活服务 | GET | 3 req/s | 10000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/oil-price-forecast) | [市场](https://apizero.cn/marketplace/oil-price-forecast) |
| 17 | qq | QQ 信息 | 生活服务 | GET | 3 req/s | 30000/5000 | A-core | [文档](https://apizero.cn/aidocs/qq) | [市场](https://apizero.cn/marketplace/qq) |
| 18 | exchange-rate | 实时汇率查询 | 金融数据 | GET | 3 req/s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/exchange-rate) | [市场](https://apizero.cn/marketplace/exchange-rate) |
| 19 | hot-baidu | 百度热搜榜 | 生活服务 | GET | 3 req/s | 10000/1000 | B-support | [文档](https://apizero.cn/aidocs/hot-baidu) | [市场](https://apizero.cn/marketplace/hot-baidu) |
| 20 | wzry | 王者战力查询 | 生活服务 | GET | QPS 3 | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/wzry) | [市场](https://apizero.cn/marketplace/wzry) |
| 21 | typhoon | 台风实时路径 | 生活服务 | POST | 3 req/s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/typhoon) | [市场](https://apizero.cn/marketplace/typhoon) |
| 22 | content-extract | 网页正文提取 | 开发工具 | GET | 3 req/s | 10000/5000 | B-support | [文档](https://apizero.cn/aidocs/content-extract) | [市场](https://apizero.cn/marketplace/content-extract) |
| 23 | wallpaper | 随机壁纸 | 生活服务 | GET | 3 req/s | 10000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/wallpaper) | [市场](https://apizero.cn/marketplace/wallpaper) |
| 24 | mobile | 手机号归属地 | 生活服务 | GET | 3 req/s | 30000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/mobile) | [市场](https://apizero.cn/marketplace/mobile) |
| 25 | douyin-works | 抖音用户作品 | 内容娱乐 | POST | 8 req/s | 10/2 | C-caution | [文档](https://apizero.cn/aidocs/douyin-works) | [市场](https://apizero.cn/marketplace/douyin-works) |
| 26 | express-pro | 快递查询PRO | 生活服务 | GET | 10 req/s | / | B-support | [文档](https://apizero.cn/aidocs/express-pro) | [市场](https://apizero.cn/marketplace/express-pro) |
| 27 | jd-address | 京东地址解析（4 级） | 地理位置 | POST | 3 req/s | 1000/10 | D-inventory | [文档](https://apizero.cn/aidocs/jd-address) | [市场](https://apizero.cn/marketplace/jd-address) |
| 28 | icp | ICP 备案查询 | 开发工具 | GET | 20 req/s | 100/30 | D-inventory | [文档](https://apizero.cn/aidocs/icp) | [市场](https://apizero.cn/marketplace/icp) |
| 29 | ocr-text | OCR 文字识别 | 文档识别 | POST | 2 req/s | 300/50 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-text) | [市场](https://apizero.cn/marketplace/ocr-text) |
| 30 | 2fa | 2FA 动态验证码 | 开发工具 | POST | 3 req/s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/2fa) | [市场](https://apizero.cn/marketplace/2fa) |
| 31 | hot-search | 全网热搜聚合 | 内容娱乐 | POST | 3 req/s | 3000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/hot-search) | [市场](https://apizero.cn/marketplace/hot-search) |
| 32 | ip-pro | IP 地址查询（街道级） | 地理位置 | GET | 3 req/s | 30/5 | D-inventory | [文档](https://apizero.cn/aidocs/ip-pro) | [市场](https://apizero.cn/marketplace/ip-pro) |
| 33 | fund | 基金估值跟踪 | 金融数据 | GET | 3 req/s | 200/50 | B-support | [文档](https://apizero.cn/aidocs/fund) | [市场](https://apizero.cn/marketplace/fund) |
| 34 | douban-movie | 豆瓣电影信息 | 内容娱乐 | GET | QPS 3 | 1000/300 | D-inventory | [文档](https://apizero.cn/aidocs/douban-movie) | [市场](https://apizero.cn/marketplace/douban-movie) |
| 35 | whois | Whois 域名查询 | 开发工具 | GET | 3 req/s | 1000/300 | B-support | [文档](https://apizero.cn/aidocs/whois) | [市场](https://apizero.cn/marketplace/whois) |
| 36 | yiyan | 一言（简版） | 生活服务 | GET | 3 req/s | 500000/200000 | D-inventory | [文档](https://apizero.cn/aidocs/yiyan) | [市场](https://apizero.cn/marketplace/yiyan) |
| 37 | netease-comment | 网易云热门乐评 | 内容娱乐 | POST | 3 req/s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/netease-comment) | [市场](https://apizero.cn/marketplace/netease-comment) |
| 38 | hitokoto | 一言 · 经典语录 | 生活服务 | GET | 3 req/s | 500000/200000 | D-inventory | [文档](https://apizero.cn/aidocs/hitokoto) | [市场](https://apizero.cn/marketplace/hitokoto) |
| 39 | brain-teaser | 脑筋急转弯 | 生活服务 | GET | 3 req/s | 200000/10000 | D-inventory | [文档](https://apizero.cn/aidocs/brain-teaser) | [市场](https://apizero.cn/marketplace/brain-teaser) |
| 40 | tts | TTS 语音合成 | AI 能力 | POST | 3 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tts) | [市场](https://apizero.cn/marketplace/tts) |
| 41 | content-moderation | 内容审核 | 内容娱乐 | POST | 3 req/s | 500/100 | D-inventory | [文档](https://apizero.cn/aidocs/content-moderation) | [市场](https://apizero.cn/marketplace/content-moderation) |
| 42 | ocr-health-cert | 健康证识别 | 生活服务 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-health-cert) | [市场](https://apizero.cn/marketplace/ocr-health-cert) |
| 43 | wzry-battle | 王者荣耀战绩查询 | 内容娱乐 | POST | 2 req/s | 20/5 | D-inventory | [文档](https://apizero.cn/aidocs/wzry-battle) | [市场](https://apizero.cn/marketplace/wzry-battle) |
| 44 | baby-naming | 八字起名 | 生活服务 | POST | 2 req/s | 5000/3000 | D-inventory | [文档](https://apizero.cn/aidocs/baby-naming) | [市场](https://apizero.cn/marketplace/baby-naming) |
| 45 | company-profile | 企业档案深度查询 | 身份核验 | POST | 3 req/s | 3/1 | D-inventory | [文档](https://apizero.cn/aidocs/company-profile) | [市场](https://apizero.cn/marketplace/company-profile) |
| 46 | shici | 随机诗词 | 内容娱乐 | POST | 3 req/s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/shici) | [市场](https://apizero.cn/marketplace/shici) |
| 47 | crazy-thursday | 疯狂星期四文案 | 生活服务 | GET | 3 req/s | 20000/10000 | D-inventory | [文档](https://apizero.cn/aidocs/crazy-thursday) | [市场](https://apizero.cn/marketplace/crazy-thursday) |
| 48 | bank-card | 银行卡BIN查询 | 金融数据 | GET | 3 req/s | 10000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/bank-card) | [市场](https://apizero.cn/marketplace/bank-card) |
| 49 | tencent-weather | 腾讯天气 | 生活服务 | POST | 3 req/s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/tencent-weather) | [市场](https://apizero.cn/marketplace/tencent-weather) |
| 50 | wechat-archive | 微信文章转存 | 内容娱乐 | POST | 1 req/s | 1000/100 | D-inventory | [文档](https://apizero.cn/aidocs/wechat-archive) | [市场](https://apizero.cn/marketplace/wechat-archive) |
| 51 | riddle | 谜语大全 | 内容娱乐 | POST | 3 req/s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/riddle) | [市场](https://apizero.cn/marketplace/riddle) |
| 52 | image-enhance | AI 图片变清晰 | AI 能力 | POST | 1 req/s | 10/ | D-inventory | [文档](https://apizero.cn/aidocs/image-enhance) | [市场](https://apizero.cn/marketplace/image-enhance) |
| 53 | ai-chat | 大模型 | AI 能力 | POST | 0 req/s | / | B-support | [文档](https://apizero.cn/aidocs/ai-chat) | [市场](https://apizero.cn/marketplace/ai-chat) |
| 54 | earthquake | 全球地震速报 | 生活服务 | POST | 3 req/s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/earthquake) | [市场](https://apizero.cn/marketplace/earthquake) |
| 55 | translate | 文本翻译 | 内容娱乐 | GET | 3 req/s | 5000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/translate) | [市场](https://apizero.cn/marketplace/translate) |
| 56 | traffic-weather-alert | 限行天气联动 | 生活服务 | GET | 3 req/s | 10000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/traffic-weather-alert) | [市场](https://apizero.cn/marketplace/traffic-weather-alert) |
| 57 | mingyan | 名人名言 | 内容娱乐 | POST | 3 req/s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/mingyan) | [市场](https://apizero.cn/marketplace/mingyan) |
| 58 | air-history | 历史空气质量 | 生活服务 | POST | 3 req/s | 50/5 | D-inventory | [文档](https://apizero.cn/aidocs/air-history) | [市场](https://apizero.cn/marketplace/air-history) |
| 59 | soul-soup | 心灵毒鸡汤 | 内容娱乐 | POST | 3 req/s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/soul-soup) | [市场](https://apizero.cn/marketplace/soul-soup) |
| 60 | doubao-image | 豆包图片生成 | AI 能力 | POST | 2 req/s | 5/1 | D-inventory | [文档](https://apizero.cn/aidocs/doubao-image) | [市场](https://apizero.cn/marketplace/doubao-image) |
| 61 | douyin-search | 抖音视频搜索 | 内容娱乐 | POST | 8 req/s | 20/2 | C-caution | [文档](https://apizero.cn/aidocs/douyin-search) | [市场](https://apizero.cn/marketplace/douyin-search) |
| 62 | food-license | 食品经营许可证识别 | 文档识别 | POST | 2 req/s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/food-license) | [市场](https://apizero.cn/marketplace/food-license) |
| 63 | site-security | 网站安全综合评分 | 开发工具 | GET | 2 req/s | 3000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/site-security) | [市场](https://apizero.cn/marketplace/site-security) |
| 64 | football | 足球赛事 | 生活服务 | POST | 40 req/s | 20/5 | B-support | [文档](https://apizero.cn/aidocs/football) | [市场](https://apizero.cn/marketplace/football) |
| 65 | bencao | 本草纲目·中药查询 | 生活服务 | GET | 3 req/s | 10000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/bencao) | [市场](https://apizero.cn/marketplace/bencao) |
| 66 | ocr-idcard | 身份证识别 | 文档识别 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-idcard) | [市场](https://apizero.cn/marketplace/ocr-idcard) |
| 67 | ocr-text-box | OCR 文字坐标识别 | 文档识别 | POST | 2 req/s | 200/40 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-text-box) | [市场](https://apizero.cn/marketplace/ocr-text-box) |
| 68 | risk-score | 综合风控评分 | 身份核验 | POST | 2 req/s | 200/10 | D-inventory | [文档](https://apizero.cn/aidocs/risk-score) | [市场](https://apizero.cn/marketplace/risk-score) |
| 69 | ssl | SSL 证书检测 | 开发工具 | GET | 3 req/s | 10000/3000 | B-support | [文档](https://apizero.cn/aidocs/ssl) | [市场](https://apizero.cn/marketplace/ssl) |
| 70 | hash | 哈希加密计算 | 开发工具 | GET | 3 req/s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/hash) | [市场](https://apizero.cn/marketplace/hash) |
| 71 | email-check | 邮箱地址检测 | 身份核验 | GET | 3 req/s | 500/100 | D-inventory | [文档](https://apizero.cn/aidocs/email-check) | [市场](https://apizero.cn/marketplace/email-check) |
| 72 | drug-insert | 药品说明书查询 | 生活服务 | GET | 40 req/s | 5/2 | B-support | [文档](https://apizero.cn/aidocs/drug-insert) | [市场](https://apizero.cn/marketplace/drug-insert) |
| 73 | unshort | 短链还原 | 开发工具 | GET | 3 req/s | 2000/300 | D-inventory | [文档](https://apizero.cn/aidocs/unshort) | [市场](https://apizero.cn/marketplace/unshort) |
| 74 | address-parse | 中文地址解析 | 地理位置 | POST | 3 req/s | 1000/100 | D-inventory | [文档](https://apizero.cn/aidocs/address-parse) | [市场](https://apizero.cn/marketplace/address-parse) |
| 75 | business-license | 营业执照识别 | 生活服务 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/business-license) | [市场](https://apizero.cn/marketplace/business-license) |
| 76 | site-check | 网站测速诊断 | 开发工具 | GET | 2 req/s | 5000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/site-check) | [市场](https://apizero.cn/marketplace/site-check) |
| 77 | text-similarity | 文本相似度 | 开发工具 | POST | QPS 3 | 50000/10000 | D-inventory | [文档](https://apizero.cn/aidocs/text-similarity) | [市场](https://apizero.cn/marketplace/text-similarity) |
| 78 | image-nsfw | 图片鉴黄 | AI 能力 | POST | 2 req/s | 100/10 | D-inventory | [文档](https://apizero.cn/aidocs/image-nsfw) | [市场](https://apizero.cn/marketplace/image-nsfw) |
| 79 | bili-dynamic | B 站用户动态 | 内容娱乐 | GET | 3 req/s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/bili-dynamic) | [市场](https://apizero.cn/marketplace/bili-dynamic) |
| 80 | webmeta | 网页元数据提取 | 开发工具 | GET | 3 req/s | 10000/5000 | B-support | [文档](https://apizero.cn/aidocs/webmeta) | [市场](https://apizero.cn/marketplace/webmeta) |
| 81 | user-info | 账户信息查询 | 开发工具 | GET | 1 req/s | 720/ | D-inventory | [文档](https://apizero.cn/aidocs/user-info) | [市场](https://apizero.cn/marketplace/user-info) |
| 82 | dns-check | DNS 劫持检测 | 开发工具 | GET | 3 req/s | 2000/50 | D-inventory | [文档](https://apizero.cn/aidocs/dns-check) | [市场](https://apizero.cn/marketplace/dns-check) |
| 83 | idcard-region | 身份证归属地查询 | 身份核验 | GET | 3 req/s | 1000/300 | D-inventory | [文档](https://apizero.cn/aidocs/idcard-region) | [市场](https://apizero.cn/marketplace/idcard-region) |
| 84 | dns-query | DNS 记录查询 | 开发工具 | GET | 3 req/s | 500/100 | D-inventory | [文档](https://apizero.cn/aidocs/dns-query) | [市场](https://apizero.cn/marketplace/dns-query) |
| 85 | text-censor | 文本审核 | 内容娱乐 | POST | 3 req/s | 100/30 | D-inventory | [文档](https://apizero.cn/aidocs/text-censor) | [市场](https://apizero.cn/marketplace/text-censor) |
| 86 | nine-grid-cutter | 九宫格切图 | 开发工具 | POST | 2 req/s | 5000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/nine-grid-cutter) | [市场](https://apizero.cn/marketplace/nine-grid-cutter) |
| 87 | cdn-ips | CDN 优选 IP | 开发工具 | GET | 3 req/s | 2000/100 | D-inventory | [文档](https://apizero.cn/aidocs/cdn-ips) | [市场](https://apizero.cn/marketplace/cdn-ips) |
| 88 | invoice | 增值税发票识别 | 文档识别 | POST | 2 req/s | 300/50 | D-inventory | [文档](https://apizero.cn/aidocs/invoice) | [市场](https://apizero.cn/marketplace/invoice) |
| 89 | idcard-organ | 身份证签发机关查询 | 身份核验 | GET | 3 req/s | 1000/300 | D-inventory | [文档](https://apizero.cn/aidocs/idcard-organ) | [市场](https://apizero.cn/marketplace/idcard-organ) |
| 90 | idcard-2c | 身份证二要素核验 | 身份核验 | POST | 3 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/idcard-2c) | [市场](https://apizero.cn/marketplace/idcard-2c) |
| 91 | blood-type | 血型遗传查询 | 生活服务 | GET | 3 req/s | 20000/10000 | D-inventory | [文档](https://apizero.cn/aidocs/blood-type) | [市场](https://apizero.cn/marketplace/blood-type) |
| 92 | bodyfat | 体脂率与 BMI 计算 | 生活服务 | GET | 3 req/s | 200000/100000 | D-inventory | [文档](https://apizero.cn/aidocs/bodyfat) | [市场](https://apizero.cn/marketplace/bodyfat) |
| 93 | browser-fingerprint | 浏览器指纹风控 | 开发工具 | POST | 3 req/s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/browser-fingerprint) | [市场](https://apizero.cn/marketplace/browser-fingerprint) |
| 94 | desensitize | 数据脱敏（敏感信息掩码） | 内容娱乐 | POST | 3 req/s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/desensitize) | [市场](https://apizero.cn/marketplace/desensitize) |
| 95 | domain-trade | 域名交易市场 | 金融数据 | GET | 3 req/s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/domain-trade) | [市场](https://apizero.cn/marketplace/domain-trade) |
| 96 | basketball | 篮球赛事 | 生活服务 | POST | 40 req/s | 20/5 | B-support | [文档](https://apizero.cn/aidocs/basketball) | [市场](https://apizero.cn/marketplace/basketball) |
| 97 | carrier-3c | 运营商三要素核验 | 身份核验 | POST | 3 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/carrier-3c) | [市场](https://apizero.cn/marketplace/carrier-3c) |
| 98 | csdn-profile | CSDN 博主信息 | 内容娱乐 | GET | 3 req/s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/csdn-profile) | [市场](https://apizero.cn/marketplace/csdn-profile) |
| 99 | ocr-qrcode | 二维码识别 | 文档识别 | POST | 2 req/s | 10/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-qrcode) | [市场](https://apizero.cn/marketplace/ocr-qrcode) |
| 100 | dns-hijack | DNS 劫持检测 | 开发工具 | GET | 3 req/s | 10000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/dns-hijack) | [市场](https://apizero.cn/marketplace/dns-hijack) |
| 101 | app-store | App Store 查询 | 开发工具 | POST | 3 req/s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/app-store) | [市场](https://apizero.cn/marketplace/app-store) |
| 102 | cf-dns | Cloudflare DNS 更新（DDNS） | 开发工具 | POST | 3 req/s | 5000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/cf-dns) | [市场](https://apizero.cn/marketplace/cf-dns) |
| 103 | ocr-cn-passport | 中国护照识别 | 文档识别 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-cn-passport) | [市场](https://apizero.cn/marketplace/ocr-cn-passport) |
| 104 | car-owner-check | 车牌车主核验 | 身份核验 | POST | 3 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/car-owner-check) | [市场](https://apizero.cn/marketplace/car-owner-check) |
| 105 | contact-parse | 联系人三要素解析 | 地理位置 | POST | 3 req/s | 500/100 | D-inventory | [文档](https://apizero.cn/aidocs/contact-parse) | [市场](https://apizero.cn/marketplace/contact-parse) |
| 106 | idcard-face-3c | 人像三要素核验 | 身份核验 | POST | 3 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/idcard-face-3c) | [市场](https://apizero.cn/marketplace/idcard-face-3c) |
| 107 | code-beautify | 代码美化图片 | 开发工具 | POST | 3 req/s | 3000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/code-beautify) | [市场](https://apizero.cn/marketplace/code-beautify) |
| 108 | ocr-bank-card | 银行卡识别 | 文档识别 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-bank-card) | [市场](https://apizero.cn/marketplace/ocr-bank-card) |
| 109 | ios-cert | iOS 证书与描述文件检测 | 开发工具 | POST | 3 req/s | 10000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/ios-cert) | [市场](https://apizero.cn/marketplace/ios-cert) |
| 110 | ocr-vehicle-license | 行驶证识别 | 文档识别 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-vehicle-license) | [市场](https://apizero.cn/marketplace/ocr-vehicle-license) |
| 111 | ocr-taxi-invoice | 出租车发票识别 | 文档识别 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-taxi-invoice) | [市场](https://apizero.cn/marketplace/ocr-taxi-invoice) |
| 112 | ocr-train-ticket | 火车票识别 | 文档识别 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-train-ticket) | [市场](https://apizero.cn/marketplace/ocr-train-ticket) |
| 113 | ocr-vehicle-invoice | 机动车发票识别 | 文档识别 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-vehicle-invoice) | [市场](https://apizero.cn/marketplace/ocr-vehicle-invoice) |
| 114 | dns-lookup | DNS 查询 | 开发工具 | POST | 3 req/s | 500/300 | B-support | [文档](https://apizero.cn/aidocs/dns-lookup) | [市场](https://apizero.cn/marketplace/dns-lookup) |
| 115 | driving-license | 驾驶证识别 | 文档识别 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/driving-license) | [市场](https://apizero.cn/marketplace/driving-license) |
| 116 | ocr-tw-permit | 台胞证识别 | 文档识别 | POST | 2 req/s | 20/ | D-inventory | [文档](https://apizero.cn/aidocs/ocr-tw-permit) | [市场](https://apizero.cn/marketplace/ocr-tw-permit) |
| 117 | bili-danmaku | B站弹幕分析 | 内容娱乐 | POST | 2 req/s | 20/10 | D-inventory | [文档](https://apizero.cn/aidocs/bili-danmaku) | [市场](https://apizero.cn/marketplace/bili-danmaku) |
| 118 | tender-files | 招中标附件列表 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-files) | [市场](https://apizero.cn/marketplace/tender-files) |
| 119 | company-contacts | 企业联系人 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/company-contacts) | [市场](https://apizero.cn/marketplace/company-contacts) |
| 120 | tender-search | 招中标信息搜索 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-search) | [市场](https://apizero.cn/marketplace/tender-search) |
| 121 | tender-number | 按编号查招中标 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-number) | [市场](https://apizero.cn/marketplace/tender-number) |
| 122 | tender-rewrite | 自然语言搜条件 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-rewrite) | [市场](https://apizero.cn/marketplace/tender-rewrite) |
| 123 | tender-extract | 招中标结构化抽取 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-extract) | [市场](https://apizero.cn/marketplace/tender-extract) |
| 124 | planned-search | 拟在建项目搜索 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/planned-search) | [市场](https://apizero.cn/marketplace/planned-search) |
| 125 | tender-contract | 合同信息搜索 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-contract) | [市场](https://apizero.cn/marketplace/tender-contract) |
| 126 | tender-source | 招中标原始网址 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-source) | [市场](https://apizero.cn/marketplace/tender-source) |
| 127 | tender-site | 按网站搜招中标 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-site) | [市场](https://apizero.cn/marketplace/tender-site) |
| 128 | tender-search-ai | AI 招中标搜索 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-search-ai) | [市场](https://apizero.cn/marketplace/tender-search-ai) |
| 129 | planned-files | 拟在建项目附件 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/planned-files) | [市场](https://apizero.cn/marketplace/planned-files) |
| 130 | tender-company | 企业招中标搜索 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-company) | [市场](https://apizero.cn/marketplace/tender-company) |
| 131 | tender-detail-ai | AI 招中标正文 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-detail-ai) | [市场](https://apizero.cn/marketplace/tender-detail-ai) |
| 132 | tender-classify | 标讯类型判别 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-classify) | [市场](https://apizero.cn/marketplace/tender-classify) |
| 133 | tender-category | 招中标14分类 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-category) | [市场](https://apizero.cn/marketplace/tender-category) |
| 134 | company-customers | 企业客户项目 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/company-customers) | [市场](https://apizero.cn/marketplace/company-customers) |
| 135 | company-stats | 企业招中标统计 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/company-stats) | [市场](https://apizero.cn/marketplace/company-stats) |
| 136 | history-today | 历史上的今天 | 内容娱乐 | POST | 3 req/s | 10000/ | D-inventory | [文档](https://apizero.cn/aidocs/history-today) | [市场](https://apizero.cn/marketplace/history-today) |
| 137 | tender-detail | 招中标正文详情 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-detail) | [市场](https://apizero.cn/marketplace/tender-detail) |
| 138 | tender-structure | 招中标结构化详情 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/tender-structure) | [市场](https://apizero.cn/marketplace/tender-structure) |
| 139 | planned-detail | 拟在建项目详情 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/planned-detail) | [市场](https://apizero.cn/marketplace/planned-detail) |
| 140 | company-suppliers | 企业供应商项目 | 招中标 | POST | 2 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/company-suppliers) | [市场](https://apizero.cn/marketplace/company-suppliers) |
| 141 | ai-video | AI 文生视频 | AI 能力 | POST | 3 req/s | / | D-inventory | [文档](https://apizero.cn/aidocs/ai-video) | [市场](https://apizero.cn/marketplace/ai-video) |
