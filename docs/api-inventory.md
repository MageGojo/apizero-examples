# ApiZero 接口导出清单

生成时间：`2026-07-06T07:53:50+00:00`  
接口总数：`105`

数据源：

- OpenAPI：https://apizero.cn/openapi.json
- LLM 完整文档：https://apizero.cn/aidocs/llms-full.txt
- Sitemap：https://apizero.cn/sitemap.xml

## 分类统计

| 分类 | 接口数 |
| --- | --- |
| AI 能力 | 4 |
| 内容娱乐 | 18 |
| 地理位置 | 3 |
| 开发工具 | 23 |
| 文档识别 | 14 |
| 生活服务 | 28 |
| 身份核验 | 9 |
| 金融数据 | 6 |

## 增长分层统计

| 增长层级 | 接口数 |
| --- | --- |
| A-core | 4 |
| A-verify | 1 |
| B-support | 9 |
| C-caution | 1 |
| D-inventory | 90 |

## 全量接口清单

免费额度列格式：`登录用户/匿名用户`，单位是每日次数。

| # | slug | 名称 | 分类 | 方法 | QPS | 免费额度 | 增长层级 | 文档 | 市场页 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | video-parse | 全平台视频元数据解析服务 | 内容娱乐 | GET | 3 / s | 20/5 | C-caution | [文档](https://apizero.cn/aidocs/video-parse) | [市场](https://apizero.cn/marketplace/video-parse) |
| 2 | barcode-gs1 | 商品条码查询PRO | 生活服务 | GET | 2 / s | 5/2 | A-verify | [文档](https://apizero.cn/aidocs/barcode-gs1) | [市场](https://apizero.cn/marketplace/barcode-gs1) |
| 3 | barcode-lookup | 商品条码查询-免费版 | 生活服务 | GET | 2 / s | 200/20 | A-core | [文档](https://apizero.cn/aidocs/barcode-lookup) | [市场](https://apizero.cn/marketplace/barcode-lookup) |
| 4 | hot-baidu | 百度热搜榜 | 生活服务 | GET | 10 / s | 10000/1000 | B-support | [文档](https://apizero.cn/aidocs/hot-baidu) | [市场](https://apizero.cn/marketplace/hot-baidu) |
| 5 | weather | 彩云天气 | 生活服务 | GET | 10 / s | 2000/100 | A-core | [文档](https://apizero.cn/aidocs/weather) | [市场](https://apizero.cn/marketplace/weather) |
| 6 | movie-box | 实时电影票房 | 生活服务 | GET | 10 / s | 20000/1000 | B-support | [文档](https://apizero.cn/aidocs/movie-box) | [市场](https://apizero.cn/marketplace/movie-box) |
| 7 | whois | Whois 域名查询 | 开发工具 | GET | 5 / s | 1000/300 | B-support | [文档](https://apizero.cn/aidocs/whois) | [市场](https://apizero.cn/marketplace/whois) |
| 8 | qq | QQ 信息 | 生活服务 | GET | 10 / s | 30000/5000 | A-core | [文档](https://apizero.cn/aidocs/qq) | [市场](https://apizero.cn/marketplace/qq) |
| 9 | shici | 随机诗词 | 内容娱乐 | POST | 5 / s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/shici) | [市场](https://apizero.cn/marketplace/shici) |
| 10 | ip-pro | IP 地址查询（街道级） | 地理位置 | GET | 3 / s | 30/5 | D-inventory | [文档](https://apizero.cn/aidocs/ip-pro) | [市场](https://apizero.cn/marketplace/ip-pro) |
| 11 | company-search | 企业工商信息查询 | 身份核验 | GET | 5 / s | 50/20 | D-inventory | [文档](https://apizero.cn/aidocs/company-search) | [市场](https://apizero.cn/marketplace/company-search) |
| 12 | moji-weather | 墨迹天气 | 生活服务 | GET | 5 / s | 3000/1000 | A-core | [文档](https://apizero.cn/aidocs/moji-weather) | [市场](https://apizero.cn/marketplace/moji-weather) |
| 13 | riddle | 谜语大全 | 内容娱乐 | POST | 5 / s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/riddle) | [市场](https://apizero.cn/marketplace/riddle) |
| 14 | exchange-rate | 实时汇率查询 | 金融数据 | GET | 5 / s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/exchange-rate) | [市场](https://apizero.cn/marketplace/exchange-rate) |
| 15 | fund | 基金估值跟踪 | 金融数据 | GET | 5 / s | 200/50 | B-support | [文档](https://apizero.cn/aidocs/fund) | [市场](https://apizero.cn/marketplace/fund) |
| 16 | hitokoto | 一言 · 经典语录 | 生活服务 | GET | 20 / s | 500000/200000 | D-inventory | [文档](https://apizero.cn/aidocs/hitokoto) | [市场](https://apizero.cn/marketplace/hitokoto) |
| 17 | netease-comment | 网易云热门乐评 | 内容娱乐 | POST | 5 / s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/netease-comment) | [市场](https://apizero.cn/marketplace/netease-comment) |
| 18 | wzry | 王者战力查询 | 生活服务 | GET | 5 / s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/wzry) | [市场](https://apizero.cn/marketplace/wzry) |
| 19 | content-moderation | 内容审核 | 内容娱乐 | POST | 10 / s | 500/100 | D-inventory | [文档](https://apizero.cn/aidocs/content-moderation) | [市场](https://apizero.cn/marketplace/content-moderation) |
| 20 | brain-teaser | 脑筋急转弯 | 生活服务 | GET | 20 / s | 200000/10000 | D-inventory | [文档](https://apizero.cn/aidocs/brain-teaser) | [市场](https://apizero.cn/marketplace/brain-teaser) |
| 21 | oil-price-forecast | 今日油价 | 生活服务 | GET | 3 / s | 10000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/oil-price-forecast) | [市场](https://apizero.cn/marketplace/oil-price-forecast) |
| 22 | gold | 黄金价格查询 | 金融数据 | GET | 5 / s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/gold) | [市场](https://apizero.cn/marketplace/gold) |
| 23 | translate | 文本翻译 | 内容娱乐 | GET | 5 / s | 5000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/translate) | [市场](https://apizero.cn/marketplace/translate) |
| 24 | ocr-text | OCR 文字识别 | 文档识别 | POST | 2 / s | 300/50 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-text) | [市场](https://apizero.cn/marketplace/ocr-text) |
| 25 | baby-naming | 八字起名 | 生活服务 | POST | 2 / s | 5000/3000 | D-inventory | [文档](https://apizero.cn/aidocs/baby-naming) | [市场](https://apizero.cn/marketplace/baby-naming) |
| 26 | express | 快递物流查询 | 生活服务 | GET | 5 / s | 100/30 | D-inventory | [文档](https://apizero.cn/aidocs/express) | [市场](https://apizero.cn/marketplace/express) |
| 27 | image-enhance | AI 图片变清晰 | AI 能力 | POST | 1 / s | 10/0 | D-inventory | [文档](https://apizero.cn/aidocs/image-enhance) | [市场](https://apizero.cn/marketplace/image-enhance) |
| 28 | tts | TTS 语音合成 | AI 能力 | POST | 3 / s | 30/10 | D-inventory | [文档](https://apizero.cn/aidocs/tts) | [市场](https://apizero.cn/marketplace/tts) |
| 29 | wzry-battle | 王者荣耀战绩查询 | 内容娱乐 | POST | 2 / s | 20/5 | D-inventory | [文档](https://apizero.cn/aidocs/wzry-battle) | [市场](https://apizero.cn/marketplace/wzry-battle) |
| 30 | crazy-thursday | 疯狂星期四文案 | 生活服务 | GET | 5 / s | 20000/10000 | D-inventory | [文档](https://apizero.cn/aidocs/crazy-thursday) | [市场](https://apizero.cn/marketplace/crazy-thursday) |
| 31 | content-extract | 网页正文提取 | 开发工具 | GET | 5 / s | 10000/5000 | B-support | [文档](https://apizero.cn/aidocs/content-extract) | [市场](https://apizero.cn/marketplace/content-extract) |
| 32 | visits-counter | 访问量计数器 | 开发工具 | GET | 10 / s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/visits-counter) | [市场](https://apizero.cn/marketplace/visits-counter) |
| 33 | doubao-image | 豆包图片生成 | AI 能力 | POST | 2 / s | 20/1 | D-inventory | [文档](https://apizero.cn/aidocs/doubao-image) | [市场](https://apizero.cn/marketplace/doubao-image) |
| 34 | dns-check | DNS 劫持检测 | 开发工具 | GET | 5 / s | 2000/50 | D-inventory | [文档](https://apizero.cn/aidocs/dns-check) | [市场](https://apizero.cn/marketplace/dns-check) |
| 35 | email-check | 邮箱地址检测 | 身份核验 | GET | 10 / s | 500/100 | D-inventory | [文档](https://apizero.cn/aidocs/email-check) | [市场](https://apizero.cn/marketplace/email-check) |
| 36 | bus-realtime | 实时公交到站 | 生活服务 | POST | 10 / s | 1000/500 | B-support | [文档](https://apizero.cn/aidocs/bus-realtime) | [市场](https://apizero.cn/marketplace/bus-realtime) |
| 37 | wallpaper | 随机壁纸 | 生活服务 | GET | 20 / s | 10000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/wallpaper) | [市场](https://apizero.cn/marketplace/wallpaper) |
| 38 | text-similarity | 文本相似度 | 开发工具 | POST | 10 / s | 50000/10000 | D-inventory | [文档](https://apizero.cn/aidocs/text-similarity) | [市场](https://apizero.cn/marketplace/text-similarity) |
| 39 | unshort | 短链还原 | 开发工具 | GET | 5 / s | 2000/300 | D-inventory | [文档](https://apizero.cn/aidocs/unshort) | [市场](https://apizero.cn/marketplace/unshort) |
| 40 | risk-score | 综合风控评分 | 身份核验 | POST | 2 / s | 200/10 | D-inventory | [文档](https://apizero.cn/aidocs/risk-score) | [市场](https://apizero.cn/marketplace/risk-score) |
| 41 | nine-grid-cutter | 九宫格切图 | 开发工具 | POST | 2 / s | 5000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/nine-grid-cutter) | [市场](https://apizero.cn/marketplace/nine-grid-cutter) |
| 42 | mobile | 手机号归属地 | 生活服务 | GET | 10 / s | 30000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/mobile) | [市场](https://apizero.cn/marketplace/mobile) |
| 43 | icp | ICP 备案查询 | 开发工具 | GET | 5 / s | 100/30 | D-inventory | [文档](https://apizero.cn/aidocs/icp) | [市场](https://apizero.cn/marketplace/icp) |
| 44 | bencao | 本草纲目·中药查询 | 生活服务 | GET | 10 / s | 10000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/bencao) | [市场](https://apizero.cn/marketplace/bencao) |
| 45 | address-parse | 中文地址解析 | 地理位置 | POST | 20 / s | 1000/100 | D-inventory | [文档](https://apizero.cn/aidocs/address-parse) | [市场](https://apizero.cn/marketplace/address-parse) |
| 46 | hash | 哈希加密计算 | 开发工具 | GET | 20 / s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/hash) | [市场](https://apizero.cn/marketplace/hash) |
| 47 | yiyan | 一言（简版） | 生活服务 | GET | 20 / s | 500000/200000 | D-inventory | [文档](https://apizero.cn/aidocs/yiyan) | [市场](https://apizero.cn/marketplace/yiyan) |
| 48 | jd-address | 京东地址解析（4 级） | 地理位置 | POST | 5 / s | 1000/10 | D-inventory | [文档](https://apizero.cn/aidocs/jd-address) | [市场](https://apizero.cn/marketplace/jd-address) |
| 49 | holiday | 中国法定节假日 | 生活服务 | GET | 20 / s | 10000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/holiday) | [市场](https://apizero.cn/marketplace/holiday) |
| 50 | invoice | 增值税发票识别 | 文档识别 | POST | 2 / s | 300/50 | D-inventory | [文档](https://apizero.cn/aidocs/invoice) | [市场](https://apizero.cn/marketplace/invoice) |
| 51 | douyin-user | 抖音用户公开信息 | 内容娱乐 | GET | 5 / s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/douyin-user) | [市场](https://apizero.cn/marketplace/douyin-user) |
| 52 | dns-query | DNS 记录查询 | 开发工具 | GET | 10 / s | 500/100 | D-inventory | [文档](https://apizero.cn/aidocs/dns-query) | [市场](https://apizero.cn/marketplace/dns-query) |
| 53 | cdn-ips | CDN 优选 IP | 开发工具 | GET | 10 / s | 2000/100 | D-inventory | [文档](https://apizero.cn/aidocs/cdn-ips) | [市场](https://apizero.cn/marketplace/cdn-ips) |
| 54 | bodyfat | 体脂率与 BMI 计算 | 生活服务 | GET | 20 / s | 200000/100000 | D-inventory | [文档](https://apizero.cn/aidocs/bodyfat) | [市场](https://apizero.cn/marketplace/bodyfat) |
| 55 | traffic-weather-alert | 限行天气联动 | 生活服务 | GET | 3 / s | 10000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/traffic-weather-alert) | [市场](https://apizero.cn/marketplace/traffic-weather-alert) |
| 56 | webmeta | 网页元数据提取 | 开发工具 | GET | 5 / s | 10000/5000 | B-support | [文档](https://apizero.cn/aidocs/webmeta) | [市场](https://apizero.cn/marketplace/webmeta) |
| 57 | ssl | SSL 证书检测 | 开发工具 | GET | 5 / s | 10000/3000 | B-support | [文档](https://apizero.cn/aidocs/ssl) | [市场](https://apizero.cn/marketplace/ssl) |
| 58 | idcard-region | 身份证归属地查询 | 身份核验 | GET | 10 / s | 1000/300 | D-inventory | [文档](https://apizero.cn/aidocs/idcard-region) | [市场](https://apizero.cn/marketplace/idcard-region) |
| 59 | blood-type | 血型遗传查询 | 生活服务 | GET | 20 / s | 20000/10000 | D-inventory | [文档](https://apizero.cn/aidocs/blood-type) | [市场](https://apizero.cn/marketplace/blood-type) |
| 60 | browser-fingerprint | 浏览器指纹风控 | 开发工具 | POST | 5 / s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/browser-fingerprint) | [市场](https://apizero.cn/marketplace/browser-fingerprint) |
| 61 | cf-dns | Cloudflare DNS 更新（DDNS） | 开发工具 | POST | 5 / s | 5000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/cf-dns) | [市场](https://apizero.cn/marketplace/cf-dns) |
| 62 | bank-card | 银行卡BIN查询 | 金融数据 | GET | 20 / s | 10000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/bank-card) | [市场](https://apizero.cn/marketplace/bank-card) |
| 63 | food-license | 食品经营许可证识别 | 文档识别 | POST | 2 / s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/food-license) | [市场](https://apizero.cn/marketplace/food-license) |
| 64 | douban-movie | 豆瓣电影信息 | 内容娱乐 | GET | 5 / s | 1000/300 | D-inventory | [文档](https://apizero.cn/aidocs/douban-movie) | [市场](https://apizero.cn/marketplace/douban-movie) |
| 65 | text-censor | 文本审核 | 内容娱乐 | POST | 5 / s | 100/30 | D-inventory | [文档](https://apizero.cn/aidocs/text-censor) | [市场](https://apizero.cn/marketplace/text-censor) |
| 66 | earthquake | 全球地震速报 | 生活服务 | POST | 10 / s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/earthquake) | [市场](https://apizero.cn/marketplace/earthquake) |
| 67 | ocr-idcard | 身份证识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-idcard) | [市场](https://apizero.cn/marketplace/ocr-idcard) |
| 68 | site-check | 网站测速诊断 | 开发工具 | GET | 2 / s | 5000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/site-check) | [市场](https://apizero.cn/marketplace/site-check) |
| 69 | code-beautify | 代码美化图片 | 开发工具 | POST | 3 / s | 3000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/code-beautify) | [市场](https://apizero.cn/marketplace/code-beautify) |
| 70 | desensitize | 数据脱敏（敏感信息掩码） | 内容娱乐 | POST | 10 / s | 200/50 | D-inventory | [文档](https://apizero.cn/aidocs/desensitize) | [市场](https://apizero.cn/marketplace/desensitize) |
| 71 | ios-cert | iOS 证书与描述文件检测 | 开发工具 | POST | 5 / s | 10000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/ios-cert) | [市场](https://apizero.cn/marketplace/ios-cert) |
| 72 | csdn-profile | CSDN 博主信息 | 内容娱乐 | GET | 5 / s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/csdn-profile) | [市场](https://apizero.cn/marketplace/csdn-profile) |
| 73 | site-security | 网站安全综合评分 | 开发工具 | GET | 2 / s | 3000/1000 | D-inventory | [文档](https://apizero.cn/aidocs/site-security) | [市场](https://apizero.cn/marketplace/site-security) |
| 74 | company-profile | 企业档案深度查询 | 身份核验 | POST | 5 / s | 3/1 | D-inventory | [文档](https://apizero.cn/aidocs/company-profile) | [市场](https://apizero.cn/marketplace/company-profile) |
| 75 | bili-dynamic | B 站用户动态 | 内容娱乐 | GET | 5 / s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/bili-dynamic) | [市场](https://apizero.cn/marketplace/bili-dynamic) |
| 76 | domain-trade | 域名交易市场 | 金融数据 | GET | 5 / s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/domain-trade) | [市场](https://apizero.cn/marketplace/domain-trade) |
| 77 | oil-price | 全国油价 | 生活服务 | POST | 10 / s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/oil-price) | [市场](https://apizero.cn/marketplace/oil-price) |
| 78 | soul-soup | 心灵毒鸡汤 | 内容娱乐 | POST | 5 / s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/soul-soup) | [市场](https://apizero.cn/marketplace/soul-soup) |
| 79 | dns-hijack | DNS 劫持检测 | 开发工具 | GET | 5 / s | 10000/5000 | D-inventory | [文档](https://apizero.cn/aidocs/dns-hijack) | [市场](https://apizero.cn/marketplace/dns-hijack) |
| 80 | idcard-organ | 身份证签发机关查询 | 身份核验 | GET | 10 / s | 1000/300 | D-inventory | [文档](https://apizero.cn/aidocs/idcard-organ) | [市场](https://apizero.cn/marketplace/idcard-organ) |
| 81 | idcard-2c | 身份证二要素核验 | 身份核验 | POST | 5 / s | 0/0 | D-inventory | [文档](https://apizero.cn/aidocs/idcard-2c) | [市场](https://apizero.cn/marketplace/idcard-2c) |
| 82 | tencent-weather | 腾讯天气 | 生活服务 | POST | 10 / s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/tencent-weather) | [市场](https://apizero.cn/marketplace/tencent-weather) |
| 83 | typhoon | 台风实时路径 | 生活服务 | POST | 10 / s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/typhoon) | [市场](https://apizero.cn/marketplace/typhoon) |
| 84 | business-license | 营业执照识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/business-license) | [市场](https://apizero.cn/marketplace/business-license) |
| 85 | ocr-vehicle-invoice | 机动车发票识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-vehicle-invoice) | [市场](https://apizero.cn/marketplace/ocr-vehicle-invoice) |
| 86 | wechat-archive | 微信文章转存 | 内容娱乐 | POST | 1 / s | 1000/100 | D-inventory | [文档](https://apizero.cn/aidocs/wechat-archive) | [市场](https://apizero.cn/marketplace/wechat-archive) |
| 87 | app-store | App Store 查询 | 开发工具 | POST | 10 / s | 1000/500 | D-inventory | [文档](https://apizero.cn/aidocs/app-store) | [市场](https://apizero.cn/marketplace/app-store) |
| 88 | stock-trend | A股实时行情 | 金融数据 | POST | 5 / s | 50/5 | D-inventory | [文档](https://apizero.cn/aidocs/stock-trend) | [市场](https://apizero.cn/marketplace/stock-trend) |
| 89 | air-history | 历史空气质量 | 生活服务 | POST | 5 / s | 50/5 | D-inventory | [文档](https://apizero.cn/aidocs/air-history) | [市场](https://apizero.cn/marketplace/air-history) |
| 90 | mingyan | 名人名言 | 内容娱乐 | POST | 5 / s | 50/30 | D-inventory | [文档](https://apizero.cn/aidocs/mingyan) | [市场](https://apizero.cn/marketplace/mingyan) |
| 91 | image-nsfw | 图片鉴黄 | AI 能力 | POST | 2 / s | 100/10 | D-inventory | [文档](https://apizero.cn/aidocs/image-nsfw) | [市场](https://apizero.cn/marketplace/image-nsfw) |
| 92 | 2fa | 2FA 动态验证码 | 开发工具 | POST | 20 / s | 1000/200 | D-inventory | [文档](https://apizero.cn/aidocs/2fa) | [市场](https://apizero.cn/marketplace/2fa) |
| 93 | carrier-3c | 运营商三要素核验 | 身份核验 | POST | 5 / s | 0/0 | D-inventory | [文档](https://apizero.cn/aidocs/carrier-3c) | [市场](https://apizero.cn/marketplace/carrier-3c) |
| 94 | ocr-vehicle-license | 行驶证识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-vehicle-license) | [市场](https://apizero.cn/marketplace/ocr-vehicle-license) |
| 95 | car-owner-check | 车牌车主核验 | 身份核验 | POST | 5 / s | 0/0 | D-inventory | [文档](https://apizero.cn/aidocs/car-owner-check) | [市场](https://apizero.cn/marketplace/car-owner-check) |
| 96 | driving-license | 驾驶证识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/driving-license) | [市场](https://apizero.cn/marketplace/driving-license) |
| 97 | ocr-bank-card | 银行卡识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-bank-card) | [市场](https://apizero.cn/marketplace/ocr-bank-card) |
| 98 | ocr-cn-passport | 中国护照识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-cn-passport) | [市场](https://apizero.cn/marketplace/ocr-cn-passport) |
| 99 | ocr-health-cert | 健康证识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-health-cert) | [市场](https://apizero.cn/marketplace/ocr-health-cert) |
| 100 | ocr-train-ticket | 火车票识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-train-ticket) | [市场](https://apizero.cn/marketplace/ocr-train-ticket) |
| 101 | hot-search | 全网热搜聚合 | 内容娱乐 | POST | 3 / s | 3000/2000 | D-inventory | [文档](https://apizero.cn/aidocs/hot-search) | [市场](https://apizero.cn/marketplace/hot-search) |
| 102 | ocr-taxi-invoice | 出租车发票识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-taxi-invoice) | [市场](https://apizero.cn/marketplace/ocr-taxi-invoice) |
| 103 | ocr-tw-permit | 台胞证识别 | 文档识别 | POST | 2 / s | 20/0 | D-inventory | [文档](https://apizero.cn/aidocs/ocr-tw-permit) | [市场](https://apizero.cn/marketplace/ocr-tw-permit) |
| 104 | bili-danmaku | B站弹幕分析 | 内容娱乐 | POST | 2 / s | 20/10 | D-inventory | [文档](https://apizero.cn/aidocs/bili-danmaku) | [市场](https://apizero.cn/marketplace/bili-danmaku) |
| 105 | dns-lookup | DNS 查询 | 开发工具 | POST | 5 / s | 500/300 | B-support | [文档](https://apizero.cn/aidocs/dns-lookup) | [市场](https://apizero.cn/marketplace/dns-lookup) |
