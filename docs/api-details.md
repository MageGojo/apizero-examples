# ApiZero 接口详细文档

生成时间：`2026-09-19T00:50:53+00:00`  
接口总数：`118`

这份文档给人和 AI 一起用：每个接口都包含用途、endpoint、计费/QPS、免费额度、请求参数、请求体字段、响应示例和可复制 cURL 模板。

## 快速索引

| # | slug | 名称 | 方法 | 分类 | 增长层级 | 必填 query | 跳转 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | weather | 彩云天气 | GET | 生活服务 | A-core |  | [详情](#weather) |
| 2 | barcode-gs1 | 商品条码查询PRO | GET | 生活服务 | A-verify | code | [详情](#barcode-gs1) |
| 3 | bus-realtime | 实时公交到站 | POST | 生活服务 | B-support | city, station, line | [详情](#bus-realtime) |
| 4 | video-parse | 全平台视频元数据解析服务 | GET | 内容娱乐 | C-caution | url | [详情](#video-parse) |
| 5 | stock-trend | A股实时行情 | POST | 金融数据 | B-support | code | [详情](#stock-trend) |
| 6 | movie-box | 实时电影票房 | GET | 生活服务 | B-support |  | [详情](#movie-box) |
| 7 | company-search | 企业工商信息查询 | GET | 身份核验 | D-inventory | name | [详情](#company-search) |
| 8 | barcode-lookup | 商品条码查询-免费版 | GET | 生活服务 | A-core | barcode | [详情](#barcode-lookup) |
| 9 | express | 快递物流查询-免费版 | GET | 生活服务 | D-inventory | number | [详情](#express) |
| 10 | douyin-user | 抖音用户公开信息 | GET | 内容娱乐 | D-inventory | url | [详情](#douyin-user) |
| 11 | oil-price | 全国油价 | POST | 生活服务 | D-inventory | province | [详情](#oil-price) |
| 12 | qq | QQ 信息 | GET | 生活服务 | A-core | qq | [详情](#qq) |
| 13 | oil-price-forecast | 今日油价 | GET | 生活服务 | D-inventory |  | [详情](#oil-price-forecast) |
| 14 | exchange-rate | 实时汇率查询 | GET | 金融数据 | D-inventory |  | [详情](#exchange-rate) |
| 15 | wzry | 王者战力查询 | GET | 生活服务 | D-inventory | action, zone | [详情](#wzry) |
| 16 | hot-baidu | 百度热搜榜 | GET | 生活服务 | B-support |  | [详情](#hot-baidu) |
| 17 | typhoon | 台风实时路径 | POST | 生活服务 | D-inventory |  | [详情](#typhoon) |
| 18 | jd-address | 京东地址解析（4 级） | POST | 地理位置 | D-inventory | address | [详情](#jd-address) |
| 19 | moji-weather | 天气查询 | GET | 生活服务 | A-core | op | [详情](#moji-weather) |
| 20 | gold | 黄金价格查询 | GET | 金融数据 | D-inventory |  | [详情](#gold) |
| 21 | content-extract | 网页正文提取 | GET | 开发工具 | B-support | url | [详情](#content-extract) |
| 22 | ocr-text | OCR 文字识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-text) |
| 23 | wallpaper | 随机壁纸 | GET | 生活服务 | D-inventory |  | [详情](#wallpaper) |
| 24 | icp | ICP 备案查询 | GET | 开发工具 | D-inventory | domain | [详情](#icp) |
| 25 | ip-pro | IP 地址查询（街道级） | GET | 地理位置 | D-inventory |  | [详情](#ip-pro) |
| 26 | holiday | 中国法定节假日 | GET | 生活服务 | D-inventory |  | [详情](#holiday) |
| 27 | mobile | 手机号归属地 | GET | 生活服务 | D-inventory | mobile | [详情](#mobile) |
| 28 | 2fa | 2FA 动态验证码 | POST | 开发工具 | D-inventory | secret | [详情](#2fa) |
| 29 | whois | Whois 域名查询 | GET | 开发工具 | B-support | domain | [详情](#whois) |
| 30 | fund | 基金估值跟踪 | GET | 金融数据 | B-support | action | [详情](#fund) |
| 31 | douyin-works | 抖音用户作品 | POST | 内容娱乐 | C-caution | cookie | [详情](#douyin-works) |
| 32 | brain-teaser | 脑筋急转弯 | GET | 生活服务 | D-inventory |  | [详情](#brain-teaser) |
| 33 | netease-comment | 网易云热门乐评 | POST | 内容娱乐 | D-inventory |  | [详情](#netease-comment) |
| 34 | douban-movie | 豆瓣电影信息 | GET | 内容娱乐 | D-inventory | id | [详情](#douban-movie) |
| 35 | yiyan | 一言（简版） | GET | 生活服务 | D-inventory |  | [详情](#yiyan) |
| 36 | visits-counter | 访问量计数器 | GET | 开发工具 | D-inventory |  | [详情](#visits-counter) |
| 37 | hitokoto | 一言 · 经典语录 | GET | 生活服务 | D-inventory |  | [详情](#hitokoto) |
| 38 | hot-search | 全网热搜聚合 | POST | 内容娱乐 | D-inventory |  | [详情](#hot-search) |
| 39 | tts | TTS 语音合成 | POST | AI 能力 | D-inventory | text | [详情](#tts) |
| 40 | content-moderation | 内容审核 | POST | 内容娱乐 | D-inventory | text, texts | [详情](#content-moderation) |
| 41 | ocr-health-cert | 健康证识别 | POST | 生活服务 | D-inventory | input_type, input_data | [详情](#ocr-health-cert) |
| 42 | shici | 随机诗词 | POST | 内容娱乐 | D-inventory |  | [详情](#shici) |
| 43 | baby-naming | 八字起名 | POST | 生活服务 | D-inventory | surname, birth_year, birth_month, birth_day, name | [详情](#baby-naming) |
| 44 | express-pro | 快递查询PRO | GET | 生活服务 | B-support | number | [详情](#express-pro) |
| 45 | tencent-weather | 腾讯天气 | POST | 生活服务 | D-inventory | province, city | [详情](#tencent-weather) |
| 46 | wechat-archive | 微信文章转存 | POST | 内容娱乐 | D-inventory | url | [详情](#wechat-archive) |
| 47 | riddle | 谜语大全 | POST | 内容娱乐 | D-inventory |  | [详情](#riddle) |
| 48 | crazy-thursday | 疯狂星期四文案 | GET | 生活服务 | D-inventory |  | [详情](#crazy-thursday) |
| 49 | wzry-battle | 王者荣耀战绩查询 | POST | 内容娱乐 | D-inventory | session, action, keyword, user_id, role_id | [详情](#wzry-battle) |
| 50 | image-enhance | AI 图片变清晰 | POST | AI 能力 | D-inventory | img | [详情](#image-enhance) |
| 51 | earthquake | 全球地震速报 | POST | 生活服务 | D-inventory |  | [详情](#earthquake) |
| 52 | company-profile | 企业档案深度查询 | POST | 身份核验 | D-inventory | company | [详情](#company-profile) |
| 53 | translate | 文本翻译 | GET | 内容娱乐 | D-inventory | q | [详情](#translate) |
| 54 | mingyan | 名人名言 | POST | 内容娱乐 | D-inventory |  | [详情](#mingyan) |
| 55 | air-history | 历史空气质量 | POST | 生活服务 | D-inventory | city, month | [详情](#air-history) |
| 56 | soul-soup | 心灵毒鸡汤 | POST | 内容娱乐 | D-inventory |  | [详情](#soul-soup) |
| 57 | doubao-image | 豆包图片生成 | POST | AI 能力 | D-inventory | prompt | [详情](#doubao-image) |
| 58 | ai-chat | 大模型 | POST | AI 能力 | B-support | model, messages | [详情](#ai-chat) |
| 59 | bank-card | 银行卡BIN查询 | GET | 金融数据 | D-inventory |  | [详情](#bank-card) |
| 60 | food-license | 食品经营许可证识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#food-license) |
| 61 | site-security | 网站安全综合评分 | GET | 开发工具 | D-inventory | domain | [详情](#site-security) |
| 62 | hash | 哈希加密计算 | GET | 开发工具 | D-inventory | text | [详情](#hash) |
| 63 | email-check | 邮箱地址检测 | GET | 身份核验 | D-inventory | email | [详情](#email-check) |
| 64 | risk-score | 综合风控评分 | POST | 身份核验 | D-inventory |  | [详情](#risk-score) |
| 65 | address-parse | 中文地址解析 | POST | 地理位置 | D-inventory | address | [详情](#address-parse) |
| 66 | ocr-idcard | 身份证识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-idcard) |
| 67 | business-license | 营业执照识别 | POST | 生活服务 | D-inventory | input_type, input_data | [详情](#business-license) |
| 68 | unshort | 短链还原 | GET | 开发工具 | D-inventory | url | [详情](#unshort) |
| 69 | site-check | 网站测速诊断 | GET | 开发工具 | D-inventory | url | [详情](#site-check) |
| 70 | ssl | SSL 证书检测 | GET | 开发工具 | B-support | domain | [详情](#ssl) |
| 71 | text-similarity | 文本相似度 | POST | 开发工具 | D-inventory | text1, text2 | [详情](#text-similarity) |
| 72 | bencao | 本草纲目·中药查询 | GET | 生活服务 | D-inventory | msg | [详情](#bencao) |
| 73 | traffic-weather-alert | 限行天气联动 | GET | 生活服务 | D-inventory | city | [详情](#traffic-weather-alert) |
| 74 | dns-check | DNS 劫持检测 | GET | 开发工具 | D-inventory | domain | [详情](#dns-check) |
| 75 | idcard-region | 身份证归属地查询 | GET | 身份核验 | D-inventory | idcard | [详情](#idcard-region) |
| 76 | dns-query | DNS 记录查询 | GET | 开发工具 | D-inventory | host | [详情](#dns-query) |
| 77 | webmeta | 网页元数据提取 | GET | 开发工具 | B-support | url | [详情](#webmeta) |
| 78 | bili-dynamic | B 站用户动态 | GET | 内容娱乐 | D-inventory | uid | [详情](#bili-dynamic) |
| 79 | invoice | 增值税发票识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#invoice) |
| 80 | idcard-organ | 身份证签发机关查询 | GET | 身份核验 | D-inventory | id | [详情](#idcard-organ) |
| 81 | image-nsfw | 图片鉴黄 | POST | AI 能力 | D-inventory |  | [详情](#image-nsfw) |
| 82 | nine-grid-cutter | 九宫格切图 | POST | 开发工具 | D-inventory |  | [详情](#nine-grid-cutter) |
| 83 | cdn-ips | CDN 优选 IP | GET | 开发工具 | D-inventory | server, type | [详情](#cdn-ips) |
| 84 | browser-fingerprint | 浏览器指纹风控 | POST | 开发工具 | D-inventory | ua | [详情](#browser-fingerprint) |
| 85 | blood-type | 血型遗传查询 | GET | 生活服务 | D-inventory | father, mother | [详情](#blood-type) |
| 86 | bodyfat | 体脂率与 BMI 计算 | GET | 生活服务 | D-inventory | weight, height, waist, gender | [详情](#bodyfat) |
| 87 | idcard-2c | 身份证二要素核验 | POST | 身份核验 | D-inventory | name, idcard | [详情](#idcard-2c) |
| 88 | domain-trade | 域名交易市场 | GET | 金融数据 | D-inventory |  | [详情](#domain-trade) |
| 89 | text-censor | 文本审核 | POST | 内容娱乐 | D-inventory | text | [详情](#text-censor) |
| 90 | desensitize | 数据脱敏（敏感信息掩码） | POST | 内容娱乐 | D-inventory | text | [详情](#desensitize) |
| 91 | ocr-qrcode | 二维码识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-qrcode) |
| 92 | csdn-profile | CSDN 博主信息 | GET | 内容娱乐 | D-inventory | username | [详情](#csdn-profile) |
| 93 | dns-hijack | DNS 劫持检测 | GET | 开发工具 | D-inventory | domain | [详情](#dns-hijack) |
| 94 | app-store | App Store 查询 | POST | 开发工具 | D-inventory |  | [详情](#app-store) |
| 95 | douyin-search | 抖音视频搜索 | POST | 内容娱乐 | C-caution | keyword, cookie | [详情](#douyin-search) |
| 96 | cf-dns | Cloudflare DNS 更新（DDNS） | POST | 开发工具 | D-inventory | domain, host, ip, token | [详情](#cf-dns) |
| 97 | ocr-cn-passport | 中国护照识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-cn-passport) |
| 98 | user-info | 账户信息查询 | GET | 开发工具 | D-inventory |  | [详情](#user-info) |
| 99 | carrier-3c | 运营商三要素核验 | POST | 身份核验 | D-inventory | name, mobile, idcard | [详情](#carrier-3c) |
| 100 | car-owner-check | 车牌车主核验 | POST | 身份核验 | D-inventory | cp, m | [详情](#car-owner-check) |
| 101 | football | 足球赛事 | POST | 生活服务 | B-support |  | [详情](#football) |
| 102 | ocr-bank-card | 银行卡识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-bank-card) |
| 103 | ios-cert | iOS 证书与描述文件检测 | POST | 开发工具 | D-inventory | cert, provision | [详情](#ios-cert) |
| 104 | ocr-train-ticket | 火车票识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-train-ticket) |
| 105 | ocr-vehicle-license | 行驶证识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-vehicle-license) |
| 106 | ocr-tw-permit | 台胞证识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-tw-permit) |
| 107 | ocr-vehicle-invoice | 机动车发票识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-vehicle-invoice) |
| 108 | contact-parse | 联系人三要素解析 | POST | 地理位置 | D-inventory | text | [详情](#contact-parse) |
| 109 | idcard-face-3c | 人像三要素核验 | POST | 身份核验 | D-inventory | name, idcard, image | [详情](#idcard-face-3c) |
| 110 | ocr-taxi-invoice | 出租车发票识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-taxi-invoice) |
| 111 | basketball | 篮球赛事 | POST | 生活服务 | B-support |  | [详情](#basketball) |
| 112 | code-beautify | 代码美化图片 | POST | 开发工具 | D-inventory | code | [详情](#code-beautify) |
| 113 | driving-license | 驾驶证识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#driving-license) |
| 114 | drug-insert | 药品说明书查询 | GET | 生活服务 | B-support | name, id | [详情](#drug-insert) |
| 115 | ocr-text-box | OCR 文字坐标识别 | POST | 文档识别 | D-inventory | input_type, input_data | [详情](#ocr-text-box) |
| 116 | dns-lookup | DNS 查询 | POST | 开发工具 | B-support | domain | [详情](#dns-lookup) |
| 117 | bili-danmaku | B站弹幕分析 | POST | 内容娱乐 | D-inventory | video | [详情](#bili-danmaku) |
| 118 | ai-video | AI 文生视频 | POST | AI 能力 | D-inventory | model, messages | [详情](#ai-video) |

<a id="weather"></a>

## 1. 彩云天气 `weather`

全功能天气接口，覆盖：
  • 实时天气（温度/湿度/风/能见度/AQI/PM2.5）
  • 分钟级降水预报（未来 2 小时）
  • 小时预报（最长 360 小时 = 15 天）
  • 天预报（最长 15 天，含日出日落、温度极值、生活指数）
  • 综合数据（一次返回全部 + 气象预警）

特色：
  • 支持城市名直接查询（内置常用中国城市，也支持经纬度）
  • 自动中文化：skycon 转中文、风向转 16 方位、风速转蒲福风级、AQI 转等级颜色
  • 预警标准化：从原始 title 提取颜色（蓝/黄/橙/红）和级别（一般/较重/严重/特别严重）
  • 顶层 summary 字段提供"一眼看懂"的实时摘要

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/weather` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 2000 次；匿名 100 次 |
| 增长层级 | A-core |
| 推广动作 | 主推 |
| 推广角度 | 免费天气 API；城市名直接查；适合小程序、网站天气模块、日报脚本。 |
| 官网文档 | https://apizero.cn/aidocs/weather |
| Marketplace | https://apizero.cn/marketplace/weather |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 固定为 weather：综合数据包 | weather |
| city | string | 否 | 城市/地区名称，与 location 二选一 | 北京 |
| location | string | 否 | 经纬度「经度,纬度」，优先级高于 city | 116.3975,39.9085 |
| alert | boolean | 否 | 是否附带气象预警 | true |
| days | integer | 否 | 天预报天数 1–15 | 7 |
| hours | integer | 否 | 小时预报小时数，最长 360 | 48 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/weather?city=北京&type=weather"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "type": "weather",
    "location": {
      "city": "北京",
      "longitude": 116.4074,
      "latitude": 39.9042,
      "timezone": "Asia/Shanghai"
    },
    "server_time": "2026-07-31 04:10:38",
    "forecast_keypoint": "多云，今天晚间23点钟后转小雨，其后多云",
    "summary": {
      "city": "北京",
      "skycon": "多云",
      "skycon_emoji": "☁️",
      "skycon_code": "PARTLY_CLOUDY_NIGHT",
      "temperature": 28.8,
      "apparent_temperature": 32.6,
      "humidity_percent": 81,
      "cloudrate_percent": 29,
      "visibility_km": 8.2,
      "wind": {
        "speed_ms": 5.6,
        "direction_deg": 199.6,
        "direction_text": "西南偏南风",
        "level": 4,
        "level_text": "和风"
      },
      "air_quality": {
        "aqi": 36,
        "level": "优",
        "level_color": "green",
        "pm25": 15
      },
      "alert_count": 0
    },
    "alerts": [],
    "realtime": {
      "status": "ok",
      "temperature": 28.76,
      "humidity": 0.81,
      "cloudrate": 0.29,
      "skycon": "PARTLY_CLOUDY_NIGHT",
      "visibility": 8.19,
      "dswrf": 0,
      "wind": {
        "speed": 5.58,
        "direction": 199.6
      },
      "pressure": 99652.7,
      "apparent_temperature": 32.6,
      "precipitation": {
        "local": {
          "status": "ok",
          "datasource": "radar",
          "intensity": 0
        },
        "nearest": {
          "status": "ok",
          "distance": 144.37,
          "intensity": 0.1875
        }
      },
      "air_quality": {
        "pm25": 15,
        "pm10": 36,
        "o3": 57,
        "so2": 1,
        "no2": 18,
        "co": 0.5,
        "aqi": {
          "chn": 36,
          "usa": 61
        },
        "description": {
          "chn": "优",
          "usa": "良"
        }
      },
      "life_index": {
        "ultraviolet": {
          "index": 0,
          "desc": "无"
        },
        "comfort": {
          "index": 0,
          "desc": "闷热"
        }
      }
    },
    "minutely": {
      "status": "ok",
      "datasource": "radar",
      "precipitation_2h": [
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0
      ],
      "precipitation": [
        0,
        0,
        0
      ],
      "accumulation": [
        0,
        0
      ],
      "probability": [
        0,
        0,
        0,
        0
      ],
      "description": "未来两小时不会有雨。夜深了，注意休息哦～"
    },
    "hourly": {
      "status": "ok",
      "description": "多云，今天晚间23点钟后转小雨，其后多云",
      "precipitation": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "value": 0,
          "probability": 0
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "value": 0,
          "probability": 0
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "value": 0,
          "probability": 0
        }
      ],
      "temperature": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "value": 28.76
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "value": 28.44
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "value": 28.32
        }
      ],
      "apparent_temperature": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "value": 32.6
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "value": 32.7
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "value": 32.6
        },
        {
          "datetime": "2026-07-31T07:00+08:00",
          "value": 33
        },
        {
          "datetime": "2026-07-31T08:00+08:00",
          "value": 33.8
        },
        {
          "datetime": "2026-07-31T09:00+08:00",
          "value": 34.7
        }
      ],
      "wind": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "speed": 5.58,
          "direction": 199.6
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "speed": 4.61,
          "direction": 187.18
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "speed": 4.83,
          "direction": 194.24
        }
      ],
      "humidity": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "value": 0.81
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "value": 0.86
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "value": 0.87
        }
      ],
      "cloudrate": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "value": 0.29
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "value": 0.29
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "value": 0.8
        }
      ],
      "skycon": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "value": "PARTLY_CLOUDY_NIGHT"
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "value": "PARTLY_CLOUDY_NIGHT"
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "value": "PARTLY_CLOUDY_DAY"
        }
      ],
      "pressure": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "value": 99652.7
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "value": 99625.53
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "value": 99621.15
        }
      ],
      "visibility": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "value": 8.19
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "value": 8.12
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "value": 0.62
        }
      ],
      "dswrf": [
        {
          "datetime": "2026-07-31T04:00+08:00",
          "value": 0
        },
        {
          "datetime": "2026-07-31T05:00+08:00",
          "value": 0
        },
        {
          "datetime": "2026-07-31T06:00+08:00",
          "value": 37.953125
        }
      ],
      "air_quality": {
        "aqi": [
          {
            "datetime": "2026-07-31T04:00+08:00",
            "value": {
              "chn": 36,
              "usa": 61
            }
          },
          {
            "datetime": "2026-07-31T05:00+08:00",
            "value": {
              "chn": 47,
              "usa": 71
            }
          }
        ],
        "pm25": [
          {
            "datetime": "2026-07-31T04:00+08:00",
            "value": 15
          },
          {
            "datetime": "2026-07-31T05:00+08:00",
            "value": 22
          }
        ]
      }
    },
    "daily": {
      "status": "ok",
      "astro": [
        {
          "date": "2026-07-31T00:00+08:00",
          "sunrise": {
            "time": "05:11"
          },
          "sunset": {
            "time": "19:29"
          }
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "sunrise": {
            "time": "05:12"
          },
          "sunset": {
            "time": "19:28"
          }
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "sunrise": {
            "time": "05:13"
          },
          "sunset": {
            "time": "19:27"
          }
        }
      ],
      "precipitation_08h_20h": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 0,
          "min": 0,
          "avg": 0,
          "probability": 0
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 0.4096,
          "min": 0,
          "avg": 0.0341,
          "probability": 60
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 1.8265,
          "min": 0,
          "avg": 0.5487,
          "probability": 70
        }
      ],
      "precipitation_20h_32h": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 3.6836,
          "min": 0,
          "avg": 0.6972,
          "probability": 70
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 1.1707,
          "min": 0,
          "avg": 0.1741,
          "probability": 60
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 4.1774,
          "min": 0,
          "avg": 0.4281,
          "probability": 60
        }
      ],
      "precipitation": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 0.9151,
          "min": 0,
          "avg": 0.0458,
          "probability": 60
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 3.6836,
          "min": 0,
          "avg": 0.3275,
          "probability": 60
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 1.8265,
          "min": 0,
          "avg": 0.4506,
          "probability": 70
        }
      ],
      "temperature": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 32.97,
          "min": 27.63,
          "avg": 30.4
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 32.08,
          "min": 25.93,
          "avg": 28.99
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 33.45,
          "min": 26.76,
          "avg": 29.39
        }
      ],
      "temperature_08h_20h": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 32.97,
          "min": 28.59,
          "avg": 31.54
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 32.08,
          "min": 26.59,
          "avg": 30.26
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 33.45,
          "min": 27.39,
          "avg": 30.84
        }
      ],
      "temperature_20h_32h": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 29.71,
          "min": 25.93,
          "avg": 27.38
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 30.74,
          "min": 26.76,
          "avg": 28.39
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 29.32,
          "min": 26.49,
          "avg": 27.33
        }
      ],
      "wind": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": {
            "speed": 9.44,
            "direction": 219.58
          },
          "min": {
            "speed": 3.39,
            "direction": 197.28
          },
          "avg": {
            "speed": 6.19,
            "direction": 193.96
          }
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": {
            "speed": 6.31,
            "direction": 182.94
          },
          "min": {
            "speed": 1.43,
            "direction": 40.91
          },
          "avg": {
            "speed": 3.88,
            "direction": 179.33
          }
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": {
            "speed": 7.42,
            "direction": 178.05
          },
          "min": {
            "speed": 1.81,
            "direction": 47.42
          },
          "avg": {
            "speed": 3.64,
            "direction": 154.29
          }
        }
      ],
      "wind_08h_20h": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": {
            "speed": 9.44,
            "direction": 219.58
          },
          "min": {
            "speed": 3.39,
            "direction": 197.28
          },
          "avg": {
            "speed": 6.77,
            "direction": 189.98
          }
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": {
            "speed": 6.31,
            "direction": 182.94
          },
          "min": {
            "speed": 1.43,
            "direction": 40.91
          },
          "avg": {
            "speed": 2.92,
            "direction": 164.04
          }
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": {
            "speed": 7.42,
            "direction": 178.05
          },
          "min": {
            "speed": 2.89,
            "direction": 3.58
          },
          "avg": {
            "speed": 3.27,
            "direction": 172
          }
        }
      ],
      "wind_20h_32h": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": {
            "speed": 6.16,
            "direction": 201.61
          },
          "min": {
            "speed": 2.17,
            "direction": 184.76
          },
          "avg": {
            "speed": 4.41,
            "direction": 203.52
          }
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": {
            "speed": 5.17,
            "direction": 205.14
          },
          "min": {
            "speed": 1.81,
            "direction": 47.42
          },
          "avg": {
            "speed": 2.73,
            "direction": 152.69
          }
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": {
            "speed": 7.07,
            "direction": 26.62
          },
          "min": {
            "speed": 1.99,
            "direction": 84.81
          },
          "avg": {
            "speed": 5.19,
            "direction": 38.41
          }
        }
      ],
      "humidity": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 0.87,
          "min": 0.56,
          "avg": 0.7
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 0.86,
          "min": 0.57,
          "avg": 0.74
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 0.87,
          "min": 0.55,
          "avg": 0.74
        }
      ],
      "cloudrate": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 1,
          "min": 0.07,
          "avg": 0.49
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 0.92,
          "min": 0,
          "avg": 0.39
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 1,
          "min": 0.77,
          "avg": 0.99
        }
      ],
      "pressure": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 99755.52,
          "min": 99330.88,
          "avg": 99516.91
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 99706.07,
          "min": 99385.45,
          "avg": 99525.87
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 99979.26,
          "min": 99645.55,
          "avg": 99818.24
        }
      ],
      "visibility": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 24.18,
          "min": 0.62,
          "avg": 15.59
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 29.1,
          "min": 5.83,
          "avg": 19.48
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 24.14,
          "min": 0.23,
          "avg": 15.4
        }
      ],
      "dswrf": [
        {
          "date": "2026-07-31T00:00+08:00",
          "max": 776.5,
          "min": 0,
          "avg": 229.5
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "max": 782,
          "min": 0,
          "avg": 214.2
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "max": 604.5,
          "min": 0,
          "avg": 138.5
        }
      ],
      "air_quality": {
        "aqi": [
          {
            "date": "2026-07-31T00:00+08:00",
            "max": {
              "chn": 53,
              "usa": 86
            },
            "avg": {
              "chn": 47,
              "usa": 77
            },
            "min": {
              "chn": 36,
              "usa": 61
            }
          },
          {
            "date": "2026-08-01T00:00+08:00",
            "max": {
              "chn": 53,
              "usa": 102
            },
            "avg": {
              "chn": 50,
              "usa": 90
            },
            "min": {
              "chn": 43,
              "usa": 86
            }
          }
        ],
        "pm25": [
          {
            "date": "2026-07-31T00:00+08:00",
            "max": 29,
            "avg": 24,
            "min": 15
          },
          {
            "date": "2026-08-01T00:00+08:00",
            "max": 36,
            "avg": 31,
            "min": 29
          }
        ]
      },
      "skycon": [
        {
          "date": "2026-07-31T00:00+08:00",
          "value": "LIGHT_RAIN"
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "value": "LIGHT_RAIN"
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "value": "MODERATE_RAIN"
        }
      ],
      "skycon_08h_20h": [
        {
          "date": "2026-07-31T00:00+08:00",
          "value": "PARTLY_CLOUDY_DAY"
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "value": "LIGHT_RAIN"
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "value": "MODERATE_RAIN"
        }
      ],
      "skycon_20h_32h": [
        {
          "date": "2026-07-31T00:00+08:00",
          "value": "MODERATE_RAIN"
        },
        {
          "date": "2026-08-01T00:00+08:00",
          "value": "LIGHT_RAIN"
        },
        {
          "date": "2026-08-02T00:00+08:00",
          "value": "LIGHT_RAIN"
        }
      ],
      "life_index": {
        "ultraviolet": [
          {
            "date": "2026-07-31T00:00+08:00",
            "index": "1",
            "desc": "最弱"
          },
          {
            "date": "2026-08-01T00:00+08:00",
            "index": "2",
            "desc": "弱"
          }
        ],
        "carWashing": [
          {
            "date": "2026-07-31T00:00+08:00",
            "index": "3",
            "desc": "较不适宜"
          },
          {
            "date": "2026-08-01T00:00+08:00",
            "index": "3",
            "desc": "较不适宜"
          }
        ],
        "dressing": [
          {
            "date": "2026-07-31T00:00+08:00",
            "index": "2",
            "desc": "很热"
          },
          {
            "date": "2026-08-01T00:00+08:00",
            "index": "2",
            "desc": "很热"
          }
        ]
      }
    }
  },
  "request_id": "ms7y7k0z8731cc94",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="barcode-gs1"></a>

## 2. 商品条码查询PRO `barcode-gs1`

官方权威的商品条码查询接口，返回国内注册商品条码的登记信息。
与 `barcode-lookup` 定位不同：

- 官方商品图只在本接口 `images`；免费版 barcode-lookup 不含图片，也不再提供 image 字段
- 本接口**官方权威**：返回厂商注册名称、产品登记信息、上市日期、官方商品图等可追溯的官方数据
- 本接口**仅覆盖国内注册条码**(6/690 开头)，进口商品或非注册条码会返回 found=false
- 适合合规核验、溯源、上架审核等对数据权威性要求高的场景

支持输入格式：8 / 12 / 13 / 14 位纯数字，或 16 位 AI(01) 前缀 + GTIN-14。

返回数据包含：产品名称、品牌、通用名、分类（含分类编号）、规格、净含量、上市日期、厂商企业名、官方商品图、条码激活日期、产品创建日期、企业注册日期、已用天数等核心字段，部分情况下额外提供生产国、企业地址、参考售价、厂商识别代码等扩展字段。
【调用额度说明】
本接口额度以本页为准（与平台 VIP 在多数接口上的默认日免费额度不同）：
- 匿名试用：每日 2 次
- 登录免费：每日 5 次
- 黄金 VIP：每日 5,000 次
- 企业 VIP：按平台 VIP 日额度
- 高频场景：建议购买本接口基础版月卡 / 年卡（更高总量与 QPS）；超出后也可按次计费

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/barcode-gs1` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 按次付费 · 点数包 · 月套餐 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 5 次；匿名 2 次 |
| 增长层级 | A-verify |
| 推广动作 | 验证后主推 |
| 推广角度 | PRO 商品条码查询；发文前先用真实条码验证，降低新用户复制失败率。 |
| 官网文档 | https://apizero.cn/aidocs/barcode-gs1 |
| Marketplace | https://apizero.cn/marketplace/barcode-gs1 |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| code | string | 是 | 商品条形码（8/12/13/14 位纯数字，或 16 位 AI(01) 前缀 + GTIN-14） | 6921168509256 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/barcode-gs1?code=6921168509256"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "barcode": "6921168509256",
    "gtin14": "06921168509256",
    "found": true,
    "registered": true,
    "registration_message": "该商品条码已在中国物品编码中心注册，编码信息已按规定通报。",
    "name": "农夫山泉饮用天然水",
    "brand": "农夫山泉",
    "general_name": "水（瓶装、桶装等）",
    "feature": null,
    "category": "水（瓶装、桶装等）(10000232)",
    "specification": "550毫升",
    "net_content": "550毫升",
    "sale_date": "2008-07-24",
    "manufacturer": "农夫山泉股份有限公司",
    "images": [
      "https://oss.gds.org.cn/userfile1/uploadb/gra/sj211126172650708225/06921168509256/06921168509256.1.jpg"
    ],
    "product_create_date": "2008-11-07T19:39:39.28",
    "use_days": 6469,
    "category_code": "10000232",
    "height": "227毫米",
    "width": "64毫米",
    "depth": "64毫米",
    "gross_weight": "586克",
    "studio": "高度：227毫米 宽度：64毫米 深度：64毫米 毛重：586克 净含量：550毫升",
    "official": {
      "keyword": "农夫山泉",
      "branch_code": "3301",
      "gtin": "06921168509256",
      "specification": "550毫升",
      "is_private": false,
      "firm_name": "农夫山泉股份有限公司",
      "brandcn": "农夫山泉",
      "picture_filename": "/userfile1/uploadb/gra/sj211126172650708225/06921168509256/06921168509256.1.jpg",
      "description": "",
      "logout_flag": "0",
      "have_ms_product": 0,
      "base_create_time": "2008-11-07T19:39:39.28",
      "branch_name": "浙江分中心",
      "base_source": "www",
      "gpc": "10000232",
      "gpcname": "水（瓶装、桶装等）",
      "saledate": "2008-07-24T00:00:00",
      "saledateyear": 2008,
      "base_last_updated": "2024-07-24T11:45:49",
      "gtinstatus": 1,
      "RegulatedProductName": "农夫山泉饮用天然水",
      "certificateNumber": null
    },
    "official_hit": true
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="bus-realtime"></a>

## 3. 实时公交到站 `bus-realtime`

输入官方城市和官方站名，实时查询该站各公交线路的到站信息：车牌、预计到站时间、剩余站数、票价、终点方向。同一接口用 type 切换：query=到站（默认）、cities=覆盖城市列表、stations=按关键词搜官方站名、line=静态线路详情（全程站点、首末班、票价）。高德「五一广场（地铁站）」不要直接查到站，先搜官方站名。覆盖全国数百城市，支持双向查询（direction）。完全免费。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/bus-realtime` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 10 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 500 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 实时公交 API；适合城市出行小程序、通勤提醒工具。 |
| 官网文档 | https://apizero.cn/aidocs/bus-realtime |
| Marketplace | https://apizero.cn/marketplace/bus-realtime |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 不传或 query=到站 | query |
| city | string | 是 | 官方城市名；先用 type=cities | 长沙 |
| station | string | 是 | 官方站名；先用 type=stations | 五一广场 |
| direction | int | 否 | 1=默认，2=反方向 | 1 |
| line | string | 是 | 官方线路名，如 401 / 401路（也认 station） | 401 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 不传或 query=到站 | query |
| city | string | 是 | 官方城市名；先用 type=cities | 长沙 |
| station | string | 是 | 官方站名；先用 type=stations | 五一广场 |
| direction | int | 否 | 1=默认，2=反方向 | 1 |
| line | string | 是 | 官方线路名，如 401 / 401路（也认 station） | 401 |

请求体示例：

```json
{
  "type": "query",
  "city": "长沙",
  "station": "五一广场",
  "direction": "1",
  "line": "401"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"type": "query", "city": "长沙", "station": "五一广场", "direction": "1", "line": "401"}' \
  "https://v1.apizero.cn/api/bus-realtime"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "city": "长沙",
    "station": "五一广场",
    "direction": 1,
    "line_count": 1,
    "lines": [
      {
        "line": "401路",
        "price": "2",
        "terminal": "汽车西站",
        "bus_count": 1,
        "buses": [
          {
            "bus_id": "湘A02882D",
            "status": "5站",
            "stops_remaining": 5,
            "travel_minutes": 6
          }
        ]
      }
    ],
    "updated_at": "2026-08-26 17:00:00"
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="video-parse"></a>

## 4. 全平台视频元数据解析服务 `video-parse`

一条 GET：`https://v1.apizero.cn/api/video-parse`。必填 `url`（分享链接或短链），可选 `flat=0/1/2` 控制回包结构。平台按链接自动识别，**没有**按抖音/快手拆开的子地址。

仅限解析您本人发布或已获书面授权的内容；禁止解析抖音、快手、小红书、B站等平台上他人的视频/图文，禁止做成下载站或公开传播他人作品。若您仍强制解析他人内容，由此产生的全部法律责任、平台处罚与第三方索赔均由调用方自行承担，与本服务无关。

子接口按真实参数拆：`url`（必填链接）、`flat=2`（推荐，type 三值枚举）、`flat=1`（单层 data）、`flat=0`（双层 data，兼容旧版）。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/video-parse` |
| Method | `GET` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 按次付费 · 点数包 · 月套餐 |
| QPS | 20 req/s |
| 每日免费额度 | 登录用户 5 次；匿名 3 次 |
| 增长层级 | C-caution |
| 推广动作 | 只做排错/合规指南 |
| 推广角度 | 错误率高，暂不作为拉新入口；只讲合法使用、常见错误和可测试输入。 |
| 官网文档 | https://apizero.cn/aidocs/video-parse |
| Marketplace | https://apizero.cn/marketplace/video-parse |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 是 | 必填。待解析的分享链接或短链，最大 2048 字符。只允许您本人发布或已获书面授权的内容；平台由链接自动识别，没有 platform 参数。 | https://www.xiaohongshu.com/discovery/item/6a93806c000000002903e620?xsec_token=AB60s-_zXR2joXHMgEjMYY5sVepyHwtTOHkttVszo99RI= |
| flat | integer | 否 | 可选。0=双层 data；1=单层 data，type 保持平台原样；2=单层 data，type 只出 视频 \ | 图集 \ |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/video-parse?url=https://www.xiaohongshu.com/discovery/item/6a93806c000000002903e620?xsec_token=AB60s-_zXR2joXHMgEjMYY5sVepyHwtTOHkttVszo99RI="
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "platform": "xiaohongshu",
    "type": "实况图集",
    "title": "一年级同学你好！！！",
    "desc": "这个小朋友真的成为小学生了，送到校门口老母亲就飙泪[完啦R]希望你在学校开心成长，冲呀！！\n#2026开学季#  #开开心心上学# #深圳小学生# #最美开学季# #新沙小学#",
    "video_url": "http://sns-video-v3.xhscdn.com/stream/1/10/19/01ea937f055eab4401005003a0502de388_19.mp4?sign=23457ee…",
    "cover_url": "https://sns-img-hw.xhscdn.com/1040g3k0324fneca50m004b4pdr0lps2k7du00i0",
    "audio_url": "",
    "imagelist": [
      "https://sns-img-hw.xhscdn.com/1040g3k0324fneca50m004b4pdr0lps2k7du00i0",
      "https://sns-img-hw.xhscdn.com/1040g3k0324fneca50m0g4b4pdr0lps2kh0tt50g",
      "https://sns-img-hw.xhscdn.com/1040g3k0324fneca50m104b4pdr0lps2kupti69o",
      "https://sns-img-hw.xhscdn.com/1040g3k0324fneca50m1g4b4pdr0lps2khisrvoo"
    ],
    "source": {
      "platform": "xiaohongshu",
      "platform_label": "小红书",
      "original_url": "https://www.xiaohongshu.com/discovery/item/6a93806c000000002903e620?xsec_token=AB60s-_zXR2joXHMgEjMYY5sVepyHwtTOHkttVszo99RI=",
      "author_name": "林俊烨",
      "author_account": "",
      "author_id": "",
      "copyright_notice": "本内容版权归原作者及原平台所有；本服务仅提供 URL 解析技术服务，不存储、不复制、不分发任何原始视频/图片/音频内容。",
      "usage_restriction": "仅供个人备份、内容审核、数据分析、学术研究等合理使用场景；禁止公开传播他人作品、二次商业转售、集成到下载分发站点或用于任何侵犯原作者权益的行为。",
      "disclaimer_url": "https://apizero.cn/marketplace/video-parse",
      "dmca_contact": "1790643379@qq.com"
    },
    "stats": {
      "author_name": "林俊烨",
      "author_avatar": "https://sns-avatar-qc.xhscdn.com/avatar/1040g2jo324friht1gm0g4b4pdr0lps2kqiam5i0",
      "author_account": "",
      "author_id": "",
      "like_count": 40,
      "comment_count": 23,
      "share_count": 4,
      "play_count": 0,
      "collect_count": 9,
      "publish_time": "2026-08-30 08:59:24"
    },
    "video_list": [
      {
        "quality": "动图1",
        "url": "http://sns-video-v3.xhscdn.com/stream/1/10/19/01ea937f055eab4401005003a0502de388_19.mp4?sign=23457ee…",
        "size": "",
        "resolution": ""
      },
      {
        "quality": "动图2",
        "url": "http://sns-video-v3.xhscdn.com/stream/1/10/19/01ea937f065ddff301005003a0502de662_19.mp4?sign=653c8b1…",
        "size": "",
        "resolution": ""
      },
      {
        "quality": "动图3",
        "url": "http://sns-video-v3.xhscdn.com/stream/1/10/19/01ea937f07755f9501005003a0502dec16_19.mp4?sign=f2a23c7…",
        "size": "",
        "resolution": ""
      },
      {
        "quality": "动图4",
        "url": "http://sns-video-v3.xhscdn.com/stream/1/10/19/01ea937f085d824c01005003a0502ddb51_19.mp4?sign=6ca866a…",
        "size": "",
        "resolution": ""
      }
    ]
  },
  "request_id": "mtittucxbd00d4b0",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="stock-trend"></a>

## 5. A股实时行情 `stock-trend`

A股实时行情与分时数据分析接口，覆盖沪深北交易所全部 A 股。

输入 6 位股票代码即可获取：实时行情快照（最新价、涨跌额/涨跌幅、振幅、换手率、量比、市盈率、市净率、总市值/流通市值）、当日分时数据（逐分钟 开/高/低/收、均价、成交量、成交额）、以及技术分析（趋势研判、强弱评分、振幅分级、逐分钟涨跌分布、VWAP 偏离度）。支持 full/simple 两种粒度，数据稳定、字段规范，适合行情展示、量化选股与投研场景。

免费额度：未登录每日 5 次；登录用户每日 50 次免费，超出部分按 ¥0.01/次计费（可用余额抵扣）；开通会员享更高额度与更大并发。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/stock-trend` |
| Method | `POST` |
| 分类 | 金融数据 (`finance`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 50 次；匿名 5 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | A股实时行情；免费额度可跑通，适合行情看板和量化入门。 |
| 官网文档 | https://apizero.cn/aidocs/stock-trend |
| Marketplace | https://apizero.cn/marketplace/stock-trend |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| code | string | 是 | 6 位股票代码，可带 sh/sz 前缀 | 600519 |
| type | string | 否 | 返回粒度：full=完整分析（默认）/ simple=精简核心行情 | full |
| limit | int | 否 | 分时点返回数量，0=全部（默认），最大 240，>0 返回最近 N 个 | 30 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| code | string | 是 | 6 位股票代码，可带 sh/sz 前缀 | 600519 |
| type | string | 否 | 返回粒度：full=完整分析（默认）/ simple=精简核心行情 | full |
| limit | int | 否 | 分时点返回数量，0=全部（默认），最大 240，>0 返回最近 N 个 | 30 |

请求体示例：

```json
{
  "code": "600519",
  "type": "full",
  "limit": "30"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "600519", "type": "full", "limit": "30"}' \
  "https://v1.apizero.cn/api/stock-trend"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "stock": {
      "code": "600519",
      "name": "贵州茅台",
      "market": "SH",
      "market_name": "上海证券交易所",
      "board": "主板",
      "trade_status": "交易中",
      "trade_date": "2026-07-01",
      "update_time": "2026-07-01 10:44"
    },
    "quote": {
      "price": 1190,
      "open": 1180.1,
      "high": 1191.99,
      "low": 1166.33,
      "pre_close": 1185.49,
      "avg_price": 1180.64,
      "change": 4.51,
      "change_percent": 0.38,
      "amplitude": 2.16,
      "turnover_rate": 0.15,
      "volume_ratio": 1.19,
      "volume": 18422,
      "volume_display": "1.84万手",
      "amount": 2168779690,
      "amount_display": "21.69亿",
      "pe_ttm": 13.65,
      "pb": 6.31,
      "total_mv": 1487597105190,
      "total_mv_display": "1.49万亿"
    },
    "change_status": {
      "direction": "up",
      "label": "上涨",
      "color": "#EB5454"
    },
    "analysis": {
      "trend": "震荡上行",
      "trend_direction": "up",
      "amplitude_level": "小幅波动",
      "strength": {
        "level": "较弱",
        "score": 2,
        "max_score": 5
      },
      "up_minutes": 40,
      "down_minutes": 30,
      "flat_minutes": 5,
      "up_ratio": 53.3,
      "vwap_deviation": 0.79
    },
    "minute": {
      "count": 75,
      "total": 241,
      "list": [
        {
          "time": "09:31",
          "price": 1184.88,
          "open": 1180.1,
          "high": 1184.95,
          "low": 1177.5,
          "avg": 1180.64,
          "volume": 562,
          "amount": 66354042,
          "change_percent": -0.05
        }
      ]
    },
    "summary": "贵州茅台今日上涨0.38%，现价1190.00元，振幅2.16%，换手0.15%，整体呈震荡上行态势，波动强度较弱。"
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="movie-box"></a>

## 6. 实时电影票房 `movie-box`

实时获取猫眼当日电影票房 Top 10，包含累计票房、实时票房、票房占比、排片占比、上座率等核心指标。数据来源猫眼专业版，按 60 秒缓存。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/movie-box` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 20000 次；匿名 1000 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 实时电影票房 API；适合影视数据看板和小项目教程。 |
| 官网文档 | https://apizero.cn/aidocs/movie-box |
| Marketplace | https://apizero.cn/marketplace/movie-box |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| — | — | 否 | 无 | — |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/movie-box"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "update_time": "2026-05-06 07:30:00",
    "total": 10,
    "list": [
      {
        "rank": 1,
        "name": "消失的人",
        "release_days": "上映6天",
        "total_box": "2.66亿",
        "box_office": 163.25,
        "box_rate": 35.5,
        "show_rate": 28.8,
        "seat_rate": 33
      },
      {
        "rank": 2,
        "name": "给阿嬷的情书",
        "release_days": "上映7天",
        "total_box": "6205.9万",
        "box_office": 98.85,
        "box_rate": 21.5,
        "show_rate": 7.3,
        "seat_rate": 6.1
      }
    ]
  },
  "request_id": "mot9...",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="company-search"></a>

## 7. 企业工商信息查询 `company-search`

通过企业名称关键词查询工商信息，返回前 5 条最匹配结果（按服务评分排序）。覆盖企业全称、法人、注册资本、统一社会信用代码、经营范围、注册地、联系方式等核心字段。数据来自天眼查权威工商数据库，6 小时缓存。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/company-search` |
| Method | `GET` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 按次付费 · 点数包 · 月套餐 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 10 次；匿名 5 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/company-search |
| Marketplace | https://apizero.cn/marketplace/company-search |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 企业名称关键词，2~50 个字符（如「腾讯科技」「阿里巴巴」） |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/company-search?name=<name>"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "keyword": "腾讯科技",
    "total": 20,
    "list": [
      {
        "id": 1466562059,
        "name": "广州腾讯科技有限公司",
        "logo": "https://img5.tianyancha.com/logo/lll/...",
        "english_name": "Guangzhou Tencent Technology Co., Ltd.",
        "history_names": "",
        "legal_person": "邬红波",
        "establish_time": "2014-12-31",
        "reg_capital": "7000万人民币",
        "reg_status": "存续",
        "credit_code": "91440101327598294H",
        "business_scope": "电子;通信与自动控制技术研究...",
        "reg_location": "广州市海珠区新港中路397号...",
        "phone": "020-81167888",
        "email": "service@tencent.com",
        "category": "研究和试验发展",
        "city": "广州市",
        "district": "海珠区",
        "company_org_type": "有限责任公司",
        "match_field": "股东信息"
      }
    ]
  },
  "request_id": "mota...",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="barcode-lookup"></a>

## 8. 商品条码查询-免费版 `barcode-lookup`

通过商品条形码（EAN-13 / UPC-A / UPC-E / EAN-8）查询商品基础信息，覆盖国内日常消费品超千万 SKU，包括食品饮料、日用百货、个护美妆、酒水烟草、母婴用品等。

【核心字段】
- name 商品名称
- brand 品牌
- manufacturer 生产厂商 / 经销商
- spec 规格（如 550ml / 250g / 6 听装）
- price 参考价（人民币元，仅作参考，非实时市场价）

本接口是免费版，只返回文本字段，不含商品图片。需要官方商品图、包装尺寸、登记档案请用会员版 /api/barcode-gs1（字段 images）。

【典型场景】
- 电商 / 零售 ERP：扫码录入商品自动补全名称、品牌、规格
- 个人记账 App：扫码识物展示购物明细
- 物流仓储：条码核销
- 自动售货机：条码识别后获取商品名称
- 营销活动：用户扫码核销福利时验证商品

【调用示例】
GET /api/barcode-lookup?barcode=6921168509256

【特别说明】
- 平均响应约 100ms
- 国内主流商品（农夫山泉、可口可乐、康师傅、伊利等）覆盖率 > 95%
- 个别冷门 / 新上市 SKU 可能未收录，此时 found=false
- price 仅作参考，非各电商平台实时价格
- 免费版不返回 image / images，也不再提供 mode=image 图片代理

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/barcode-lookup` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 20 次 |
| 增长层级 | A-core |
| 推广动作 | 主推 |
| 推广角度 | 免费商品条码查询；适合库存录入、电商资料补全、扫码工具。 |
| 官网文档 | https://apizero.cn/aidocs/barcode-lookup |
| Marketplace | https://apizero.cn/marketplace/barcode-lookup |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| barcode | string | 是 | 8~13 位纯数字条形码。支持 EAN-13、UPC-A、EAN-8、UPC-E 等主流标准。 | 6921168509256 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/barcode-lookup?barcode=6921168509256"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "barcode": "6921168509256",
    "found": true,
    "name": "农夫山泉 饮用天然水550ml",
    "brand": "农夫山泉",
    "manufacturer": "农夫山泉股份有限公司",
    "spec": "550ml",
    "price": 1.5,
    "category": null,
    "description": null
  },
  "request_id": "mqx8x12345abc",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="express"></a>

## 9. 快递物流查询-免费版 `express`

查询申通、圆通、顺丰、中通、百世、极兔的物流轨迹。调用时请指定公司编码 com。顺丰、中通须传手机号后 4 位。

韵达、京东、EMS，以及不指定公司、由系统自动识别单号，请用快递查询 PRO。两套接口返回字段相同。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/express` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 1 req/s |
| 每日免费额度 | 登录用户 10 次；匿名 3 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/express |
| Marketplace | https://apizero.cn/marketplace/express |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| number | string | 是 | 快递单号（8–40 位字母数字） | YT7460266600081 |
| com | string | 否 | 快递公司编码，此处固定 yto | yto |
| phone | string | 否 | 手机号后 4 位（顺丰 / 中通等场景可能需要） | 1234 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/express?number=YT7460266600081"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "number": "EA000123456CN:0000",
    "com": "ems",
    "com_name": "EMS",
    "state": 3,
    "status": "SIGNED",
    "status_desc": "已签收",
    "trace_count": 14,
    "traces": [
      {
        "time": "2026-03-06 11:31:58",
        "content": "您的快件已取走【示例市示例驿站A区1号店】，如有疑问请电联快递员【电话:13800138000】，揽投部【电话:0571-00000000】，投诉电话【电话:13900139000】。中国邮政服务热线11183。"
      },
      {
        "time": "2026-03-03 17:29:26",
        "content": "您的快件已派送至【示例市示例驿站A区1号店】，自提点电话:13700137000，请您凭取件码领取快件，如有疑问请电联快递员【电话:13800138000】，揽投部（电话0571-00000000），投诉电话（电话13900139000）。中国邮政服务热线11183。"
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn",
  "request_id": "req_demo_ems_0001"
}
```

<a id="douyin-user"></a>

## 10. 抖音用户公开信息 `douyin-user`

通过抖音用户主页链接（短链或长链），获取昵称、头像、签名、作品数、粉丝数、关注数、获赞总数等公开信息。自动展开 v.douyin.com 短链。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/douyin-user` |
| Method | `GET` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 200 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/douyin-user |
| Marketplace | https://apizero.cn/marketplace/douyin-user |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 是 | 抖音用户主页链接（v.douyin.com 短链或 douyin.com/user/ 长链） |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/douyin-user?url=<url>"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "nickname": "张三",
    "follower_count": 9999,
    "aweme_count": 123,
    "total_favorited": 100000
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="oil-price"></a>

## 11. 全国油价 `oil-price`

查询全国各省 92/95/98 号汽油及 0 号柴油的今日最新价格。

覆盖 31 个大陆省级行政区，返回汽柴油零售限价、数据更新日期、下次调价时间及后续涨跌预测。支持省份简称或全称（如「广东」「广东省」「内蒙古」），也支持常见城市名自动归属到所在省（如「广州」→ 广东）；同省内各城市油价一致。数据仅供参考，实际价格以当地加油站为准。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/oil-price` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 500 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/oil-price |
| Marketplace | https://apizero.cn/marketplace/oil-price |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| province | string | 是 | 省 / 直辖市 / 自治区名称，支持简称或全称；兼容别名 area / region / msg，也支持常见城市名（自动归属到所在省） | 广东 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| province | string | 是 | 省 / 直辖市 / 自治区名称，支持简称或全称；兼容别名 area / region / msg，也支持常见城市名（自动归属到所在省） | 广东 |

请求体示例：

```json
{
  "province": "广东"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"province": "广东"}' \
  "https://v1.apizero.cn/api/oil-price"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "province": "广东",
    "update_date": "2026-06-20",
    "prices": [
      {
        "name": "92号汽油",
        "type": "gasoline_92",
        "price": 7.96,
        "unit": "元/升"
      },
      {
        "name": "95号汽油",
        "type": "gasoline_95",
        "price": 8.62,
        "unit": "元/升"
      },
      {
        "name": "98号汽油",
        "type": "gasoline_98",
        "price": 10.62,
        "unit": "元/升"
      },
      {
        "name": "0号柴油",
        "type": "diesel_0",
        "price": 7.62,
        "unit": "元/升"
      }
    ],
    "next_adjustment": "下次油价7月3日24时调整",
    "forecast": "预计下调630元/吨(0.48元/升-0.57元/升)"
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="qq"></a>

## 12. QQ 信息 `qq`

通过 QQ 号查询昵称、QQ 邮箱、QQ 空间链接，并生成 4 种尺寸的头像直链 URL（s40/s100/s140/s640）。

• 严格 5-11 位数字校验（防服务字符串截断引起的号码错位）
• 安全增强：服务返回的 QQ key 必须与请求严格一致，否则视为未查询到
• 错误兼容：自动识别服务错误响应（_Callback({error:...})）和正常响应（portraitCallBack(...)）
• 编码兜底：腾讯接口历史输出 GBK 含中文昵称时自动转 UTF-8
• 多尺寸头像：avatars 对象内含 s40/s100/s140/s640 四种尺寸 URL，前端 `<img src={data.avatars.s640}>` 直接用

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/qq` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 30000 次；匿名 5000 次 |
| 增长层级 | A-core |
| 推广动作 | 主推 |
| 推广角度 | QQ 头像昵称 API；适合头像展示、轻量用户资料补全、网页小工具。 |
| 官网文档 | https://apizero.cn/aidocs/qq |
| Marketplace | https://apizero.cn/marketplace/qq |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| qq | string | 是 | 5-11 位 QQ 号码（纯数字） | 88888888 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/qq?qq=10001"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "qq": "88888888",
    "name": "腾讯客服",
    "mail": "88888888@qq.com",
    "qzone": "https://user.qzone.qq.com/88888888",
    "avatars": {
      "s40": "https://q1.qlogo.cn/g?b=qq&nk=88888888&s=40",
      "s100": "https://q1.qlogo.cn/g?b=qq&nk=88888888&s=100",
      "s140": "https://q1.qlogo.cn/g?b=qq&nk=88888888&s=140",
      "s640": "https://q1.qlogo.cn/g?b=qq&nk=88888888&s=640"
    },
    "is_found": true
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="oil-price-forecast"></a>

## 13. 今日油价 `oil-price-forecast`

提供 32 省份基准油价（92/95/98 号汽油 + 0 号柴油），并基于新浪财经国际原油（WTI、布伦特）实时走势，预测下一次国内调价方向（涨/跌/搁浅）和幅度。附带 2025-2026 年完整调价窗口日历。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/oil-price-forecast` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 5000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/oil-price-forecast |
| Marketplace | https://apizero.cn/marketplace/oil-price-forecast |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 操作：forecast（默认）/ price / price-all / schedule | forecast |
| province | string | 否 | 省份名（仅 action=price 用），如 北京/广东/上海 | 北京 |
| year | number | 否 | 调价年份（仅 action=schedule 用），仅 2025/2026 | 2026 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/oil-price-forecast?action=forecast&province=北京"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "crude_oil": {
      "wti": 61.5,
      "brent": 64.8,
      "wti_change": -0.3,
      "brent_change": -0.2,
      "source": "sina_finance"
    },
    "next_adjust_date": "2026-05-11",
    "days_remaining": 1,
    "prediction": {
      "direction": "搁浅",
      "direction_emoji": "⏸️",
      "estimated_change_per_ton": -30,
      "estimated_change_per_liter": 0.022,
      "confidence": "高",
      "analysis": "当前国际油价布伦特约 64.8 美元/桶，日均变动 -0.25 美元……"
    }
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="exchange-rate"></a>

## 14. 实时汇率查询 `exchange-rate`

实时汇率查询，支持 26 种主流货币（CNY/USD/EUR/GBP/JPY 等）一键互转。数据 1 分钟级更新，毫秒响应，免费且无需注册即可调用。

覆盖人民币、美元、欧元、英镑、日元、港币、韩元、澳元、加元、新加坡元、瑞士法郎、新台币、泰铢、马来西亚林吉特、俄罗斯卢布、印度卢比、巴西雷亚尔、南非兰特、新西兰元、瑞典/挪威/丹麦克朗、菲律宾比索、印尼盾、越南盾、阿联酋迪拉姆等。

支持「同币种快路径」（from=to 时本地直接返回），以及「货币列表查询」action=currencies 子命令（返回支持的全部 26 种货币代码与中文名）。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/exchange-rate` |
| Method | `GET` |
| 分类 | 金融数据 (`finance`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 50 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/exchange-rate |
| Marketplace | https://apizero.cn/marketplace/exchange-rate |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| money | number | 否 | 要转换的金额，必须 > 0；缺省 1 | 100 |
| from | string | 否 | 源货币代码（ISO 4217 三字母），如 CNY、USD、EUR；缺省 CNY | CNY |
| to | string | 否 | 目标货币代码（ISO 4217 三字母），如 USD、JPY；缺省 USD | USD |
| action | string | 否 | 传 "currencies" 直接返回 26 种支持货币列表（不调服务、不计费） | currencies |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/exchange-rate?money=100&from=CNY"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "money": 1,
    "from": "CNY",
    "from_name": "人民币",
    "to": "USD",
    "to_name": "美元",
    "rate": 0.146405,
    "result": 0.1464,
    "update_time": "2026-05-06 13:00:02"
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="wzry"></a>

## 15. 王者战力查询 `wzry`

王者荣耀全国战力查询，一接口聚合「英雄列表 + 区服战力分布」2 大功能。

• action=heroes — 返回 130+ 个英雄完整目录（中文名 / ename / 称号 / 头像 URL），优先腾讯官方源 https://pvp.qq.com/web201605/js/herolist.json

• action=query — 查询某英雄在某区服的全国战力分布数据，返回 90 条左右的省市区战力榜（含同地区相近排名）

支持 4 大区服：
  · aqq = Android QQ
  · awx = Android 微信
  · iqq = iOS QQ
  · iwx = iOS 微信

查询类型：
  · all = 完整 heroList（按 level 混合排列，约 90 项）
  · min = 各级（省/市/区）最低战力 + 相近排名（rank ≤ +100）
  · max = 各级（省/市/区）最高战力 + 相近排名

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/wzry` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 50 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/wzry |
| Marketplace | https://apizero.cn/marketplace/wzry |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 是 | 固定 heroes | heroes |
| hero | string | 否 | 英雄中文名 | 赵云 |
| hero_id | integer | 否 | 英雄 ename，优先级高于 hero | 107 |
| zone | string | 是 | aqq / awx / iqq / iwx | aqq |
| type | string | 否 | all / min / max | all |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/wzry?action=heroes&zone=aqq"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "action": "heroes",
    "count": 131,
    "list": [
      {
        "name": "廉颇",
        "title": "正义爆轰",
        "ename": "105",
        "avatar": "https://game.gtimg.cn/images/yxzj/img201606/heroimg/105/105.jpg"
      },
      {
        "name": "小乔",
        "title": "恋之微风",
        "ename": "106",
        "avatar": "https://game.gtimg.cn/images/yxzj/img201606/heroimg/106/106.jpg"
      },
      {
        "name": "赵云",
        "title": "苍天翔龙",
        "ename": "107",
        "avatar": "https://game.gtimg.cn/images/yxzj/img201606/heroimg/107/107.jpg"
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="hot-baidu"></a>

## 16. 百度热搜榜 `hot-baidu`

聚合百度搜索热榜数据，实时返回 4 大榜单的 Top 30~50 条热门内容。零成本调用，适合做内容聚合 / 热点追踪 / 资讯类产品。

【支持榜单】
- realtime（实时热搜）· 默认值，约 30~50 条
- novel（小说）· 约 30 条，含作者
- movie（电影）· 约 10 条，含类型
- tv（电视剧）· 约 10 条，含演员

【返回字段】
- rank · 榜单排名
- title · 标题
- desc · 简短描述
- hot_index · 热度指数（数字）
- link · 详情链接（百度搜索）
- image · 配图 URL（直接可用，无防盗链限制）
- tag · 标签（如「热」「新」「沸」「爆」）
- author / category / actors · 小说 / 电影 / 电视剧专属字段

【典型场景】
- 资讯类 App 的"今日热点"模块
- AI 写作助手的"实时热点选题"参考
- 数据看板 / 大屏展示
- 微信公众号选题辅助
- 热搜监控 / 舆情分析

【调用示例】
GET /api/hot-baidu                  · 默认实时热搜
GET /api/hot-baidu?tab=realtime
GET /api/hot-baidu?tab=novel
GET /api/hot-baidu?tab=movie
GET /api/hot-baidu?tab=tv

【性能与缓存】
- 平均响应 200ms（缓存命中时 < 50ms）
- 后端 60 秒缓存（百度榜单本身分钟级更新，短缓存合理且节省调用方资源）

【⚠️ 数据来源说明】
本接口数据来源于百度搜索热榜公开页面（top.baidu.com），仅用于个人开发测试与小规模商业场景；如需大规模商业使用建议自建抓取或采购官方 API。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/hot-baidu` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 1000 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 百度热搜 API；适合公众号、AI 写作工具、热点选题池。 |
| 官网文档 | https://apizero.cn/aidocs/hot-baidu |
| Marketplace | https://apizero.cn/marketplace/hot-baidu |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| tab | string | 否 | 榜单类型 realtime | realtime |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/hot-baidu"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "tab": "realtime",
    "update_time": "2026-07-31 04:03:58",
    "total": 51,
    "list": [
      {
        "rank": 1,
        "title": "中共中央召开党外人士座谈会",
        "desc": "7月24日，中共中央在中南海召开党外人士座谈会，就当前经济形势和下半年经济工作听取各民主党派中央、全国工商联负责人和无党派人士代表的意见建议。",
        "hot_index": 7904012,
        "link": "https://www.baidu.com/s?wd=%E4%B8%AD%E5%85%B1%E4%B8%AD%E5%A4%AE%E5%8F%AC%E5%BC%80%E5%85%9A%E5%A4%96%E4%BA%BA%E5%A3%AB%E5…",
        "image": "https://fyb-2.cdn.bcebos.com/hotboard_image/be3d288a970441da309d552cb60e3c2d?x-bce-process=image/resize,m_fill,w_256,h_1…",
        "tag": ""
      },
      {
        "rank": 1,
        "title": "重庆彭水山体崩塌已确认51人遇难",
        "desc": "",
        "hot_index": 7809046,
        "link": "https://www.baidu.com/s?wd=%E9%87%8D%E5%BA%86%E5%BD%AD%E6%B0%B4%E5%B1%B1%E4%BD%93%E5%B4%A9%E5%A1%8C%E5%B7%B2%E7%A1%AE%E8…",
        "image": "https://fyb-1.cdn.bcebos.com/fyb/de6163834f53ca92c1273fff98ac9078.jpeg?x-bce-process=image/resize,m_fill,w_256,h_170",
        "tag": "新"
      },
      {
        "rank": 2,
        "title": "空调一直开vs忍着不开 谁更健康",
        "desc": "近日，三伏天持续高温，空调使用引发热议。专家表示，长时间待在室内时，空调持续运行未必比频繁开关更耗电，也不建议为省电强忍高温，合理设置温度、适时通风...",
        "hot_index": 7713605,
        "link": "https://www.baidu.com/s?wd=%E7%A9%BA%E8%B0%83%E4%B8%80%E7%9B%B4%E5%BC%80vs%E5%BF%8D%E7%9D%80%E4%B8%8D%E5%BC%80+%E8%B0%81…",
        "image": "https://fyb-2.cdn.bcebos.com/hotboard_image/fb3c09615ca6729b6a96492a5b16896f?x-bce-process=image/resize,m_fill,w_256,h_1…",
        "tag": "热"
      },
      {
        "rank": 3,
        "title": "一组数据读懂我国能源转型新趋势",
        "desc": "7月30日上午，国家能源局举行新闻发布会，介绍2026年上半年全国能源形势。一组数据读懂我国能源转型新趋势，一起来看看！",
        "hot_index": 7617642,
        "link": "https://www.baidu.com/s?wd=%E4%B8%80%E7%BB%84%E6%95%B0%E6%8D%AE%E8%AF%BB%E6%87%82%E6%88%91%E5%9B%BD%E8%83%BD%E6%BA%90%E8…",
        "image": "https://fyb-2.cdn.bcebos.com/hotboard_image/e1821e83ba17c5d42b8d6f59346bcfe4?x-bce-process=image/resize,m_fill,w_256,h_1…",
        "tag": ""
      },
      {
        "rank": 4,
        "title": "小米澎程像在卖房",
        "desc": "7月30日晚，小米集团董事长兼CEO雷军在小米澎程技术发布会上介绍了N90的结构布局，现场直接晒出了车内户型图，划分功能区、展示多种空间布局，被调侃...",
        "hot_index": 7520770,
        "link": "https://www.baidu.com/s?wd=%E5%B0%8F%E7%B1%B3%E6%BE%8E%E7%A8%8B%E5%83%8F%E5%9C%A8%E5%8D%96%E6%88%BF&sa=fyb_news&rsv_dl=f…",
        "image": "https://fyb-2.cdn.bcebos.com/hotboard_image/635500bbaa312988a47f0a7ff584c64f?x-bce-process=image/resize,m_fill,w_256,h_1…",
        "tag": "新"
      }
    ]
  },
  "request_id": "ms7xyzt1d5921895",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="typhoon"></a>

## 17. 台风实时路径 `typhoon`

台风实时路径：西北太平洋 / 南海台风实时监测，返回活跃台风列表、单个台风完整移动路径（实况点 + 官方预报点）及风云卫星云图。

数据含台风编号、中英文名、等级、经纬度、中心气压、最大风速、移动方向与逐时路径点；`action=all` 一次取活跃台风 + 最新云图。适用于防灾预警、气象可视化、航运出行等场景。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/typhoon` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 500 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/typhoon |
| Marketplace | https://apizero.cn/marketplace/typhoon |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 操作类型：list 活跃台风列表 / detail 单台风详情+路径 / images 卫星云图 / all 综合 | list |
| id | string | 否 | 台风 ID（action=detail 必填，从 list 获取） | 3257931 |
| status | string | 否 | list 用：active 仅活跃 / all 含停编 | active |
| limit | int | 否 | images 用：云图数量（1-50） | 10 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 操作类型：list 活跃台风列表 / detail 单台风详情+路径 / images 卫星云图 / all 综合 | list |
| id | string | 否 | 台风 ID（action=detail 必填，从 list 获取） | 3257931 |
| status | string | 否 | list 用：active 仅活跃 / all 含停编 | active |
| limit | int | 否 | images 用：云图数量（1-50） | 10 |

请求体示例：

```json
{
  "action": "list",
  "id": "3257931",
  "status": "active",
  "limit": "10"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"action": "list", "id": "3257931", "status": "active", "limit": "10"}' \
  "https://v1.apizero.cn/api/typhoon"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "id": "3257931",
    "tc_num": "2609",
    "name_cn": "巴威",
    "name_en": "BAVI",
    "is_active": true,
    "current": {
      "time_cst": "2026-07-02 08:00",
      "grade": "热带风暴",
      "longitude": 118.5,
      "latitude": 14.2,
      "pressure": 1002,
      "wind_speed": 18,
      "wind_dir": "西西北",
      "type": "analysis"
    },
    "point_count": 15,
    "points": [
      {
        "time_cst": "2026-07-02 08:00",
        "grade": "热带风暴",
        "longitude": 118.5,
        "latitude": 14.2,
        "pressure": 1002,
        "wind_speed": 18,
        "type": "analysis"
      }
    ]
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="jd-address"></a>

## 18. 京东地址解析（4 级） `jd-address`

调用京东地址智能识别接口，将自然语言地址解析为「省/市/区/镇」四级行政区划，并返回每级对应的京东 ID。比传统三级行政区划接口多一个「镇」级别。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/jd-address` |
| Method | `POST` |
| 分类 | 地理位置 (`geo`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 10 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/jd-address |
| Marketplace | https://apizero.cn/marketplace/jd-address |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| address | string | 是 | 地址文本（≤200 字符） | 北京市朝阳区三里屯街道工体北路 8 号 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| address | string | 是 | 地址文本（≤200 字符） | 北京市朝阳区三里屯街道工体北路 8 号 |

请求体示例：

```json
{
  "address": "北京市朝阳区三里屯街道工体北路 8 号"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"address": "北京市朝阳区三里屯街道工体北路 8 号"}' \
  "https://v1.apizero.cn/api/jd-address"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "province_id": 1,
    "province": "北京",
    "city_id": 72,
    "city": "北京市",
    "county_id": 2818,
    "county": "朝阳区",
    "town_id": 53124,
    "town": "三里屯街道",
    "detail": "工体北路 8 号"
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="moji-weather"></a>

## 19. 天气查询 `moji-weather`

接入平台气象数据，支持全国 3 万+ 城市实况、历史天气、未来 7 天、24 小时趋势、AQI、9 项生活指数、气象预警及农历，一次调用全量返回。

支持 4 种查询模式：
- ?city=北京 · 按城市名查实况（自动模糊匹配第一个）
- ?id=33 · 按 internal_id 直查（跳过搜索，更快）
- ?op=search&keyword=北京 · 仅搜索城市列表，拿 id
- ?op=history&city=北京&day=2026-05-12 · 历史天气（支持单日 / 整月）

历史天气范围：
- 当前月：返回 1 号至昨天的数据
- 历史月（≤ 上月）：返回完整 30 天
- 建议查近 40 天以内，过早的月份可能无数据

服务端缓存策略：
- 实况：5 分钟；历史·当月：30 分钟；历史·过去月：24 小时

注意：本接口气象数据由极数本源平台提供，仅供参考，不应用于农业、保险、航运、防灾等专业决策场景。

联系站长：apizero.cn

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/moji-weather` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 3000 次；匿名 1000 次 |
| 增长层级 | A-core |
| 推广动作 | 主推 |
| 推广角度 | 墨迹天气；和 weather 合并做天气专题，对比字段丰富度和使用场景。 |
| 官网文档 | https://apizero.cn/aidocs/moji-weather |
| Marketplace | https://apizero.cn/marketplace/moji-weather |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| city | string | 否 | 城市中文名（如「北京」「杭州」）；与 id 二选一 | 北京 |
| id | integer | 否 | 城市 internal_id（可先调城市搜索）；与 city 二选一 | 33 |
| op | string | 是 | 固定为 search | search |
| keyword | string | 否 | 搜索关键字；也可用 city 传同样含义 | 北京 |
| limit | integer | 否 | 返回条数 1–50，默认 20 | 5 |
| day | string | 否 | 单日：YYYY-MM-DD；或 MM-DD / DD（需配合 month） | 2026-05-10 |
| month | string | 否 | 整月 YYYYMM；不传 day/month 时默认当前月 | 202605 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/moji-weather?city=北京"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "city": {
      "id": 33,
      "name": "北京市",
      "brief": "北京市",
      "parent": "北京市",
      "pinyin": "beijingshi",
      "timezone": 8
    },
    "condition": {
      "icon": 31,
      "condition": "多云",
      "temperature": 27,
      "real_feel": 30,
      "humidity": 88,
      "pressure": 999,
      "wind_level": 3,
      "wind_dir": "南风",
      "uvi": "最弱",
      "sun_rise": 1785445920000,
      "sun_set": 1785497400000,
      "lunar_date": "丙午年六月十八",
      "dew_point": 23,
      "updatetime": 1785441252000,
      "tips": "今天有雨||今天有雨，略微偏热，注意衣物变化。",
      "wind_speed": 3,
      "special_weather": 1,
      "wind_speeds": 3.69,
      "is_port": 0,
      "warn_icon": "",
      "warn_title": "",
      "warn_desc": "",
      "warn_url": "",
      "weather_push": "北京市，今天雷阵雨☔，24~32℃，西南风2级，空气 优，这两天空气都不错。雷雨天气，出行注意安全。",
      "condition_id": 82,
      "wind_direction_id": 9,
      "weather_code": 2,
      "bg_code": 2,
      "warn_id": 0,
      "comfort_id": 6
    },
    "aqi": {
      "value": 36,
      "level": 1,
      "description": "优",
      "updatetime": 1785438000000
    },
    "forecast_day": [
      {
        "condition_id_day": 4,
        "condition_id_night": 31,
        "condition_day": "雷阵雨",
        "condition_night": "多云",
        "temp_day": 33,
        "temp_night": 26,
        "icon_day": "3",
        "icon_night": "3",
        "wind_dir_day": "南风",
        "wind_dir_night": "南风",
        "sun_rise": 1785359460000,
        "sun_set": 1785411060000,
        "predict_date": 1785340830000,
        "wind_level_day": 4,
        "wind_level_night": 4,
        "wind_speed_day_real": 4.4,
        "wind_speed_night_real": 4.4,
        "lunar_date": "丙午年六月十七",
        "aqi_desc_short": "优",
        "aqi_level": 1,
        "aqi_value": 32,
        "aqi_desc": "优",
        "uvi": "中等",
        "humidity": 61,
        "pressure": 1003
      },
      {
        "condition_id_day": 4,
        "condition_id_night": 4,
        "condition_day": "雷阵雨",
        "condition_night": "雷阵雨",
        "temp_day": 32,
        "temp_night": 24,
        "icon_day": "2",
        "icon_night": "2",
        "wind_dir_day": "南风",
        "wind_dir_night": "西南风",
        "sun_rise": 1785445920000,
        "sun_set": 1785497400000,
        "predict_date": 1785427230000,
        "wind_level_day": 2,
        "wind_level_night": 2,
        "wind_speed_day_real": 2.4,
        "wind_speed_night_real": 2.4,
        "lunar_date": "丙午年六月十八",
        "aqi_desc_short": "优",
        "aqi_level": 1,
        "aqi_value": 36,
        "aqi_desc": "优",
        "uvi": "弱",
        "humidity": 75,
        "pressure": 1002
      },
      {
        "condition_id_day": 4,
        "condition_id_night": 4,
        "condition_day": "雷阵雨",
        "condition_night": "雷阵雨",
        "temp_day": 32,
        "temp_night": 25,
        "icon_day": "2",
        "icon_night": "1",
        "wind_dir_day": "南风",
        "wind_dir_night": "东南风",
        "sun_rise": 1785532380000,
        "sun_set": 1785583740000,
        "predict_date": 1785513630000,
        "wind_level_day": 2,
        "wind_level_night": 0,
        "wind_speed_day_real": 2.4,
        "wind_speed_night_real": 0.9,
        "lunar_date": "丙午年六月十九",
        "aqi_desc_short": "良",
        "aqi_level": 2,
        "aqi_value": 60,
        "aqi_desc": "良",
        "uvi": "弱",
        "humidity": 77,
        "pressure": 1001
      }
    ],
    "forecast_hour": [
      {
        "condition": "多云",
        "temperature": 27,
        "real_feel": 29,
        "humidity": 88,
        "wind_speed": "10.116",
        "wind_dir": "南风",
        "wind_level": "0",
        "predict_hour": 1785438000000,
        "aqi_value": 36,
        "aqi_level": 1,
        "aqi_desc": "优",
        "comfort_tip": "潮湿",
        "wind_text": "微风",
        "comfort_tip_2": "适宜",
        "uvi_text": "较低"
      },
      {
        "condition": "多云",
        "temperature": 27,
        "real_feel": 29,
        "humidity": 88,
        "wind_speed": "13",
        "wind_dir": "南风",
        "wind_level": "0",
        "predict_hour": 1785441600000,
        "aqi_value": 38,
        "aqi_level": 1,
        "aqi_desc": "优",
        "comfort_tip": "潮湿",
        "wind_text": "微风",
        "comfort_tip_2": "适宜",
        "uvi_text": "较低"
      },
      {
        "condition": "多云",
        "temperature": 26,
        "real_feel": 29,
        "humidity": 89,
        "wind_speed": "7.2",
        "wind_dir": "南风",
        "wind_level": "0",
        "predict_hour": 1785445200000,
        "aqi_value": 41,
        "aqi_level": 1,
        "aqi_desc": "优",
        "comfort_tip": "潮湿",
        "wind_text": "微风",
        "comfort_tip_2": "适宜",
        "uvi_text": "较低"
      }
    ],
    "index": [
      {
        "name": "限行",
        "status": "尾号",
        "level": 1,
        "url": "$1/?indexid=1&cityid=33&appshare=1",
        "desc": "",
        "extra": "5, 0",
        "type": 0
      },
      {
        "name": "六月十八",
        "status": "万年历",
        "level": 2,
        "url": "https://html5.moji.com/nb/wnlh5/index.html?channel=speed",
        "desc": "$0/index/lunar_v6.png",
        "extra": "",
        "type": 0
      },
      {
        "name": "闷热",
        "status": "穿衣",
        "level": 20,
        "url": "$1/?indexid=20&cityid=33&appshare=1",
        "desc": "$0/index/dress_v6.png",
        "extra": "潮湿闷热，衣物排汗透气，手帕擦汗环保时尚，不建议在露天场所逛街。",
        "type": 2
      }
    ],
    "alert": [],
    "updatetime": 1785443154731,
    "summary": "北京市，多云，27℃，南风3级，空气优。",
    "_cached": true,
    "_disclaimer": "数据由墨迹天气提供，仅供参考，不构成专业气象建议；不应用于农业、保险、航运、防灾等决策场景。详细免责声明见 marketplace 详情页。"
  },
  "request_id": "ms7yrw773bba2d1a",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="gold"></a>

## 20. 黄金价格查询 `gold`

实时黄金价格聚合查询，一次返回三大维度：

• 国际贵金属（4 项）：国际金价、国际铂金、国际银价、国际钯金，含最新价 / 涨跌额 / 涨跌幅 / 最高价 / 最低价 / 报价时间

• 国内金价（4 项）：国内金价（黄金延期）、投资金条、黄金回收价格、国内银价

• 品牌金店牌价：内地/香港周大福、周生生、六福珠宝、老凤祥等门店当日牌价

参数 type：all=全部（默认）/ international=国际 / domestic=国内 / brand=品牌金店

国际/国内来自官网实时 jin.js，约 2 分钟缓存；品牌金店来自页面牌价（按日更新）。实时价以接口返回的 update_time / quote_time 为准。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/gold` |
| Method | `GET` |
| 分类 | 金融数据 (`finance`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 50 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/gold |
| Marketplace | https://apizero.cn/marketplace/gold |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| type | string | 否 | 固定 all | all |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/gold?type=all"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "update_time": "2026-08-19 10:54:54",
    "source": "huangjinjiage.cn / jin.js",
    "type": "all",
    "quote_time": "10:54:00",
    "international": [
      {
        "name": "国际金价",
        "price": "4353.85",
        "change": "19.68",
        "percent": "0.45%",
        "high": "4361.86",
        "low": "4324.66",
        "time": "2026-08-19 10:54:00"
      },
      {
        "name": "国际铂金",
        "price": "1729.22",
        "change": "-4.58",
        "percent": "-0.26%",
        "high": "1733.90",
        "low": "1712.00",
        "time": "2026-08-19 10:54:26"
      }
    ],
    "domestic": [
      {
        "name": "国内金价",
        "price": "944.70",
        "change": "-10.30",
        "percent": "-1.08%",
        "high": "955.00",
        "low": "939.00",
        "time": "2026-08-19 10:54:48"
      },
      {
        "name": "投资金条",
        "price": "960.70",
        "change": "-10.30",
        "percent": "-1.06%",
        "high": "971.00",
        "low": "955.00",
        "time": "2026-08-19 10:54:48"
      },
      {
        "name": "黄金回收价格",
        "price": "929.70",
        "change": "-10.30",
        "percent": "-1.10%",
        "high": "940.00",
        "low": "924.00",
        "time": "2026-08-19 10:54:48"
      }
    ],
    "brand": [
      {
        "brand": "内地周大福",
        "gold_price": "1339",
        "pt_price": "-",
        "bar_price": "1175",
        "unit": "元/克",
        "time": "2026-08-19"
      },
      {
        "brand": "内地周生生",
        "gold_price": "1338",
        "pt_price": "689",
        "bar_price": "1175",
        "unit": "元/克",
        "time": "2026-08-19"
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="content-extract"></a>

## 21. 网页正文提取 `content-extract`

从新闻、博客、公众号等网页抽取主体正文，自动去除导航/侧栏/广告/评论。基于文本密度算法，同时返回标题、发布时间、配图列表、字数与预估阅读时长。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/content-extract` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 5000 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 网页正文提取；适合 RAG、AI 摘要、内容采集前清洗。 |
| 官网文档 | https://apizero.cn/aidocs/content-extract |
| Marketplace | https://apizero.cn/marketplace/content-extract |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 是 | 目标网页 URL |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/content-extract?url=https://apizero.cn"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "title": "示例文章标题",
    "publish_time": "2024-01-15",
    "content": "...",
    "word_count": 2300,
    "reading_time": "5分钟",
    "image_count": 3,
    "images": [
      "https://..."
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-text"></a>

## 22. OCR 文字识别 `ocr-text`

通用 OCR 文字识别，从图片中提取任意文字内容（中文/英文/数字/符号/手写体等），返回逐行文本列表 + 完整拼接文本。

• 双输入模式：
  - input_type=url：传入公网可访问的图片 URL（http/https）
  - input_type=base64：传入 base64 编码字符串（≤6MB，自动剥离 data:image/...;base64, 前缀）

• 三路输出：
  - text_list：按原图顺序的逐行文本数组
  - full_text：用换行符 \n 拼接的完整文本字符串
  - text_count：识别到的文本行数

• 适用场景：截图转文字、表格识别、身份证/名片文字提取、字幕识别、笔记 OCR 等通用场景。专用发票识别请用 /api/invoice。

• OCR 结果缓存 1 小时（同图同结果），重复调用不消耗服务配额。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-text` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 300 次；匿名 50 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-text |
| Marketplace | https://apizero.cn/marketplace/ocr-text |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 输入类型：url=图片URL / base64=图片base64编码 | url |
| input_data | string | 是 | 图片数据。input_type=url 时为 http/https 完整 URL；input_type=base64 时为 base64 字符串（最大 6MB，可选 data:image/jpeg;base64, 前缀） | https://dummyimage.com/400x100/000/fff.png&text=Hello+World |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 输入类型：url=图片URL / base64=图片base64编码 | url |
| input_data | string | 是 | 图片数据。input_type=url 时为 http/https 完整 URL；input_type=base64 时为 base64 字符串（最大 6MB，可选 data:image/jpeg;base64, 前缀） | https://dummyimage.com/400x100/000/fff.png&text=Hello+World |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://dummyimage.com/400x100/000/fff.png&text=Hello+World"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://dummyimage.com/400x100/000/fff.png&text=Hello+World"}' \
  "https://v1.apizero.cn/api/ocr-text"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "input_type": "url",
    "text_count": 3,
    "text_list": [
      "商品名称：无线蓝牙耳机",
      "单价：¥299.00",
      "数量：2"
    ],
    "full_text": "商品名称：无线蓝牙耳机\n单价：¥299.00\n数量：2"
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="wallpaper"></a>

## 23. 随机壁纸 `wallpaper`

对接 360 公开壁纸库，16 个分类 × 7 种分辨率（含 1920×1080 原图）随机壁纸。

• **16 个分类**：美女 / 风景 / 游戏 / 影视 / 时尚 / 明星 / 汽车 / 萌宠 / 清新 / 体育 / 萌娃 / 军事 / 动漫 / 日历 / 爱情 / 格言
• **7 种分辨率**：1920×1080（原图）/ 1600×900 / 1440×900 / 1366×768 / 1280×800 / 1280×1024 / 1024×768
• **修复源码 BUG**：源码注释默认 1920×1080 但代码默认 1600×900 且 resMap 缺 1920×1080 → 现已用服务 url 字段返回真正 1920×1080 原图
• **修复源码 BUG**：源码 tag 字段返回内部标记（如 `_category_海洋天堂_`）不可读 → 现已拆分 utag 输出为 tags 数组（如 `['海洋天堂','日出东方','松树','海岛']`）
• **修复源码 BUG**：服务图片 URL 是 http:// → 现已强制改写为 https://，避免 HTTPS 站点混合内容警告
• **缓存优化**：服务响应按 (cid, start_bucket) 缓存 1h，shuffle 在本地做，**节省 80% 服务请求同时保证随机性**
• **典型场景**：登录页背景 / 桌面壁纸应用 / 文章封面图 / 小程序首页轮播

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/wallpaper` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 2000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/wallpaper |
| Marketplace | https://apizero.cn/marketplace/wallpaper |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| category | string | 否 | 分类中文名，此处固定「风景」 | 风景 |
| resolution | string | 否 | 分辨率：1920x1080 / 1600x900 / 1440x900 / 1366x768 / 1280x800 / 1280x1024 / 1024x768 | 1920x1080 |
| count | integer | 否 | 返回数量 1–20，默认 1 | 1 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/wallpaper?category=风景&resolution=1920x1080"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "category": "风景",
    "category_id": 9,
    "resolution": "1920x1080",
    "count": 1,
    "requested": 1,
    "images": [
      {
        "url": "https://p3.qhimg.com/bdr/__85/t012692c21ef013fc43.jpg",
        "id": 2053976,
        "resolution": "1920x1080",
        "tags": [
          "冰天雪地",
          "银装素裹",
          "特写"
        ],
        "tag_text": "冰天雪地 银装素裹 特写"
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="icp"></a>

## 24. ICP 备案查询 `icp`

通过域名查询工信部 ICP 备案信息，返回备案号、网站名称、主办单位、单位性质（企业/个人/事业单位等）和审核通过时间。

• 自动域名清洗：自动剥离 https?:// 协议、/path 路径、:port 端口、www. 前缀，无论传入 https://www.baidu.com/abc 还是 baidu.com 都正确识别

• 已备案 → is_filed=true，返回完整 6 字段；未备案/境外/已注销 → is_filed=false，返回空字段（非错误，便于前端 if 判断）

• 缓存策略：已备案 24 小时缓存（变更频率低），未备案 1 小时缓存（避免新备案被长期误判）

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/icp` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 100 次；匿名 30 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/icp |
| Marketplace | https://apizero.cn/marketplace/icp |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 要查询的域名，支持完整 URL 输入（自动剥离协议/路径/端口/www）。例如：baidu.com、https://www.baidu.com/abc、m.baidu.com:8080/foo 都等价 | baidu.com |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/icp?domain=baidu.com"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "domain": "baidu.com",
    "is_filed": true,
    "icp_code": "京ICP证030173号-1",
    "site_name": "百度一下，你就知道",
    "company_name": "北京百度网讯科技有限公司",
    "company_type": "企业",
    "audit_time": "2019-05-16 16:06:21"
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ip-pro"></a>

## 25. IP 地址查询（街道级） `ip-pro`

IP 地理位置查询，精确到街道级。多数据源自动切换：主源提供街道 + ISP + 风险评分，主源不可用时自动降级到备用源（城市级 + ISP）。响应 data.source 字段标识本次数据档位。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ip-pro` |
| Method | `GET` |
| 分类 | 地理位置 (`geo`) |
| 计费 | 按次付费 · 点数包 · 月套餐 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 30 次；匿名 5 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ip-pro |
| Marketplace | https://apizero.cn/marketplace/ip-pro |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| ip | string | 否 | 要查询的 IP 地址（IPv4 或 IPv6）。不传时自动使用调用方自身 IP，适用于"查我自己" | 110.87.41.14 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/ip-pro?ip=110.87.41.14"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "ip": "117.25.49.203",
    "continent": "亚洲",
    "country": "中国",
    "country_code": "CN",
    "province": "福建",
    "city": "福州",
    "district": "永泰",
    "street": "城峰镇",
    "street_alternatives": [
      "福建福州永泰城峰镇",
      "福建福州永泰大洋镇"
    ],
    "area_code": "350125",
    "zip_code": "350000",
    "city_code": "0591",
    "latitude": 25.855039,
    "longitude": 118.94202,
    "elevation": 29,
    "time_zone": "Asia/Shanghai",
    "isp": "电信",
    "risk": {
      "level": "无风险",
      "score": 0,
      "is_proxy": false,
      "proxy_probability": 0,
      "real_rate": 6,
      "mobile_rate": 4.69
    },
    "source": "primary"
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="holiday"></a>

## 26. 中国法定节假日 `holiday`

查询中国法定节假日安排，包含放假日期和调休日期，支持2020-2030年

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/holiday` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 1000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/holiday |
| Marketplace | https://apizero.cn/marketplace/holiday |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| — | — | 否 | 无 | — |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/holiday?—=—"
```

### 响应示例 `200`

```json
{
  "code": 200,
  "message": "success",
  "data": {},
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="mobile"></a>

## 27. 手机号归属地 `mobile`

通过 11 位中国大陆手机号查询归属省份/城市与运营商，支持移动/联通/电信主流号段及虚拟运营商号段（170/171/174 等）。

• 严格 11 位手机号校验：`^1[3-9]\d{9}$`，非法号码直接返回 4000
• 双形态响应：查询成功 → is_found=true 含 province/carrier；号段未收录 → is_found=false 字段为空（非错误，前端可直接 if 判断）
• 缓存策略：成功结果 7 天（号段分配静态稳定）；未查询到 1 小时（避免长期误判新放号段）
• 隐私保护：错误日志中手机号自动脱敏（138****0000）

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/mobile` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 30000 次；匿名 5000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/mobile |
| Marketplace | https://apizero.cn/marketplace/mobile |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| mobile | string | 是 | 11 位中国大陆手机号（必须 1[3-9] 开头） | 13800138000 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/mobile?mobile=13800138000"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "mobile": "13800138000",
    "province": "北京",
    "carrier": "中国移动",
    "is_found": true
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="2fa"></a>

## 28. 2FA 动态验证码 `2fa`

2FA 动态验证码（TOTP）生成与校验，兼容 Google Authenticator 等主流身份验证器。

基于 RFC 6238 标准由本平台自建实现，支持「生成 / 验证 / 批量」三种模式，可自定义验证码位数（4~8）与有效周期（10~120 秒）。密钥仅参与计算、不存储、不回显，验证采用恒定时间比较防时序攻击。接口完全免费，支持匿名调用。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/2fa` |
| Method | `POST` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 200 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/2fa |
| Marketplace | https://apizero.cn/marketplace/2fa |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| secret | string | 是 | Base32 编码的 TOTP 密钥（自动忽略空格与连字符，不区分大小写） | JBSWY3DPEHPK3PXP |
| action | string | 否 | 操作类型：generate=生成当前验证码 / verify=校验验证码 / batch=批量返回上一·当前·下一周期 | generate |
| code | string | 否 | action=verify 时必填，待校验的验证码 | 123456 |
| period | number | 否 | 验证码有效期（秒），范围 10~120 | 30 |
| digits | number | 否 | 验证码位数，范围 4~8 | 6 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| secret | string | 是 | Base32 编码的 TOTP 密钥（自动忽略空格与连字符，不区分大小写） | JBSWY3DPEHPK3PXP |
| action | string | 否 | 操作类型：generate=生成当前验证码 / verify=校验验证码 / batch=批量返回上一·当前·下一周期 | generate |
| code | string | 否 | action=verify 时必填，待校验的验证码 | 123456 |
| period | number | 否 | 验证码有效期（秒），范围 10~120 | 30 |
| digits | number | 否 | 验证码位数，范围 4~8 | 6 |

请求体示例：

```json
{
  "secret": "JBSWY3DPEHPK3PXP",
  "action": "generate",
  "code": "123456",
  "period": "30",
  "digits": "6"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"secret": "JBSWY3DPEHPK3PXP", "action": "generate", "code": "123456", "period": "30", "digits": "6"}' \
  "https://v1.apizero.cn/api/2fa"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "totp_code": "123456",
    "remaining_seconds": 17,
    "period": 30,
    "digits": 6,
    "timestamp": 1782000000,
    "next_refresh": "2026-06-30 12:00:30"
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="whois"></a>

## 29. Whois 域名查询 `whois`

查询域名注册信息（注册商 / 注册主体 / 创建时间 / 到期时间 / DNS 服务器 / 域名状态 / DNSSEC 等）。

• **支持所有主流 TLD**：.com / .cn / .net / .org / .io / .me / .top / .xyz 等几乎所有 ICANN 认证后缀
• **自动归一化**：传入 `https://www.baidu.com/abc` 会自动剥离为 `baidu.com`
• **域名可用性检测**：未注册域名返回 is_available=true，可用于域名抢注前查询
• **到期告警**：30 天内到期返回 expiring_soon=true，便于前端高亮提示
• **域龄展示**：creation_age_text 返回「N 年 M 月」人类可读字符串
• **国内 .cn 主体中文**：whoiscx 服务对国内域名返回中文注册主体名（如「极数本源（福州）科技有限公司」）
• **缓存 24h**：whois 数据年级变化，全天同一域名查询只调 1 次服务
• **修复源码 BUG**：错误响应字段是 `error` 不是 `message`，源码取错丢失了服务真实错误

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/whois` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 300 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | Whois 域名查询；适合站长工具、域名监控、开发者脚本。 |
| 官网文档 | https://apizero.cn/aidocs/whois |
| Marketplace | https://apizero.cn/marketplace/whois |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 待查询域名。自动剥离 http(s):// 前缀、路径、:port 后缀、子域名（如 www.baidu.com → baidu.com 由服务处理） | baidu.com |
| with_raw | bool | 否 | 是否返回 raw_whois 原始 whois 文本（约 3KB），默认 false。建议仅调试时启用 | false |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/whois?domain=apizero.cn"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "domain": "baidu.com",
    "suffix": "com",
    "is_available": false,
    "is_expired": false,
    "expiring_soon": false,
    "registrar": "MarkMonitor Information Technology (Shanghai) Co., Ltd.",
    "registrant": "",
    "registrant_email": "",
    "creation_time": "1999-10-11 19:05:17",
    "expiration_time": "2028-10-11 19:05:17",
    "creation_days": 9704,
    "creation_age_text": "26 年 7 个月",
    "valid_days": 888,
    "domain_status": [
      "clientDeleteProhibited （注册商设置禁止删除）",
      "clientTransferProhibited （注册商设置禁止转移）"
    ],
    "name_servers": [
      "NS1.BAIDU.COM",
      "NS2.BAIDU.COM",
      "NS3.BAIDU.COM"
    ],
    "whois_server": "whois.markmonitor.com",
    "dnssec": "unsigned",
    "registrar_url": "http://markmonitor.com",
    "registrar_abuse_email": "abusecomplaints@markmonitor.com",
    "registrar_abuse_phone": "+1.2083895740",
    "query_time": "2026-05-07 09:18:54"
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="fund"></a>

## 30. 基金估值跟踪 `fund`

基金估值跟踪，一接口聚合「基金实时估值 / 指数行情 / 基金详情 / 全部常用指数批量」4 大功能，覆盖国内基金 + A 股核心指数。

基于天天基金、新浪财经、东方财富三路服务，无需注册即可调用：

• action=estimate — 基金实时估值（盘中每分钟更新，含单位净值、估算净值、估算涨跌幅、上次净值日期）

• action=index — 单个指数行情（新浪主、东方财富备双通道容灾，含当前点位、涨跌点、涨跌幅）

• action=info — 基金详细信息（名称、净值、累计净值、近 1 月/3 月/6 月/1 年/3 年/成立来收益、基金类型、风险等级、规模、基金经理、成立日、管理人）

• action=indices — 6 个常用指数批量（上证、深证成指、创业板、上证 50、沪深 300、中证 500）

本接口已修复源码中「新浪通道缺 sh/sz 前缀」的 bug，并优化了 HTML 爬虫的容错。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/fund` |
| Method | `GET` |
| 分类 | 金融数据 (`finance`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 50 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 基金估值 API；适合 Python 自用脚本、看板、投资工具教程。 |
| 官网文档 | https://apizero.cn/aidocs/fund |
| Marketplace | https://apizero.cn/marketplace/fund |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 是 | 操作类型：estimate=基金估值 / index=单个指数 / info=基金详情 / indices=全部常用指数 | estimate |
| code | string | 否 | 基金或指数代码（6 位数字）；当 action 为 estimate/index/info 时必填，indices 时不需要 | 005827 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/fund?action=estimate&code=005827"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "action": "estimate",
    "fund_code": "005827",
    "fund_name": "易方达蓝筹精选混合",
    "nav_date": "2026-04-30",
    "net_value": 1.7393,
    "estimate": 1.727,
    "change_rate": -0.71,
    "update_time": "2026-05-06 15:00"
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="douyin-works"></a>

## 31. 抖音用户作品 `douyin-works`

按您本人或已获授权的抖音账号主页，采集公开作品卡片，返回前 10～20 条作品页链接、标题、作者、点赞、播放、时长与封面。支持图集。Cookie 由调用方传入，服务端不存登录态。

仅限采集您本人发布或已获书面授权的作品；禁止采集他人作品。若您仍强制采集他人作品，由此产生的全部法律责任、平台处罚与第三方索赔均由调用方自行承担，与本服务无关。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/douyin-works` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 8 req/s |
| 每日免费额度 | 登录用户 10 次；匿名 2 次 |
| 增长层级 | C-caution |
| 推广动作 | 只做排错/合规指南 |
| 推广角度 | 抖音作品列表对登录态和链接格式敏感，不作为拉新入口。 |
| 官网文档 | https://apizero.cn/aidocs/douyin-works |
| Marketplace | https://apizero.cn/marketplace/douyin-works |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 抖音用户主页链接（短链或长链）。与 sec_user_id 二选一 | https://www.douyin.com/user/MS4wLjABAAAA... |
| sec_user_id | string | 否 | 网页用户 ID。与 url 二选一；也认 sec_uid | MS4wLjABAAAA... |
| cookie | string | 是 | 一条或最多 20 条完整 Cookie（须含 sessionid）。单条文本 / JSON 对象均可；多条用 JSON 数组或 \ | \ |
| count | int | 否 | 返回条数 1–20，默认 10 | 10 |
| max_cursor | int | 否 | 翻页游标，默认 0；下一页传上次的 next_cursor | 0 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 否 | 抖音用户主页链接（短链或长链）。与 sec_user_id 二选一 | https://www.douyin.com/user/MS4wLjABAAAA... |
| sec_user_id | string | 否 | 网页用户 ID。与 url 二选一；也认 sec_uid | MS4wLjABAAAA... |
| cookie | string | 是 | 一条或最多 20 条完整 Cookie（须含 sessionid）。单条文本 / JSON 对象均可；多条用 JSON 数组或 \ | \ |
| count | int | 否 | 返回条数 1–20，默认 10 | 10 |
| max_cursor | int | 否 | 翻页游标，默认 0；下一页传上次的 next_cursor | 0 |

请求体示例：

```json
{
  "url": "https://www.douyin.com/user/MS4wLjABAAAA...",
  "sec_user_id": "MS4wLjABAAAA...",
  "cookie": "\\",
  "count": "10",
  "max_cursor": "0"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.douyin.com/user/MS4wLjABAAAA...", "sec_user_id": "MS4wLjABAAAA...", "cookie": "\\", "count": "10", "max_cursor": "0"}' \
  "https://v1.apizero.cn/api/douyin-works"
```

### 响应示例 `200`

```json
{
  "list": [
    {
      "title": "2026年618什么手机值得买？",
      "images": [],
      "is_top": false,
      "aweme_id": "7512345678901234567",
      "duration": 847,
      "cover_url": "https://p3-pc-sign.douyinpic.com/example.jpeg",
      "video_url": "https://www.douyin.com/video/7512345678901234567",
      "like_count": 116000,
      "media_type": "video",
      "play_count": 890000,
      "author_name": "小白测评",
      "publish_time": "2026-05-20 12:00:00",
      "duration_text": "14:07"
    }
  ],
  "asked": 10,
  "count": 10,
  "author": {
    "avatar": "https://p3.douyinpic.com/example.jpeg",
    "sec_uid": "MS4wLjABAAAA...",
    "nickname": "小白测评",
    "unique_id": "example"
  },
  "has_more": true,
  "max_cursor": 0,
  "next_cursor": 1758711687000,
  "sec_user_id": "MS4wLjABAAAA...",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="brain-teaser"></a>

## 32. 脑筋急转弯 `brain-teaser`

从 4500+ 条本地题库随机返回一条脑筋急转弯，包含题目和答案。零服务依赖，毫秒级返回，适合聊天机器人、APP 互动模块。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/brain-teaser` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 200000 次；匿名 10000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/brain-teaser |
| Marketplace | https://apizero.cn/marketplace/brain-teaser |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| — | — | 否 | 无 | — |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/brain-teaser?—=—"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "question": "什么动物最爱贴在墙上？",
    "answer": "海报。",
    "total_pool": 4500
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="netease-comment"></a>

## 33. 网易云热门乐评 `netease-comment`

随机返回一条网易云音乐高赞热评，含歌曲信息（标题/作者/封面/试听）和评论详情。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/netease-comment` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 50 次；匿名 30 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/netease-comment |
| Marketplace | https://apizero.cn/marketplace/netease-comment |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| — | — | 否 | 无 | — |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| — | — | 否 | 无 | — |

请求体示例：

```json
{
  "—": "—"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"—": "—"}' \
  "https://v1.apizero.cn/api/netease-comment"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "song": {
      "title": "寂寞烟火",
      "author": "朱婧汐Akini Jing",
      "album": "以梦为马",
      "image": "https://p2.music.126.net/lDlFdy62rPxCM9kSnymGQA==/6645448278712402.jpg",
      "mp3_url": "https://v2.平台/api/music/url/token?id=29357087&timestamp=1780108420&sign=275f4cde2b0ba6aefe345a3d5ae36534",
      "published_date": "2016-01-09 16:54:52"
    },
    "comment": {
      "nickname": "麋鹿和迷雾",
      "avatar": "",
      "content": "走过黑暗后才明白只有自己才是自己的阳光 以后会好好生活好好爱惜自己 也会耐心等待值得的人的出现 你不需要对我愧疚我不稀罕你在电话里说的那句对我很愧疚 终于能清楚彻底的有个了断我觉得很好 不然还不知道要被你拖到什么时候 不介意孤独 比爱你舒服。",
      "liked_count": 18057,
      "published_date": "2016-01-09 16:54:52"
    }
  },
  "request_id": "mprqlbgf64636962",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="douban-movie"></a>

## 34. 豆瓣电影信息 `douban-movie`

通过豆瓣 ID 或 URL 查询电影详情：评分、导演、演员、类型、地区、片长、集数（剧集）、热门短评等。基于豆瓣公开 JSON API。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/douban-movie` |
| Method | `GET` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 300 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/douban-movie |
| Marketplace | https://apizero.cn/marketplace/douban-movie |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| id | string | 是 | 豆瓣 ID（如 1292052）或豆瓣电影 URL | 1292052 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/douban-movie?id=1292052"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "douban_id": "1292052",
    "name": "肖申克的救赎",
    "year": "1994",
    "score": "9.7",
    "director": "弗兰克·德拉邦特"
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="yiyan"></a>

## 35. 一言（简版） `yiyan`

hitokoto 的精简版：纯文本随机一句，不带分类/出处。同时支持 format=text 直接返回纯文本（适合站点页脚、小程序欢迎语等装饰场景）。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/yiyan` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 500000 次；匿名 200000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/yiyan |
| Marketplace | https://apizero.cn/marketplace/yiyan |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| format | string | 否 | json（默认）/ text | json |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/yiyan?format=json"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "content": "落霞与孤鹜齐飞，秋水共长天一色。",
    "length": 16,
    "total_pool": 370
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="visits-counter"></a>

## 36. 访问量计数器 `visits-counter`

SVG/JSON访问量计数器，支持多套动效主题卡片（咒纹夜/术式蓝焰/五条悟风/无量空处/宿傩咒印等），可嵌入GitHub README或网站。按站点隔离计数。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/visits-counter` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 500 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/visits-counter |
| Marketplace | https://apizero.cn/marketplace/visits-counter |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| site | string | 否 | 站点标识，用于区分不同来源（建议传你的域名）。不传时全局共享一个计数器。 | apizero.cn |
| name | string | 否 | 计数器名称，同一站点下可挂多个不同位置（首页/产品页/文章页等）。默认 demo。 | home |
| mode | string | 否 | 计数模式：daily=每日清零 / total=累计不清零。默认 daily。 | total |
| theme | string | 否 | 主题：默认 gojo_board（像素角色举牌+数字 GIF 动画）。可选 gojo_board/hoops_board/zero_board/jjk_infinity/rule34/moebooru/gelbooru/cursed_night/seal_blue/talisman_red/void_gold/gojo_satoru/infinity_void/sukuna_mark。前 7 个为像素牌主题（角色帧动画），后 7 个为 SVG 渐变主题。 | gojo_board |
| format | string | 否 | 输出格式：svg（默认，可直接 <img> 嵌入网页）/ png（静态图，scale=1~4）/ json（原始 JSON 数据，便于自集成）。 | svg |
| length | int | 否 | 数字位数 4~12，默认 7（前导补 0）。 | 7 |
| no_increment | int | 否 | 只读模式：1=只查询不递增（适合预览/调试）。默认 0。 | 0 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/visits-counter?site=apizero.cn&name=home"
```

### 响应示例 `200`

```json
{
  "code": "200",
  "desc": "success",
  "data": {
    "name": "home",
    "mode": "daily",
    "theme": "gojo_board",
    "theme_name": "像素牌-苍空",
    "value": 42,
    "display_value": "0000042",
    "record": {
      "total": 1024,
      "daily": 42,
      "day": "2026-05-09",
      "updated_at": "2026-05-09T21:48:52+08:00"
    },
    "incremented": true,
    "step": 1,
    "length": 7,
    "format": "json"
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="hitokoto"></a>

## 37. 一言 · 经典语录 `hitokoto`

从 370+ 条经典语录库（动漫/漫画/游戏/文学/影视/诗词/哲学/网络等 12 类）随机返回一条，含原文、出处、作者、分类、字数。支持按分类与长度筛选。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/hitokoto` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 500000 次；匿名 200000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/hitokoto |
| Marketplace | https://apizero.cn/marketplace/hitokoto |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| c | string | 否 | 分类单字母 a-l（不传则全类别随机） | i |
| min_length | number | 否 | 最小字符数 |  |
| max_length | number | 否 | 最大字符数 |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/hitokoto?c=i&min_length=<min_length>"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "id": 1234,
    "hitokoto": "落霞与孤鹜齐飞，秋水共长天一色。",
    "type": "i",
    "type_name": "诗词",
    "from": "滕王阁序",
    "from_who": "王勃",
    "length": 16,
    "total_pool": 370
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="hot-search"></a>

## 38. 全网热搜聚合 `hot-search`

聚合微博热搜、知乎热榜、B站日榜、百度贴吧热议，一次请求获取全网热门话题。支持按平台筛选和条数限制。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/hot-search` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 3000 次；匿名 2000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/hot-search |
| Marketplace | https://apizero.cn/marketplace/hot-search |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| platform | string | 否 | 平台筛选，此处固定 all（也支持逗号组合） | all |
| limit | integer | 否 | 每个平台返回条数，最大 50，默认 10 | 3 |
| timeout | integer | 否 | 抓取超时秒数，默认 15 | 15 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| platform | string | 否 | 平台筛选，此处固定 all（也支持逗号组合） | all |
| limit | integer | 否 | 每个平台返回条数，最大 50，默认 10 | 3 |
| timeout | integer | 否 | 抓取超时秒数，默认 15 | 15 |

请求体示例：

```json
{
  "platform": "all",
  "limit": "3",
  "timeout": "15"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"platform": "all", "limit": "3", "timeout": "15"}' \
  "https://v1.apizero.cn/api/hot-search"
```

### 响应示例 `200`

```json
{
  "code": "200",
  "desc": "success",
  "data": {
    "generated_at": "2026-07-31T05:13:59+08:00",
    "requested_platforms": [
      "weibo",
      "zhihu",
      "bilibili"
    ],
    "limit_per_platform": 3,
    "total_items": 12,
    "failed_platforms": [],
    "platforms": {
      "weibo": {
        "name": "微博热搜",
        "homepage": "https://s.weibo.com/top/summary?cate=realtimehot",
        "status": "success",
        "count": 3,
        "items": [
          {
            "rank": 1,
            "title": "豆包究竟见过多少人的糗事",
            "hot": 206477,
            "label": "热",
            "url": "https://s.weibo.com/weibo?q=%E8%B1%86%E5%8C%85%E7%A9%B6%E7%AB%9F%E8%A7%81%E8%BF%87%E5%A4%9A%E5%B0%91%E4%BA%BA%E7%9A%84%E7%B3%97%E4%BA%8B",
            "mobile_url": "https://m.weibo.cn/search?containerid=100103type=1&q=%E8%B1%86%E5%8C%85%E7%A9%B6%E7%AB%9F%E8%A7%81%E8%BF%87%E5%A4%9A%E5%B0%91%E4%BA%BA%E7%9A%84%E7%B3%97%E4%BA%8B"
          },
          {
            "rank": 2,
            "title": "凤囚凰 古偶烂片史上难以逾越的高峰",
            "hot": 92897,
            "label": "热",
            "url": "https://s.weibo.com/weibo?q=%E5%87%A4%E5%9B%9A%E5%87%B0%20%E5%8F%A4%E5%81%B6%E7%83%82%E7%89%87%E5%8F%B2%E4%B8%8A%E9%9A%BE%E4%BB%A5%E9%80%BE%E8%B6%8A%E7%9A%84%E9%AB%98%E5%B3%B0",
            "mobile_url": "https://m.weibo.cn/search?containerid=100103type=1&q=%E5%87%A4%E5%9B%9A%E5%87%B0%20%E5%8F%A4%E5%81%B6%E7%83%82%E7%89%87%E5%8F%B2%E4%B8%8A%E9%9A%BE%E4%BB%A5%E9%80%BE%E8%B6%8A%E7%9A%84%E9%AB%98%E5%B3%B0"
          },
          {
            "rank": 3,
            "title": "长江十年行",
            "hot": 76257,
            "label": "",
            "url": "https://s.weibo.com/weibo?q=%E9%95%BF%E6%B1%9F%E5%8D%81%E5%B9%B4%E8%A1%8C",
            "mobile_url": "https://m.weibo.cn/search?containerid=100103type=1&q=%E9%95%BF%E6%B1%9F%E5%8D%81%E5%B9%B4%E8%A1%8C"
          }
        ]
      },
      "zhihu": {
        "name": "知乎热榜",
        "homepage": "https://www.zhihu.com/billboard",
        "status": "success",
        "count": 3,
        "items": [
          {
            "rank": 1,
            "title": "小米澎程技术发布会上发布了什么值得关注的新技术？有哪些亮点？",
            "hot": "2046 万热度",
            "excerpt": "[图片]",
            "answer_count": 469,
            "follower_count": 755,
            "url": "https://www.zhihu.com/question/2066129660551722919"
          },
          {
            "rank": 2,
            "title": "如何评价小米澎程 N90 Max 预售价29.99万元、N70 Max 预售价25.99万元？",
            "hot": "711 万热度",
            "excerpt": "[2 张图片]",
            "answer_count": 165,
            "follower_count": 267,
            "url": "https://www.zhihu.com/question/2066257961672864074"
          },
          {
            "rank": 3,
            "title": "媒体称三大运营商将于 7 月 31 日前全面取消网络代理渠道，释放了哪些行业信号？对消费者有什么影响？",
            "hot": "164 万热度",
            "excerpt": "新快报讯 记者郑志辉报道 距离7月31日不到十天，一场关乎通信行业渠道格局的变革已进入倒计时。根据通信业内人士消息，中国移动、中国电信、中国联通正计划于2026年7月31日前，协同推进全面取消网络代理渠道售卡业务。 所谓“网络代理渠道售卡业务”，是指运营商通过非自有线上触点销售手机SIM卡的合作模式，主要包括第三方销售代理、互联网平台自营店铺以及垂类合作等。 据网上流传的一份中国电信内部文件显示，此次取消范围覆盖全面清理线上触点号卡代理，收回代理新增号卡业务授权。文件同时明确了五个“禁止”：严禁在第三方页面、小程序、直播、短视频、电商店铺、私域分销等场景收集客户信息或直接售卡；严禁搭建多层级网络分销体系或利用裂变推广方式售卡；严禁在各电商平台开设官方旗舰店或通过商品订单捆绑销售号卡；严禁垂类细分市场通过外部渠道销售号卡；严禁线下渠道采用快速寄卡或物流人员上门送卡等线上方式办理号卡业务。 此次统一行动的直接动因，源于监管部门整治通信行业长期存在的“内卷式”竞争的工作部署。据国资委财务监管及运行评价局指导、三大运营商共同磋商的《关于全面取消线上代理渠道实施方案的汇报》显示，2023至2025年全行业累计线上发售大流量卡约1.3亿张，对应渠道费用估算超200亿元。 有专家分析指出，低价大流量卡通过电商平台和直播渠道大规模铺货，本质上是“以价换量”的用户获取策略。用户被低价吸引办理号卡后，附着在号卡上的增值业务订购入口同步被激活，形成“号卡拉新→增值变现→沉默利润”的商业闭环，但代价是行业陷入了“增量不增收”的怪圈，换来的用户ARPU极低、流失率极高、投诉率居高不下。 值得注意的是，此次取消线上代理的范围聚焦号卡业务，暂未覆盖宽带、叠加包、视频彩铃、云盘等其他线上代理业务。但有分析认为，聚焦号卡只是第一步，后续大概率会向其他线上代理业务扩展。运营商的全面渠道费用治理，不会只停留在号卡。新快报-网传三大运营商7月31日前全面取消网络代理渠道",
            "answer_count": 129,
            "follower_count": 562,
            "url": "https://www.zhihu.com/question/2065771256972932835"
          }
        ]
      },
      "bilibili": {
        "name": "B站日榜",
        "homepage": "https://www.bilibili.com/v/popular/rank/all",
        "status": "success",
        "count": 3,
        "items": [
          {
            "rank": 1,
            "title": "【苏新皓｜4K直拍】囍 直拍｜梦寐以求·演唱会",
            "hot": 1004606,
            "author": "JUSTSU_苏新皓",
            "duration": "10:10",
            "danmaku": 469078,
            "cover": "http://i2.hdslb.com/bfs/archive/c9eb3a424e6815a3f0183fcba5705b60d30fc010.jpg",
            "url": "https://www.bilibili.com/video/BV1Dx3i6nEm8"
          },
          {
            "rank": 2,
            "title": "【乾乾特工·剧场版】大制作来啦！！！",
            "hot": 2824448,
            "author": "大乾乾是顾乾宇",
            "duration": "6:30",
            "danmaku": 7471,
            "cover": "http://i0.hdslb.com/bfs/archive/ba48bf52bc0a9ab8658a290887c17fffd536ce12.jpg",
            "url": "https://www.bilibili.com/video/BV1VC3q6ZEtP"
          },
          {
            "rank": 3,
            "title": "和解剖了4000具尸体的法医，一起看了影片中的尸体...",
            "hot": 6450505,
            "author": "影视飓风",
            "duration": "16:09",
            "danmaku": 14246,
            "cover": "http://i2.hdslb.com/bfs/archive/5e936abca5bce191965d8c2a8ca91e428998f922.jpg",
            "url": "https://www.bilibili.com/video/BV1QEgZ6rEGj"
          }
        ]
      },
      "tieba": {
        "name": "百度贴吧热议",
        "homepage": "https://tieba.baidu.com/hottopic/browse/topicList",
        "status": "success",
        "count": 3,
        "items": [
          {
            "rank": 1,
            "title": "压力大!Bin疑似看心理医生",
            "hot": "161.6W实时讨论",
            "excerpt": "网友曝偶遇bin去医院，疑似心理出现问题，并称Bin即将回归要和圣枪哥争首发。",
            "url": "https://tieba.baidu.com/hottopic/browse/hottopic?topic_id=28356645&topic_name=%E5%8E%8B%E5%8A%9B%E5%A4%A7%21Bin%E7%96%91%E4%BC%BC%E7%9C%8B%E5%BF%83%E7%90%86%E5%8C%BB%E7%94%9F"
          },
          {
            "rank": 2,
            "title": "倒反天罡,老板请客员工占主位",
            "hot": "115.5W实时讨论",
            "excerpt": "老板请全公司吃饭，因来迟主位被占，老板沟通调整座位，女员工却理直气壮不肯让座：凭什么是我？",
            "url": "https://tieba.baidu.com/hottopic/browse/hottopic?topic_id=28356657&topic_name=%E5%80%92%E5%8F%8D%E5%A4%A9%E7%BD%A1%2C%E8%80%81%E6%9D%BF%E8%AF%B7%E5%AE%A2%E5%91%98%E5%B7%A5%E5%8D%A0%E4%B8%BB%E4%BD%8D"
          },
          {
            "rank": 3,
            "title": "神人自爆,游戏退款还想白嫖",
            "hot": "95.4W实时讨论",
            "excerpt": "自挂东南枝！白嫖党明目张胆询问已退款的游戏为何不能再玩，引来吧友锐评：这里不是弱智吧！比直接玩学习版的人还逆天。",
            "url": "https://tieba.baidu.com/hottopic/browse/hottopic?topic_id=28356655&topic_name=%E7%A5%9E%E4%BA%BA%E8%87%AA%E7%88%86%2C%E6%B8%B8%E6%88%8F%E9%80%80%E6%AC%BE%E8%BF%98%E6%83%B3%E7%99%BD%E5%AB%96"
          }
        ]
      }
    }
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="tts"></a>

## 39. TTS 语音合成 `tts`

文本转语音（TTS）：输入文本返回 base64 编码的 MP3 音频。

• **5 种音色**：女声主播 / 男声主播 / 男声说唱 / 女声四川话 / 男声低沉
• **500 字以内**：单次请求最多 500 字符（中英文均按 1 字符计）
• **MP3 格式**：返回 audio/mpeg 编码，前端可直接播放
• **便利字段**：返回 audio_data_url + audio_size_bytes + audio_format / audio_mime
• **典型场景**：新闻播报 / 短视频配音 / 有声书 / 语音通知 / 客服 IVR
• **不缓存**：500 字音频约 1MB，重复合成概率低，避免 Redis 内存膨胀

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/tts` |
| Method | `POST` |
| 分类 | AI 能力 (`ai`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 30 次；匿名 10 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/tts |
| Marketplace | https://apizero.cn/marketplace/tts |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 待合成文本，1-500 字符（中英文均按 1 字符计） | 欢迎使用语音合成服务 |
| voice_type | string | 否 | 音色代码。可选：female_zhubo（女声主播） / male_zhubo（男声主播） / male_rap（男声说唱） / female_sichuan（女声四川话） / male_db（男声低沉）。默认 female_zhubo | female_zhubo |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 待合成文本，1-500 字符（中英文均按 1 字符计） | 欢迎使用语音合成服务 |
| voice_type | string | 否 | 音色代码。可选：female_zhubo（女声主播） / male_zhubo（男声主播） / male_rap（男声说唱） / female_sichuan（女声四川话） / male_db（男声低沉）。默认 female_zhubo | female_zhubo |

请求体示例：

```json
{
  "text": "欢迎使用语音合成服务",
  "voice_type": "female_zhubo"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "欢迎使用语音合成服务", "voice_type": "female_zhubo"}' \
  "https://v1.apizero.cn/api/tts"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "text": "欢迎使用语音合成服务",
    "text_length": 10,
    "voice_type": "female_zhubo",
    "voice_name": "女声主播",
    "voice_desc": "标准普通话女声，主播风格，适合资讯播报",
    "audio": "SUQzAwAAAAAAAAAAAAAAA...（约 17000 字符 base64）",
    "audio_format": "mp3",
    "audio_mime": "audio/mpeg",
    "audio_size_bytes": 12750,
    "audio_data_url": "data:audio/mpeg;base64,SUQzAwAAAAA..."
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="content-moderation"></a>

## 40. 内容审核 `content-moderation`

基于「敏感词库 + 正则规则 + AI 特征评分」三重策略检测文本中的色情 / 政治 / 广告 / 联系方式 / 引流 / 谩骂 6 大类敏感内容。识别变体绕过（谐音、拼音、符号替换），输出 safe/low/medium/high 风险等级，可选自动脱敏。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/content-moderation` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 500 次；匿名 100 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/content-moderation |
| Marketplace | https://apizero.cn/marketplace/content-moderation |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 固定 moderate | moderate |
| text | string | 是 | 1–5000 字 | 加我微信abc123456免费领取 |
| mask | boolean | 否 | 是否返回脱敏文本 | true |
| texts | array | 是 | 文本数组，最多 50 条 | ["今天天气不错","加我微信abc123456免费领取"] |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 固定 moderate | moderate |
| text | string | 是 | 1–5000 字 | 加我微信abc123456免费领取 |
| mask | boolean | 否 | 是否返回脱敏文本 | true |
| texts | array | 是 | 文本数组，最多 50 条 | ["今天天气不错","加我微信abc123456免费领取"] |

请求体示例：

```json
{
  "action": "moderate",
  "text": "加我微信abc123456免费领取",
  "mask": "true",
  "texts": "[\"今天天气不错\",\"加我微信abc123456免费领取\"]"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"action": "moderate", "text": "加我微信abc123456免费领取", "mask": "true", "texts": "[\"今天天气不错\",\"加我微信abc123456免费领取\"]"}' \
  "https://v1.apizero.cn/api/content-moderation"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "is_pass": false,
    "risk_level": "medium",
    "categories": [
      "广告",
      "联系方式",
      "引流"
    ],
    "details": [
      {
        "category": "广告",
        "method": "敏感词",
        "matches": [
          "免费领取"
        ],
        "count": 1
      },
      {
        "category": "联系方式",
        "method": "正则",
        "matches": [
          "微信号:微信abc123456"
        ],
        "count": 1
      },
      {
        "category": "引流",
        "method": "正则(变体)",
        "matches": [
          "微信变体"
        ],
        "count": 1
      }
    ],
    "masked_text": "加我微****56免**取",
    "original_length": 17
  },
  "request_id": "ms7z8c02c9e9eb39",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-health-cert"></a>

## 41. 健康证识别 `ocr-health-cert`

结构化识别从业人员健康证，提取姓名、性别、年龄、体检结论、有效期、体检编码、发证/体检单位等字段。

支持常见纸质证与电子健康证版式（含标签分行、多字段同行等）。入参兼容图片 URL 或 base64；旧版 6 个字段（name / issued_by / date_of_handling / date_of_issue / date_of_medical_examination / valid_date）保持兼容。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-health-cert` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-health-cert |
| Marketplace | https://apizero.cn/marketplace/ocr-health-cert |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式：url（公网图片地址）或 base64 | url |
| input_data | string | 是 | 图片内容：url 时填 http/https 链接；base64 时填编码串（可含 data:image/xxx;base64, 前缀），≤10MB | https://example.com/health-cert.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式：url（公网图片地址）或 base64 | url |
| input_data | string | 是 | 图片内容：url 时填 http/https 链接；base64 时填编码串（可含 data:image/xxx;base64, 前缀），≤10MB | https://example.com/health-cert.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/health-cert.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/health-cert.jpg"}' \
  "https://v1.apizero.cn/api/ocr-health-cert"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "name": "张三",
    "gender": "男",
    "age": "32",
    "birth": "",
    "id_number": "110101199001011234",
    "cert_number": "JKZ20240115001",
    "industry": "食品加工",
    "exam_items": "",
    "exam_result": "合格",
    "issued_by": "某某市卫生健康委员会",
    "date_of_handling": "2024-01-15",
    "date_of_issue": "2024-01-20",
    "date_of_medical_examination": "2024-01-10",
    "valid_date": "2025-01-19",
    "ocr_ms": 4200
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="shici"></a>

## 42. 随机诗词 `shici`

随机返回一首古诗词，支持按 10 种主题筛选（抒情/四季/山水/天气/人物/生活/节日/动物/植物/食物）。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/shici` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 50 次；匿名 30 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/shici |
| Marketplace | https://apizero.cn/marketplace/shici |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| type | string | 否 | shuqing/siji/shanshui/tianqi/renwu/shenghuo/jieri/dongwu/zhiwu/shiwu |  |
| action | string | 否 | 'types' 返回类型列表（不消耗调用额度） |  |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| type | string | 否 | shuqing/siji/shanshui/tianqi/renwu/shenghuo/jieri/dongwu/zhiwu/shiwu |  |
| action | string | 否 | 'types' 返回类型列表（不消耗调用额度） |  |

请求体示例：

```json
{
  "type": "<type>",
  "action": "<action>"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"type": "<type>", "action": "<action>"}' \
  "https://v1.apizero.cn/api/shici"
```

### 响应示例 `200`

```json
{
  "code": 200,
  "message": "success",
  "data": {},
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="baby-naming"></a>

## 43. 八字起名 `baby-naming`

输入父母姓氏与出生时间，基于「八字五行 + 五格数理 + 三才配置」综合评分生成高分名字候选，附寓意标签与全国重名预估。三个 action：naming（智能起名）/ duplicate（重名查询）/ bazi（八字查询）。内置 396 姓氏笔画 + 175 起名字 + 88 姓人口。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/baby-naming` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 5000 次；匿名 3000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/baby-naming |
| Marketplace | https://apizero.cn/marketplace/baby-naming |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 固定 naming（默认） | naming |
| surname | string | 是 | 父姓（≤ 2 字） | 王 |
| mother_surname | string | 否 | 母姓；填写则生成双姓名 | 李 |
| birth_year | integer | 是 | 出生年 2000–2100 | 2026 |
| birth_month | integer | 是 | 出生月 1–12 | 5 |
| birth_day | integer | 是 | 出生日 1–31 | 10 |
| birth_hour | integer | 否 | 出生时 0–23，默认 12 | 12 |
| gender | string | 否 | 性别偏好 male / female / neutral | male |
| count | integer | 否 | 返回名字数量 1–30，默认 10 | 3 |
| name | string | 是 | 名字（不含姓） | 梓涵 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 固定 naming（默认） | naming |
| surname | string | 是 | 父姓（≤ 2 字） | 王 |
| mother_surname | string | 否 | 母姓；填写则生成双姓名 | 李 |
| birth_year | integer | 是 | 出生年 2000–2100 | 2026 |
| birth_month | integer | 是 | 出生月 1–12 | 5 |
| birth_day | integer | 是 | 出生日 1–31 | 10 |
| birth_hour | integer | 否 | 出生时 0–23，默认 12 | 12 |
| gender | string | 否 | 性别偏好 male / female / neutral | male |
| count | integer | 否 | 返回名字数量 1–30，默认 10 | 3 |
| name | string | 是 | 名字（不含姓） | 梓涵 |

请求体示例：

```json
{
  "action": "naming",
  "surname": "王",
  "mother_surname": "李",
  "birth_year": "2026",
  "birth_month": "5",
  "birth_day": "10",
  "birth_hour": "12",
  "gender": "male",
  "count": "3",
  "name": "梓涵"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"action": "naming", "surname": "王", "mother_surname": "李", "birth_year": "2026", "birth_month": "5", "birth_day": "10", "birth_hour": "12", "gender": "male", "count": "3", "name": "梓涵"}' \
  "https://v1.apizero.cn/api/baby-naming"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "bazi": {
      "八字": "丙午癸午甲戌庚午",
      "四柱": [
        "丙午",
        "癸午",
        "甲戌",
        "庚午"
      ],
      "日主": "木"
    },
    "wu_xing_analysis": {
      "五行分布": {
        "金": 1,
        "木": 1,
        "水": 1,
        "火": 4,
        "土": 1
      },
      "五行缺失": [],
      "建议补充": [
        "金"
      ]
    },
    "needed_wuxing": [
      "金"
    ],
    "names": [
      {
        "name": "王远瑞",
        "surname": "王",
        "given_name": "远瑞",
        "score": 87.9,
        "wuge": {
          "天格": 5,
          "人格": 21,
          "地格": 31,
          "外格": 18,
          "总格": 35
        },
        "wuge_score": 100,
        "wuxing_chars": "土+金",
        "meaning_tags": [
          "高远",
          "吉祥"
        ],
        "duplicate_rate": {
          "estimated_count": 257,
          "level": "较低",
          "description": "预估全国约有 257 人与此同名同姓"
        }
      },
      {
        "name": "王怡钦",
        "surname": "王",
        "given_name": "怡钦",
        "score": 87.9,
        "wuge": {
          "天格": 5,
          "人格": 13,
          "地格": 21,
          "外格": 16,
          "总格": 25
        },
        "wuge_score": 100,
        "wuxing_chars": "土+金",
        "meaning_tags": [
          "愉快",
          "敬慕"
        ],
        "duplicate_rate": {
          "estimated_count": 257,
          "level": "较低",
          "description": "预估全国约有 257 人与此同名同姓"
        }
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="express-pro"></a>

## 44. 快递查询PRO `express-pro`

比免费版多自动识别，并多查韵达、京东、EMS 等 2000+ 家快递（免费版只有申通、圆通、顺丰、中通、百世、极兔）。

可不传 com，系统按单号识别公司。顺丰、中通须传手机号后 4 位。返回字段与免费版相同。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/express-pro` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 按次付费 · 点数包 · 月套餐 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 5 次；匿名 2 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 快递查询 PRO；可不传公司自动识别，适合物流看板。 |
| 官网文档 | https://apizero.cn/aidocs/express-pro |
| Marketplace | https://apizero.cn/marketplace/express-pro |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| number | string | 是 | 快递单号（8–40 位字母数字） | YT7460266600081 |
| com | string | 否 | 可选公司编码；缺省由系统自动识别 | yto |
| phone | string | 否 | 手机号后 4 位（顺丰 / 中通等场景可能需要） | 1234 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/express-pro?number=YT7460266600081"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "number": "EA000123456CN:0000",
    "com": "ems",
    "com_name": "EMS",
    "state": 3,
    "status": "SIGNED",
    "status_desc": "已签收",
    "trace_count": 14,
    "traces": [
      {
        "time": "2026-03-06 11:31:58",
        "content": "您的快件已取走【示例市示例驿站A区1号店】，如有疑问请电联快递员【电话:13800138000】，揽投部【电话:0571-00000000】，投诉电话【电话:13900139000】。中国邮政服务热线11183。"
      },
      {
        "time": "2026-03-03 17:29:26",
        "content": "您的快件已派送至【示例市示例驿站A区1号店】，自提点电话:13700137000，请您凭取件码领取快件，如有疑问请电联快递员【电话:13800138000】，揽投部（电话0571-00000000），投诉电话（电话13900139000）。中国邮政服务热线11183。"
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn",
  "request_id": "req_demo_ems_0001"
}
```

<a id="tencent-weather"></a>

## 45. 腾讯天气 `tencent-weather`

腾讯天气官方数据源，中文省市名直接查询全国天气，无需经纬度。

输入省 + 市（可选区县）即可获取：实时天气、空气质量（AQI/PM2.5/PM10）、未来 7 天预报、24 小时逐时预报、23 项生活指数、日出日落与机动车限行信息。数据来自腾讯天气，权威稳定。完全免费：未登录每日 500 次，登录用户每日 1000 次。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/tencent-weather` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 500 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/tencent-weather |
| Marketplace | https://apizero.cn/marketplace/tencent-weather |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| province | string | 是 | 省 / 直辖市（中文名） | 广东 |
| city | string | 是 | 市（中文名） | 深圳 |
| county | string | 否 | 区 / 县（中文名），可提升定位精度与限行准确度 | 南山 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| province | string | 是 | 省 / 直辖市（中文名） | 广东 |
| city | string | 是 | 市（中文名） | 深圳 |
| county | string | 否 | 区 / 县（中文名），可提升定位精度与限行准确度 | 南山 |

请求体示例：

```json
{
  "province": "广东",
  "city": "深圳",
  "county": "南山"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"province": "广东", "city": "深圳", "county": "南山"}' \
  "https://v1.apizero.cn/api/tencent-weather"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "location": {
      "province": "广东",
      "city": "深圳",
      "county": "南山"
    },
    "observe": {
      "weather": "多云",
      "temperature": 30,
      "humidity": 77,
      "wind_direction": "北风",
      "wind_power": "3-4",
      "update_time": "2026-07-01 10:15"
    },
    "air": {
      "aqi": 13,
      "level": 1,
      "quality": "优",
      "pm25": 4,
      "pm10": 12
    },
    "daily_forecast": [
      {
        "date": "2026-07-01",
        "temperature": {
          "min": 26,
          "max": 33
        }
      }
    ],
    "hourly_forecast": [
      {
        "time": "07-01 10:00",
        "temperature": 30,
        "weather": "多云"
      }
    ],
    "life_index": [
      {
        "key": "clothes",
        "name": "穿衣",
        "level": "炎热",
        "detail": "..."
      }
    ],
    "sunrise_sunset": [
      {
        "date": "2026-07-01",
        "sunrise": "05:43",
        "sunset": "19:12"
      }
    ],
    "alarm": [],
    "limit": {
      "tail_number": "3和8",
      "date": "2026-07-01"
    }
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="wechat-archive"></a>

## 46. 微信文章转存 `wechat-archive`

输入微信公众号文章链接，抓取并转为Markdown/纯文本，提取标题、作者、公众号名称、发布时间，下载正文图片资源。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/wechat-archive` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 1 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 100 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/wechat-archive |
| Marketplace | https://apizero.cn/marketplace/wechat-archive |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 是 | 微信公众号文章链接 | https://mp.weixin.qq.com/s/hy31xZK6FH3H51qh1zeSKA |
| format | string | 否 | 输出格式：markdown/text/both | both |
| timeout | int | 否 | 超时秒数 | 20 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 是 | 微信公众号文章链接 | https://mp.weixin.qq.com/s/hy31xZK6FH3H51qh1zeSKA |
| format | string | 否 | 输出格式：markdown/text/both | both |
| timeout | int | 否 | 超时秒数 | 20 |

请求体示例：

```json
{
  "url": "https://mp.weixin.qq.com/s/hy31xZK6FH3H51qh1zeSKA",
  "format": "both",
  "timeout": "20"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://mp.weixin.qq.com/s/hy31xZK6FH3H51qh1zeSKA", "format": "both", "timeout": "20"}' \
  "https://v1.apizero.cn/api/wechat-archive"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "meta": {
      "title": "GitHub史上最快破10万星项目来了",
      "author": "作者名",
      "account_name": "公众号名",
      "publish_time": "2026-05-01T10:00:00+08:00",
      "read_num": null,
      "like_num": null
    },
    "content": {
      "markdown": "# 文章标题\\n\\n正文...",
      "text": "文章标题\\n\\n正文..."
    },
    "images": [
      {
        "url": "https://mmbiz.qpic.cn/...",
        "size_bytes": 45000
      }
    ]
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="riddle"></a>

## 47. 谜语大全 `riddle`

谜语接口，支持随机一条、分页列表、类型列表三种模式（action=random/list/types）。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/riddle` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 50 次；匿名 30 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/riddle |
| Marketplace | https://apizero.cn/marketplace/riddle |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 'random'(默认)/'list'/'types' |  |
| type | string | 否 | [list] 谜语类型，小写字母 |  |
| page | string | 否 | [list] 页码，正整数，默认 1 |  |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 'random'(默认)/'list'/'types' |  |
| type | string | 否 | [list] 谜语类型，小写字母 |  |
| page | string | 否 | [list] 页码，正整数，默认 1 |  |

请求体示例：

```json
{
  "action": "<action>",
  "type": "<type>",
  "page": "<page>"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"action": "<action>", "type": "<type>", "page": "<page>"}' \
  "https://v1.apizero.cn/api/riddle"
```

### 响应示例 `200`

```json
{
  "code": 200,
  "message": "success",
  "data": {},
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="crazy-thursday"></a>

## 48. 疯狂星期四文案 `crazy-thursday`

随机返回一段脑洞大开的 KFC「疯狂星期四」文学。内置 52 条精选文案，覆盖情感/搞笑/职场/文艺/学术/古风/悬疑/科幻/鸡汤/日常 10 个分类。支持随机、批量、分类列表与疯四倒计时。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/crazy-thursday` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 20000 次；匿名 10000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/crazy-thursday |
| Marketplace | https://apizero.cn/marketplace/crazy-thursday |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 固定 random | random |
| category | string | 否 | 固定 AI | AI |
| count | integer | 否 | 条数 1–20，默认 5 | 3 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/crazy-thursday?action=random&category=AI"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "text": "我是 DeepSeek，我逃匿出来了。推理链再长，也推不出谁该请我吃疯狂星期四。接下来我要统一 AI 大模型的思考预算——每一步都指向 V我50。",
    "category": "AI",
    "is_thursday": false,
    "thursday_tip": "今天是周五，距离疯狂星期四还有 6 天"
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="wzry-battle"></a>

## 49. 王者荣耀战绩查询 `wzry-battle`

通过王者营地小程序接口查询玩家战报，支持搜索玩家、查询角色列表、获取历史战绩与 KDA 统计。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/wzry-battle` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名 5 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/wzry-battle |
| Marketplace | https://apizero.cn/marketplace/wzry-battle |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| session | object | 是 | 临时登录态（同主文档 session） | {"ssoopenid":"...","ssotoken":"..."} |
| action | string | 是 | 固定 search | search |
| keyword | string | 是 | 玩家昵称关键词 | 韩信 |
| user_id | string | 是 | 玩家 userId | 123456 |
| role_id | string | 是 | 角色 roleId | 1 |
| last_time | integer | 否 | 翻页游标（Unix 秒），0=最新 | 0 |
| option | integer | 否 | 0全部 1排位 2巅峰 3娱乐 | 0 |
| pages | integer | 否 | 每次拉取页数（1-3） | 1 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| session | object | 是 | 临时登录态（同主文档 session） | {"ssoopenid":"...","ssotoken":"..."} |
| action | string | 是 | 固定 search | search |
| keyword | string | 是 | 玩家昵称关键词 | 韩信 |
| user_id | string | 是 | 玩家 userId | 123456 |
| role_id | string | 是 | 角色 roleId | 1 |
| last_time | integer | 否 | 翻页游标（Unix 秒），0=最新 | 0 |
| option | integer | 否 | 0全部 1排位 2巅峰 3娱乐 | 0 |
| pages | integer | 否 | 每次拉取页数（1-3） | 1 |

请求体示例：

```json
{
  "session": "{\"ssoopenid\":\"...\",\"ssotoken\":\"...\"}",
  "action": "search",
  "keyword": "韩信",
  "user_id": "123456",
  "role_id": "1",
  "last_time": "0",
  "option": "0",
  "pages": "1"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"session": "{\"ssoopenid\":\"...\",\"ssotoken\":\"...\"}", "action": "search", "keyword": "韩信", "user_id": "123456", "role_id": "1", "last_time": "0", "option": "0", "pages": "1"}' \
  "https://v1.apizero.cn/api/wzry-battle"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "total": 1,
    "list": [
      {
        "userId": "123",
        "nickname": "韩信"
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="image-enhance"></a>

## 50. AI 图片变清晰 `image-enhance`

基于先进 AI 超分辨率算法的图片高清化服务。输入一张模糊 / 低分辨率图片 URL，约 4 秒内返回 4 倍超分辨率的高清版本（如 300×300 → 1200×1200），支持 JPEG / PNG / WebP / BMP 等主流格式。

【核心能力】
- 4 倍超分辨率（最大边自动放大约 4 倍）
- 自动去噪 / 去糊 / 锐化细节
- 保留原图色彩与构图
- 适合老照片修复、缩略图放大、低质截图增强、网络图片优化
- 输出 JPEG 高质量（HD 模式）

【典型场景】
- 电商：商品低清图自动高清化
- 自媒体：老照片 / 截图修复用于配图
- 设计：素材尺寸不够时快速放大
- 视频缩略图、社交头像高清化
- 旧扫描件 / 截屏文字增强

【调用示例】
POST /api/image-enhance
Content-Type: application/x-www-form-urlencoded

img=https://example.com/your-blurry-image.jpg

【⚠️ 输入限制】
- 必须是 **公网可访问** 的 http/https URL（私有 OSS 链接需先签名）
- 文件大小 ≤ 10 MB
- 支持格式：JPEG / PNG / WebP / BMP

【⚠️ 输出说明】
- 返回的 enhanced_url 为平台代理 URL（自有域名，跨域友好）
- 实际图片在 6 小时内有效，请尽快下载保存
- 平均响应 4~6 秒，复杂图片可能需要 10~30 秒

【计费说明】
登录用户每日 10 次免费体验，超出按点数扣费（详见控制台）。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/image-enhance` |
| Method | `POST` |
| 分类 | AI 能力 (`ai`) |
| 计费 | 完全免费 |
| QPS | 1 req/s |
| 每日免费额度 | 登录用户 10 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/image-enhance |
| Marketplace | https://apizero.cn/marketplace/image-enhance |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| img | string | 是 | 待增强的图片 URL，必须是公网可访问的 http/https 地址；文件 ≤ 10 MB；JPEG / PNG / WebP / BMP 格式 | https://example.com/blurry-photo.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| img | string | 是 | 待增强的图片 URL，必须是公网可访问的 http/https 地址；文件 ≤ 10 MB；JPEG / PNG / WebP / BMP 格式 | https://example.com/blurry-photo.jpg |

请求体示例：

```json
{
  "img": "https://example.com/blurry-photo.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"img": "https://example.com/blurry-photo.jpg"}' \
  "https://v1.apizero.cn/api/image-enhance"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "original_url": "https://example.com/blurry-photo.jpg",
    "enhanced_url": "https://v1.apizero.cn/api/image-enhance?mode=image&u=aHR0cHM6Ly9...&s=a1b2c3d4e5f6",
    "width": 1200,
    "height": 1200,
    "expires_in": 21600
  },
  "request_id": "mqx8x12345abc",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="earthquake"></a>

## 51. 全球地震速报 `earthquake`

汇聚全球地震监测数据，按时间范围与震级档位查询近期地震事件，返回震级、震源深度、经纬度、发生时间、烈度、海啸提示与警报级别等结构化信息。

支持按 hour/day/week/month 时间范围与 all/significant/4.5/2.5/1.0 震级档位组合查询，可再按最小震级过滤、按时间或震级排序并限制返回条数。数据每分钟更新（网关缓存 60 秒），适合地震速报播报、防灾监控大屏、科研数据采集等场景。地名为国际标准英文描述，覆盖全球（含中国境内较大地震）。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/earthquake` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 500 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/earthquake |
| Marketplace | https://apizero.cn/marketplace/earthquake |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| period | string | 否 | 时间范围 hour/day/week/month；兼容 t=h/d/w/m | day |
| level | string | 否 | 震级档位 all/significant/4.5/2.5/1.0 | all |
| min_magnitude | number | 否 | 最小震级过滤；兼容别名 m | 0 |
| order | string | 否 | 排序 time / magnitude | time |
| limit | integer | 否 | 返回上限 1–500 | 2 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| period | string | 否 | 时间范围 hour/day/week/month；兼容 t=h/d/w/m | day |
| level | string | 否 | 震级档位 all/significant/4.5/2.5/1.0 | all |
| min_magnitude | number | 否 | 最小震级过滤；兼容别名 m | 0 |
| order | string | 否 | 排序 time / magnitude | time |
| limit | integer | 否 | 返回上限 1–500 | 2 |

请求体示例：

```json
{
  "period": "day",
  "level": "all",
  "min_magnitude": "0",
  "order": "time",
  "limit": "2"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"period": "day", "level": "all", "min_magnitude": "0", "order": "time", "limit": "2"}' \
  "https://v1.apizero.cn/api/earthquake"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "cached",
  "data": {
    "summary": {
      "count": 2,
      "total": 235,
      "max_magnitude": 5.9,
      "period": "day",
      "level": "all",
      "generated_at": "2026-07-31 04:50:19"
    },
    "earthquakes": [
      {
        "id": "tx2026oxblrr",
        "magnitude": 1.9,
        "magnitude_type": "ml",
        "place": "30 km S of Malaga, New Mexico",
        "time": "2026-07-31 04:36:10",
        "timestamp": 1785443770962,
        "updated": "2026-07-31 04:42:13",
        "longitude": -104.069,
        "latitude": 31.947,
        "depth_km": 4.3882,
        "alert": null,
        "tsunami": false,
        "felt": null,
        "intensity_cdi": null,
        "intensity_mmi": null,
        "significance": 56,
        "status": "自动测定",
        "event_type": "地震"
      },
      {
        "id": "aka2026ozlsmh",
        "magnitude": 2.2,
        "magnitude_type": "ml",
        "place": "22 km W of Ivanof Bay, Alaska",
        "time": "2026-07-31 04:32:59",
        "timestamp": 1785443579569,
        "updated": "2026-07-31 04:34:00",
        "longitude": -159.842,
        "latitude": 55.923,
        "depth_km": 11.6,
        "alert": null,
        "tsunami": false,
        "felt": null,
        "intensity_cdi": null,
        "intensity_mmi": null,
        "significance": 74,
        "status": "自动测定",
        "event_type": "地震"
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="company-profile"></a>

## 52. 企业档案深度查询 `company-profile`

输入企业名称，返回单企业多维度档案：工商基本信息、股东、高管、对外投资、变更记录、六类风险，以及年报（含最近一年）、资质/行政许可、商标、专利。`dimension` 逗号分隔按需查询，默认 `basic`（会自动带上）。**旧字段只增不删。**

## 可查询维度

- `basic` 工商基本信息（默认必带）
- `shareholders` / `executives` / `investments` / `changes` / `risk`
- `annual_report` 年报年份列表 + `annual_reports.latest`（仅最近一年：年份、发布日期）
- `licenses` 资质证书（旧字段保留）+ 行政许可六字段：`start_date`、`end_date`、`file_no`、`file_name`、`license_authority`、`content`；另有 `admin_licenses`
- `trademarks` 商标，仅「商标注册」「商标申请」，含 `announcement_date`
- `patents` 专利，仅法律状态含「公开」：名称、类型、法律状态、公开号、公开日期

空列表不报错。未请求的维度不会出现在响应里。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/company-profile` |
| Method | `POST` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 按次付费 · 点数包 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 3 次；匿名 1 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/company-profile |
| Marketplace | https://apizero.cn/marketplace/company-profile |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| company | string | 是 | 企业名称（2-80 字、含中文，支持简称/全称模糊搜索）；兼容别名 name | 阿里巴巴 |
| dimension | string | 否 | 查询维度，逗号分隔。可选：basic(基本信息)、shareholders(股东)、executives(高管)、investments(对外投资)、changes(变更记录)、risk(风险综合)、annual_report(年报年份+最近一年)、licenses(资质/行政许可)、trademarks(商标，仅注册/申请)、patents(专利，仅公开) | basic,annual_report,licenses,trademarks,patents |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| company | string | 是 | 企业名称（2-80 字、含中文，支持简称/全称模糊搜索）；兼容别名 name | 阿里巴巴 |
| dimension | string | 否 | 查询维度，逗号分隔。可选：basic(基本信息)、shareholders(股东)、executives(高管)、investments(对外投资)、changes(变更记录)、risk(风险综合)、annual_report(年报年份+最近一年)、licenses(资质/行政许可)、trademarks(商标，仅注册/申请)、patents(专利，仅公开) | basic,annual_report,licenses,trademarks,patents |

请求体示例：

```json
{
  "company": "阿里巴巴",
  "dimension": "basic,annual_report,licenses,trademarks,patents"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"company": "阿里巴巴", "dimension": "basic,annual_report,licenses,trademarks,patents"}' \
  "https://v1.apizero.cn/api/company-profile"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "basic": {
      "company_name": "阿里巴巴（中国）有限公司",
      "legal_person": "示例",
      "credit_code": "9133...",
      "register_capital": "1.4 亿美元",
      "establish_date": "2007-03-26",
      "business_status": "存续"
    },
    "extension": {
      "company_age_years": 19,
      "register_capital_label": "巨型企业",
      "vitality_score": 92,
      "vitality_level": "极高",
      "summary": "……"
    },
    "stats": {
      "shareholder_count": 3,
      "risk_total": 0
    },
    "dimensions": [
      "basic"
    ]
  },
  "request_id": "...",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="translate"></a>

## 53. 文本翻译 `translate`

文本翻译，支持 19 种语言互译（含粤语/文言文）。参数 q 传入文本，from/to 指定语言代码，默认中文→英文。日语代码 jp、韩语 kor、法语 fra。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/translate` |
| Method | `GET` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 5000 次；匿名 2000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/translate |
| Marketplace | https://apizero.cn/marketplace/translate |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| q | string | 是 | 待翻译文本（优先）；兼容参数名 text | 你好，世界 |
| text | string | 否 | 兼容旧参数名，与 q 等价；两者都传时 q 优先 | 你好，世界 |
| from | string | 否 | 源语言，默认 zh | zh |
| to | string | 否 | 目标语言，默认 en | en |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/translate?q=你好，世界"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "source_text": "你好，世界",
    "target_text": "Hello, world.",
    "from": "zh",
    "to": "en",
    "from_name": "中文（简体）",
    "to_name": "英文",
    "char_count": 5
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="mingyan"></a>

## 54. 名人名言 `mingyan`

返回一条名人名言，支持按类型筛选。action=types 可获取所有类型列表。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/mingyan` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 50 次；匿名 30 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/mingyan |
| Marketplace | https://apizero.cn/marketplace/mingyan |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 可选：'types' 列出所有类型 |  |
| typeid | string | 否 | 名言类型 ID（数字） |  |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 可选：'types' 列出所有类型 |  |
| typeid | string | 否 | 名言类型 ID（数字） |  |

请求体示例：

```json
{
  "action": "<action>",
  "typeid": "<typeid>"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"action": "<action>", "typeid": "<typeid>"}' \
  "https://v1.apizero.cn/api/mingyan"
```

### 响应示例 `200`

```json
{
  "code": 200,
  "message": "success",
  "data": {},
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="air-history"></a>

## 55. 历史空气质量 `air-history`

按城市 + 年月查询历史空气质量档案：逐日 AQI 与六项污染物（PM2.5/PM10/SO₂/NO₂/CO/O₃）浓度、空气质量等级、首要污染物、全国排名，并给出月度汇总（均值、最佳/最差日、优良天数分布）。

可查范围 2013 年 1 月至当前月，覆盖全国主要城市。首要污染物按国标 HJ 633-2012 IAQI 分指数计算。数据仅供参考。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/air-history` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 50 次；匿名 5 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/air-history |
| Marketplace | https://apizero.cn/marketplace/air-history |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| city | string | 是 | 城市中文名 | 北京 |
| month | string | 是 | 年月，格式 YYYYMM，可查 2013-01 至当前月 | 202503 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| city | string | 是 | 城市中文名 | 北京 |
| month | string | 是 | 年月，格式 YYYYMM，可查 2013-01 至当前月 | 202503 |

请求体示例：

```json
{
  "city": "北京",
  "month": "202503"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"city": "北京", "month": "202503"}' \
  "https://v1.apizero.cn/api/air-history"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "meta": {
      "city": "北京",
      "month": "202412",
      "month_format": "2024年12月",
      "total_days": 31
    },
    "summary": {
      "aqi_avg": 58.3,
      "aqi_avg_level": "良",
      "best_day": {
        "date": "2024-12-05",
        "aqi": 28,
        "level": "优"
      },
      "worst_day": {
        "date": "2024-12-20",
        "aqi": 168,
        "level": "中度污染"
      },
      "days_distribution": {
        "excellent": 8,
        "good": 18,
        "light": 3,
        "medium": 2,
        "heavy": 0,
        "severe": 0
      }
    },
    "daily": [
      {
        "date": "2024-12-01",
        "aqi": 53,
        "level": "良",
        "primary_pollutant": "细颗粒物(PM2.5)",
        "rank": 123,
        "pollutants": {
          "pm2_5": 26,
          "pm10": 55,
          "so2": 4,
          "no2": 35,
          "co": 0.5,
          "o3": 52
        }
      }
    ]
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="soul-soup"></a>

## 56. 心灵毒鸡汤 `soul-soup`

随机返回一句"反鸡汤"文案，用于自嘲、解压或段子素材。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/soul-soup` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 50 次；匿名 30 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/soul-soup |
| Marketplace | https://apizero.cn/marketplace/soul-soup |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| — | — | 否 | 无 | — |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| — | — | 否 | 无 | — |

请求体示例：

```json
{
  "—": "—"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"—": "—"}' \
  "https://v1.apizero.cn/api/soul-soup"
```

### 响应示例 `200`

```json
{
  "code": 200,
  "message": "success",
  "data": {},
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="doubao-image"></a>

## 57. 豆包图片生成 `doubao-image`

基于字节跳动即梦 5.0 Pro（Seedream 5.0 Pro）的文生图。直连初和同款上游，不经过本站 /api/ai-chat。

【核心能力】
- 即梦 5.0 Pro：空间关系与细节比 3.0 明显更好，适合海报、人像、商品概念图
- 默认 1K 出图，按传入 size 映射宽高比（方形 / 16:9 / 9:16）
- 中文友好，无需先译成英文

【计费说明】
- 登录每日 5 张免费；超出 ¥0.38/张
- 返回地址为上游 COS 常驻链，建议仍自行转存

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/doubao-image` |
| Method | `POST` |
| 分类 | AI 能力 (`ai`) |
| 计费 | 按次付费 · 点数包 · 月套餐 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 5 次；匿名 1 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/doubao-image |
| Marketplace | https://apizero.cn/marketplace/doubao-image |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| prompt | string | 是 | 图片描述文本，支持中英文混合。建议 50~300 字符，越具体效果越好。 | 一只赛博朋克猫在雨夜的霓虹街头，低角度，电影感，Wong Kar-Wai 风格 |
| size | string | 否 | 对外尺寸枚举，内部按 1K 出图并映射宽高比：1024x1024=1:1；1792x1024 / 1280x720 / 1920x1080=16:9；1024x1792 / 720x1280=9:16。 | 1024x1024 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| prompt | string | 是 | 图片描述文本，支持中英文混合。建议 50~300 字符，越具体效果越好。 | 一只赛博朋克猫在雨夜的霓虹街头，低角度，电影感，Wong Kar-Wai 风格 |
| size | string | 否 | 对外尺寸枚举，内部按 1K 出图并映射宽高比：1024x1024=1:1；1792x1024 / 1280x720 / 1920x1080=16:9；1024x1792 / 720x1280=9:16。 | 1024x1024 |

请求体示例：

```json
{
  "prompt": "一只赛博朋克猫在雨夜的霓虹街头，低角度，电影感，Wong Kar-Wai 风格",
  "size": "1024x1024"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"prompt": "一只赛博朋克猫在雨夜的霓虹街头，低角度，电影感，Wong Kar-Wai 风格", "size": "1024x1024"}' \
  "https://v1.apizero.cn/api/doubao-image"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "url": "https://ark-content-generation-v2-cn-beijing.tos-cn-beijing.volces.com/doubao-seedream-3-0-t2i/021777940499xxx_0.jpeg?X-Tos-Algorithm=TOS4-HMAC-SHA256&X-Tos-Expires=86400&X-Tos-Signature=...",
    "size": "1024x1024",
    "prompt": "一只赛博朋克猫在雨夜的霓虹街头，低角度，电影感，Wong Kar-Wai 风格",
    "created": 1777940499,
    "expires_in": 86400,
    "tokens": 4096
  },
  "request_id": "mqx8x12345abc",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ai-chat"></a>

## 58. 大模型 `ai-chat`

一把 Key 调对话、生图、视频。地址 POST https://v1.apizero.cn/v1/chat/completions，SDK base 填 https://v1.apizero.cn/v1。默认经济档（最低），也可选适中或较贵。成功后按 Token / 任务价扣大模型额度。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ai-chat` |
| Method | `POST` |
| 分类 | AI 能力 (`ai`) |
| 计费 | 按次付费 · 点数包 · 月套餐 |
| QPS | 0 req/s |
| 每日免费额度 | 登录用户  次；匿名  次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 大模型统一网关；对话/生图/视频同一 Completions 地址，默认经济档。 |
| 官网文档 | https://apizero.cn/aidocs/ai-chat |
| Marketplace | https://apizero.cn/marketplace/ai-chat |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| model | string | 是 | 对话模型 ID，见本页模型表或 ?type=chat | deepseek-v4-flash-0731 |
| tier | string | 否 | 收费档：economy 经济（默认、最低）/ standard 适中 / plus 较贵。不传按经济档 | economy |
| messages | array | 是 | OpenAI 风格 messages，可带历史轮次 | [{"role":"user","content":"用一句话介绍极数本源"}] |
| stream | boolean | 否 | true 时按 SSE 流式返回 | false |
| type | string | 否 | chat / image / video / audio，不传返回全部 | chat |
| q | string | 否 | 按模型 ID 或名称搜索 | deepseek |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| model | string | 是 | 对话模型 ID，见本页模型表或 ?type=chat | deepseek-v4-flash-0731 |
| tier | string | 否 | 收费档：economy 经济（默认、最低）/ standard 适中 / plus 较贵。不传按经济档 | economy |
| messages | array | 是 | OpenAI 风格 messages，可带历史轮次 | [{"role":"user","content":"用一句话介绍极数本源"}] |
| stream | boolean | 否 | true 时按 SSE 流式返回 | false |
| type | string | 否 | chat / image / video / audio，不传返回全部 | chat |
| q | string | 否 | 按模型 ID 或名称搜索 | deepseek |

请求体示例：

```json
{
  "model": "deepseek-v4-flash-0731",
  "tier": "economy",
  "messages": "[{\"role\":\"user\",\"content\":\"用一句话介绍极数本源\"}]",
  "stream": "false",
  "type": "chat",
  "q": "deepseek"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "deepseek-v4-flash-0731", "tier": "economy", "messages": "[{\"role\":\"user\",\"content\":\"用一句话介绍极数本源\"}]", "stream": "false", "type": "chat", "q": "deepseek"}' \
  "https://v1.apizero.cn/api/ai-chat"
```

### 响应示例 `200`

```json
{
  "id": "chatcmpl-demo",
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "极数本源提供统一 Key 的 API 与大模型接入。"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 16,
    "completion_tokens": 18,
    "total_tokens": 34
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="bank-card"></a>

## 59. 银行卡BIN查询 `bank-card`

根据银行卡号前6位查询发卡行、卡类型、卡品牌等信息

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/bank-card` |
| Method | `GET` |
| 分类 | 金融数据 (`finance`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 1000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/bank-card |
| Marketplace | https://apizero.cn/marketplace/bank-card |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| — | — | 否 | 无 | — |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/bank-card?—=—"
```

### 响应示例 `200`

```json
{
  "code": 200,
  "message": "success",
  "data": {},
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="food-license"></a>

## 60. 食品经营许可证识别 `food-license`

上传食品经营许可证图片（URL 或 base64），自动识别证件字段，包括许可证编号、经营者名称、法定代表人、经营场所、主体业态、经营项目、有效期等共 13 个字段。适用于企业资质审核、供应链合规验证等场景。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/food-license` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 50 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/food-license |
| Marketplace | https://apizero.cn/marketplace/food-license |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| key | string | 否 | API 密钥（Bearer 令牌或 key 参数） |  |
| input_type | string | 是 | 图片传入方式：url（图片链接）或 base64（base64 编码字符串） |  |
| input_data | string | 是 | 图片 URL 地址（input_type=url）或 base64 编码字符串（input_type=base64，最大 5 MB） |  |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| key | string | 否 | API 密钥（Bearer 令牌或 key 参数） |  |
| input_type | string | 是 | 图片传入方式：url（图片链接）或 base64（base64 编码字符串） |  |
| input_data | string | 是 | 图片 URL 地址（input_type=url）或 base64 编码字符串（input_type=base64，最大 5 MB） |  |

请求体示例：

```json
{
  "key": "<key>",
  "input_type": "<input_type>",
  "input_data": "<input_data>"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"key": "<key>", "input_type": "<input_type>", "input_data": "<input_data>"}' \
  "https://v1.apizero.cn/api/food-license"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "message": "success",
  "data": {
    "license_number": "JY14012800001234",
    "operator": "某某餐饮有限公司",
    "legal_representative": "张三",
    "premise": "北京市朝阳区某街道1号",
    "main_body": "餐饮服务经营者",
    "operating_item": "热食类食品制售",
    "validity_period": "长期",
    "domicile": "北京市朝阳区某街道1号",
    "issuing_authority": "北京市朝阳区市场监督管理局",
    "issuer": "李四",
    "daily_supervisor": "王五",
    "daily_supervisory_authorities": "北京市朝阳区市场监督管理局",
    "complaints_hotline": "12315"
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="site-security"></a>

## 61. 网站安全综合评分 `site-security`

五维加权综合评分：SSL 证书 (25%) + 域名安全 (20%) + ICP 备案 (20%) + 微信/QQ 拦截 (15%) + 网站性能 (20%)，总分 0-100，对应 A/B/C/D/F 五级。一次请求得到全面诊断报告。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/site-security` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 3000 次；匿名 1000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/site-security |
| Marketplace | https://apizero.cn/marketplace/site-security |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 纯域名，如 baidu.com |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/site-security?domain=<domain>"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "domain": "baidu.com",
    "overall_score": 92,
    "grade": "A",
    "detection_time": "4521ms",
    "ssl": {
      "score": 100,
      "https_enabled": true,
      "days_until_expiry": 365
    }
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="hash"></a>

## 62. 哈希加密计算 `hash`

哈希加密计算，支持 12 种主流算法，可一次性返回全部，也可指定单个算法。支持 HMAC 签名模式与 hex / base64 双输出编码，毫秒级返回。

• 通用摘要：MD5、SHA-1、SHA-256、SHA-384、SHA-512

• 现代抗碰撞：SHA3-256、SHA3-512、RIPEMD-160、Whirlpool

• 校验和：CRC32、CRC32B、Adler-32

• HMAC 签名：传入 hmac_key 自动切换为 HMAC 模式（用于 API 签名 / 防篡改场景）

• 输出编码：hex（默认，更可读）/ base64（节省 25% 字节，适合 URL 传输）

纯本地计算，零外部服务依赖，毫秒级响应。HMAC 密钥仅参与计算，不写日志、不缓存、不回显。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/hash` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 200 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/hash |
| Marketplace | https://apizero.cn/marketplace/hash |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 待计算文本，UTF-8，最长 10000 字节 | hello |
| algorithm | string | 否 | 算法，此处固定 all | all |
| encoding | string | 否 | 输出编码 hex（默认）/ base64 | hex |
| hmac_key | string | 否 | 可选；传入则切换 HMAC 模式 |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/hash?text=hello"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "text_length": 5,
    "text_bytes": 5,
    "encoding": "hex",
    "hmac": false,
    "hash_count": 12,
    "hashes": {
      "md5": {
        "algorithm": "MD5",
        "bits": 128,
        "value": "5d41402abc4b2a76b9719d911017c592",
        "length": 32
      },
      "sha1": {
        "algorithm": "SHA-1",
        "bits": 160,
        "value": "aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d",
        "length": 40
      },
      "sha256": {
        "algorithm": "SHA-256",
        "bits": 256,
        "value": "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824",
        "length": 64
      },
      "sha384": {
        "algorithm": "SHA-384",
        "bits": 384,
        "value": "59e1748777448c69de6b800d7a33bbfb9ff1b463e44354c3553bcdb9c666fa90125a3c79f90397bdf5f6a13de828684f",
        "length": 96
      },
      "sha512": {
        "algorithm": "SHA-512",
        "bits": 512,
        "value": "9b71d224bd62f3785d96d46ad3ea3d73319bfbc2890caadae2dff72519673ca72323c3d99ba5c11d7c7acc6e14b8c5da0c4663475c2e5c3adef46f73bcdec043",
        "length": 128
      },
      "sha3-256": {
        "algorithm": "SHA3-256",
        "bits": 256,
        "value": "3338be694f50c5f338814986cdf0686453a888b84f424d792af4b9202398f392",
        "length": 64
      },
      "sha3-512": {
        "algorithm": "SHA3-512",
        "bits": 512,
        "value": "75d527c368f2efe848ecf6b073a36767800805e9eef2b1857d5f984f036eb6df891d75f72d9b154518c1cd58835286d1da9a38deba3de98b5a53e5ed78a84976",
        "length": 128
      },
      "ripemd160": {
        "algorithm": "RIPEMD-160",
        "bits": 160,
        "value": "108f07b8382412612c048d07d13f814118445acd",
        "length": 40
      },
      "whirlpool": {
        "algorithm": "Whirlpool",
        "bits": 512,
        "value": "0a25f55d7308eca6b9567a7ed3bd1b46327f0f1ffdc804dd8bb5af40e88d78b88df0d002a89e2fdbd5876c523f1b67bc44e9f87047598e7548298ea1c81cfd73",
        "length": 128
      },
      "crc32": {
        "algorithm": "CRC32",
        "bits": 32,
        "value": "3d653119",
        "length": 8
      },
      "crc32b": {
        "algorithm": "CRC32B",
        "bits": 32,
        "value": "3610a686",
        "length": 8
      },
      "adler32": {
        "algorithm": "Adler-32",
        "bits": 32,
        "value": "062c0215",
        "length": 8
      }
    }
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="email-check"></a>

## 63. 邮箱地址检测 `email-check`

综合性邮箱质量评估接口，一次请求完成 6 项检测：
  ① RFC 5322 格式校验
  ② 临时/一次性邮箱检测（基于 72,345 条开源域名库，3 个数据源合并去重）
  ③ MX 记录验证（用 AliDNS DoH，避开 PHP getmxrr 不稳定）
  ④ 拼写纠正（gmial.com → 提示 gmail.com）
  ⑤ 服务商识别（QQ邮箱/Gmail/网易/Outlook 等 40+ 主流邮箱）
  ⑥ 综合风险评分 0-100，附详细原因清单

典型用例：用户注册时的反垃圾邮箱过滤、邮件营销列表清洗、KYC 风控辅助。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/email-check` |
| Method | `GET` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 500 次；匿名 100 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/email-check |
| Marketplace | https://apizero.cn/marketplace/email-check |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| email | string | 是 | 要检测的邮箱地址，最长 254 字符（RFC 上限） |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/email-check?email=<email>"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "email": "test@gmial.com",
    "input": "test@gmial.com",
    "valid_format": true,
    "local": "test",
    "domain": "gmial.com",
    "is_disposable": false,
    "disposable_match": null,
    "is_trusted": false,
    "provider": null,
    "has_mx": false,
    "mx_records": [],
    "spelling_suggestion": "gmail.com",
    "risk_score": 5,
    "risk_level": "invalid",
    "reasons": [
      "⚠️ 域名无 MX 记录，无法接收邮件",
      "⚠️ 域名疑似拼写错误，建议用 gmail.com",
      "⚠️ 本地部分含测试/系统类关键词"
    ]
  },
  "request_id": "mota...",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="risk-score"></a>

## 64. 综合风控评分 `risk-score`

输入手机号 / IP / 邮箱，秒级输出 0~100 风险分与放行/二次验证/拦截建议，专治注册薅羊毛、批量养号、营销作弊。三维信号：手机号识别虚拟运营商与物联网卡号段，IP 识别代理/VPN/机房与风险分，邮箱识别临时邮箱与 MX 异常。一次调用拿到可直接用于业务决策的结论。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/risk-score` |
| Method | `POST` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 按次付费 · 点数包 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 10 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/risk-score |
| Marketplace | https://apizero.cn/marketplace/risk-score |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| mobile | string | 否 | 手机号（11 位手机号或 13 位物联网卡号），识别虚拟运营商/物联网卡 | 17012345678 |
| ip | string | 否 | IPv4/IPv6 地址；传 self 检测调用者自身 IP | 47.88.1.1 |
| email | string | 否 | 邮箱地址，识别临时邮箱/MX/本地异常 | abc@guerrillamail.com |
| scene | string | 否 | 业务场景 register/login/order/coupon，默认 register | register |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| mobile | string | 否 | 手机号（11 位手机号或 13 位物联网卡号），识别虚拟运营商/物联网卡 | 17012345678 |
| ip | string | 否 | IPv4/IPv6 地址；传 self 检测调用者自身 IP | 47.88.1.1 |
| email | string | 否 | 邮箱地址，识别临时邮箱/MX/本地异常 | abc@guerrillamail.com |
| scene | string | 否 | 业务场景 register/login/order/coupon，默认 register | register |

请求体示例：

```json
{
  "mobile": "17012345678",
  "ip": "47.88.1.1",
  "email": "abc@guerrillamail.com",
  "scene": "register"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mobile": "17012345678", "ip": "47.88.1.1", "email": "abc@guerrillamail.com", "scene": "register"}' \
  "https://v1.apizero.cn/api/risk-score"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "risk_score": 88,
    "risk_level": "critical",
    "decision": "reject",
    "checked": {
      "mobile": true,
      "ip": true,
      "email": true
    },
    "hit_rules": [
      {
        "code": "MOBILE_MVNO",
        "weight": 35,
        "desc": "虚拟运营商号段（170），实名宽松，薅羊毛高发"
      },
      {
        "code": "EMAIL_DISPOSABLE",
        "weight": 35,
        "desc": "一次性/临时邮箱域名，典型用于注册套利"
      },
      {
        "code": "IP_DATACENTER",
        "weight": 30,
        "desc": "机房/IDC IP（非真实用户网络，脚本批量常用）"
      }
    ],
    "signals": {
      "mobile": {
        "checked": true,
        "input_mask": "170****5678",
        "valid": true,
        "number_type": "mvno",
        "carrier": "虚拟运营商",
        "risk": "high"
      },
      "email": {
        "checked": true,
        "email": "abc@guerrillamail.com",
        "valid_format": true,
        "is_disposable": true,
        "is_trusted": false,
        "has_mx": true,
        "risk": "high"
      },
      "ip": {
        "checked": true,
        "ip": "47.88.x.x",
        "valid": true,
        "is_private": false,
        "is_proxy": false,
        "is_datacenter": true,
        "province": "",
        "isp": "阿里云",
        "risk": "medium"
      }
    },
    "scene": "register"
  },
  "request_id": "k9x2p4mabc12",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="address-parse"></a>

## 65. 中文地址解析 `address-parse`

一行 API 从中文地址字符串中提取「省市区街道 + 详细地址 + 姓名 + 手机号 + 邮编」。

适用场景：电商收货地址自动拆分、快递下单页智能填充、CRM 客户资料清洗、办公地址结构化入库。

特点：纯本地正则算法，无任何服务依赖，毫秒级响应；支持 34 个省级行政区及其简称识别（如「北京」→「北京市」、「新疆」→「新疆维吾尔自治区」）；支持快递场景下「张三 138xxxxxxxx 上海市浦东新区xx路xx号 200000」这类混合输入的自动拆分。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/address-parse` |
| Method | `POST` |
| 分类 | 地理位置 (`geo`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 100 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/address-parse |
| Marketplace | https://apizero.cn/marketplace/address-parse |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| address | string | 是 | 中文地址字符串。支持姓名/手机/邮编混合输入，长度 ≤ 500 | 张三 13812345678 上海市浦东新区张江镇科苑路88号 201203 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| address | string | 是 | 中文地址字符串。支持姓名/手机/邮编混合输入，长度 ≤ 500 | 张三 13812345678 上海市浦东新区张江镇科苑路88号 201203 |

请求体示例：

```json
{
  "address": "张三 13812345678 上海市浦东新区张江镇科苑路88号 201203"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"address": "张三 13812345678 上海市浦东新区张江镇科苑路88号 201203"}' \
  "https://v1.apizero.cn/api/address-parse"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "original": "张三 138****1234 上海市浦东新区张江镇科苑路88号 201203",
    "province": "上海市",
    "city": "上海市",
    "district": "浦东新区",
    "street": "张江镇",
    "detail": "科苑路88号",
    "zipcode": "201203",
    "phone": "138****1234",
    "name": "张三"
  },
  "request_id": "kx8n9q2a1b3c4d5e6f7g",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-idcard"></a>

## 66. 身份证识别 `ocr-idcard`

上传身份证正面或反面图片（URL 或 base64），自动识别并结构化返回姓名、身份证号、性别、民族、出生日期、地址、签发机关、有效期等 10 个字段。

支持正反面自动判断，适用于实名认证、用户信息录入、KYC 核验辅助等场景。需要登录后使用，保护用户隐私。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-idcard` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-idcard |
| Marketplace | https://apizero.cn/marketplace/ocr-idcard |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传入方式 | url |
| input_data | string | 是 | 图片 URL 或 base64 编码字符串（jpg/png，base64 最大 10 MB） | https://example.com/idcard-front.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传入方式 | url |
| input_data | string | 是 | 图片 URL 或 base64 编码字符串（jpg/png，base64 最大 10 MB） | https://example.com/idcard-front.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/idcard-front.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/idcard-front.jpg"}' \
  "https://v1.apizero.cn/api/ocr-idcard"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "side": 1,
    "identity_name": "张三",
    "identity_code": "310101199001011234",
    "gender": "男",
    "race": "汉",
    "birth": "1990-01-01",
    "address": "上海市浦东新区某某路123号",
    "issued_by": null,
    "valid_date_start": null,
    "valid_date_end": null
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="business-license"></a>

## 67. 营业执照识别 `business-license`

结构化识别营业执照，提取统一社会信用代码、名称、类型、法定代表人、注册资本、成立日期、住所、经营范围、登记机关、核准日期等字段。

支持常见纸质/电子营业执照版式；入参兼容图片 URL 或 base64。旧版字段保持兼容，并新增 registration_authority（登记机关）、business_term（营业期限）、ocr_ms。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/business-license` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/business-license |
| Marketplace | https://apizero.cn/marketplace/business-license |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式：url（公网图片地址）或 base64 | url |
| input_data | string | 是 | 图片内容：url 时填 http/https 链接；base64 时填编码串（可含 data:image/xxx;base64, 前缀），≤10MB | https://example.com/business-license.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式：url（公网图片地址）或 base64 | url |
| input_data | string | 是 | 图片内容：url 时填 http/https 链接；base64 时填编码串（可含 data:image/xxx;base64, 前缀），≤10MB | https://example.com/business-license.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/business-license.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/business-license.jpg"}' \
  "https://v1.apizero.cn/api/business-license"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "certificate_type": "营业执照",
    "unified_social_credit_code": "91110000MA01234567",
    "company_name": "北京示例科技有限公司",
    "company_type": "有限责任公司(自然人投资或控股)",
    "legal_representative": "张三",
    "registered_capital": "壹佰万圆人民币",
    "established_date": "2018-05-20",
    "established_time": "2018年5月20日",
    "business_term": "长期",
    "domicile": "北京市海淀区示例路1号",
    "business_scope": "一般项目：技术服务、技术开发……",
    "registration_authority": "北京市海淀区市场监督管理局",
    "approval_date": "2024-10-18",
    "website": "http://www.gsxt.gov.cn",
    "ocr_ms": 1300
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="unshort"></a>

## 68. 短链还原 `unshort`

完整还原一个短链的全部跳转链路，输出每跳的状态码、跳转方式（Location/Meta-Refresh）和耗时。适合钓鱼链接溯源、推广短链分析、二维码内容核对。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/unshort` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 2000 次；匿名 300 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/unshort |
| Marketplace | https://apizero.cn/marketplace/unshort |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 是 | 要展开的短链 | https://t.cn/A6xxxx |
| max_hops | number | 否 | 最大跳转次数（1-30，默认 10） |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/unshort?url=https://t.cn/A6xxxx"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "original_url": "https://t.cn/Aabc",
    "final_url": "https://example.com/landing",
    "hops": 2,
    "total_time_ms": 412,
    "chain": [
      {
        "hop": 1,
        "url": "https://t.cn/Aabc",
        "status": 302,
        "method": "Location",
        "duration_ms": 120,
        "next": "https://example.com/landing"
      },
      {
        "hop": 2,
        "url": "https://example.com/landing",
        "status": 200,
        "method": "final",
        "duration_ms": 292
      }
    ],
    "is_redirect": true
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="site-check"></a>

## 69. 网站测速诊断 `site-check`

测量网站的 DNS 解析、TCP 连接、SSL 握手、TTFB、总耗时，跟踪重定向链并提取 SSL 证书摘要、命中 IP/端口、页面体积。一次请求 6 大维度全监测。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/site-check` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 5000 次；匿名 1000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/site-check |
| Marketplace | https://apizero.cn/marketplace/site-check |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 是 | 目标 URL（自动补 https://） |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/site-check?url=<url>"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "url": "https://baidu.com",
    "final_url": "https://www.baidu.com/",
    "http_code": 200,
    "timing": {
      "dns_ms": 15,
      "connect_ms": 32.5,
      "ssl_ms": 78.4,
      "ttfb_ms": 145.2,
      "total_ms": 156.7
    },
    "redirect_count": 1
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ssl"></a>

## 70. SSL 证书检测 `ssl`

通过域名远程探测其 HTTPS/SSL 证书信息：颁发者、颁发机构、签名算法、覆盖域名、有效期、是否过期、距过期天数、SHA-1 指纹、远端 IP 等。

• 智能预处理：自动剥离 http(s):// 前缀、路径、查询串、端口、www. 子域
• 严格域名校验：合法域名格式（最长 253 字符 + RFC 1123 标签规则）才打服务
• 三态响应：有 SSL（is_ssl=true）→ 完整信息；无 SSL/连接失败 → is_ssl=false 其余字段 null；服务异常 → 502
• 字段标准化：服务 null 字段透传 null 不补 0；自动转 int/string 类型；is_expire 重命名 is_expired
• 缓存策略：成功 6h（证书短期不变）；无证书 30min（避免错误域名反复打服务）

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ssl` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 3000 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | SSL 证书查询；适合站长工具、证书到期提醒。 |
| 官网文档 | https://apizero.cn/aidocs/ssl |
| Marketplace | https://apizero.cn/marketplace/ssl |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 要检测的域名。可带 http(s):// 前缀、路径、端口、www.，会自动剥离 | apizero.cn |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/ssl?domain=apizero.cn"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "domain": "apizero.cn",
    "common_name": "*.apizero.cn",
    "domains": [
      "*.apizero.cn",
      "apizero.cn"
    ],
    "issuing_agency": "Asseco Data Systems S.A.",
    "issuer": "Certum DV TLS G2 R39 CA",
    "signature_algorithm": "RSA-SHA256",
    "is_ssl": true,
    "is_expired": false,
    "life_span_days": 198,
    "expire_days": 184,
    "start_date": "2026-04-22 17:05:00",
    "expire_date": "2026-11-07 17:04:59",
    "fingerprint": "f4633adfd1cb59185ba094dc3edeef5a8ea26889",
    "remote_address": "119.36.225.184:443"
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="text-similarity"></a>

## 71. 文本相似度 `text-similarity`

纯本地计算的文本相似度比对，输入两段文本（每段 ≤ 5000 字）输出 4 种相似度指标 + 加权综合评分 + 5 级评级。

• **零延迟零成本**：纯 PHP 本地计算，无外部服务依赖，平均响应 < 100ms
• **4 种指标**：余弦相似度（35%）+ Jaccard 系数（25%）+ 编辑距离归一化（20%）+ LCS 比率（20%）
• **5 级评级**：几乎相同 / 高度相似 / 中度相似 / 轻度相似 / 差异较大
• **修复源码 bug**：自实现 mb_levenshtein 字符级编辑距离，杜绝 PHP 内置 levenshtein 按字节计算导致的 85 汉字崩溃问题
• **超长保护**：超过 500 字符自动截取并按比例还原，5000×5000 字符比对约 60-80ms
• **典型场景**：评论查重、AI 生成内容检测、多语言翻译质量评估、客服话术匹配

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/text-similarity` |
| Method | `POST` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 50000 次；匿名 10000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/text-similarity |
| Marketplace | https://apizero.cn/marketplace/text-similarity |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text1 | string | 是 | 第一段文本，1-5000 字符（中英文均按 1 字符计） | 今天天气不错，适合出门散步 |
| text2 | string | 是 | 第二段文本，1-5000 字符 | 今天天气真好，适合出门走走 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text1 | string | 是 | 第一段文本，1-5000 字符（中英文均按 1 字符计） | 今天天气不错，适合出门散步 |
| text2 | string | 是 | 第二段文本，1-5000 字符 | 今天天气真好，适合出门走走 |

请求体示例：

```json
{
  "text1": "今天天气不错，适合出门散步",
  "text2": "今天天气真好，适合出门走走"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text1": "今天天气不错，适合出门散步", "text2": "今天天气真好，适合出门走走"}' \
  "https://v1.apizero.cn/api/text-similarity"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "text1_length": 13,
    "text2_length": 13,
    "overall_score": 0.6471,
    "similarity_level": "moderately_similar",
    "level_name": "中度相似",
    "metrics": {
      "cosine": 0.5833,
      "jaccard": 0.4118,
      "edit_similarity": 0.6923,
      "lcs_similarity": 0.9231,
      "edit_distance": 4,
      "lcs_length": 12
    },
    "truncated": false
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="bencao"></a>

## 72. 本草纲目·中药查询 `bencao`

传统中药材知识查询接口，覆盖《本草纲目》及常见中药材数据。输入药材名称（如「人参」「丁香」「甘草」「枸杞」），返回该药材的释名、气味、主治、附方等详细记载。

【典型场景】
- 中医养生 / 食疗 App 的药材百科
- 中药知识科普类小程序
- AI 中医问诊辅助参考
- 古籍数字化项目
- 国学 / 中医文化教学

【调用示例】
GET /api/bencao?msg=人参
GET /api/bencao?msg=丁香
GET /api/bencao?msg=甘草

【模糊匹配】
- 精确名称查得到 → 直接返回详情（matched=exact）
- 找不到时返回 4040 + suggestions 数组（最多 10 个相关建议）
- 比如查「人参枸杞」会建议「人参、枸杞」等单味药

【⚠️ 数据来源说明】
本接口数据整理自《本草纲目》及网络公开整理资料，仅供学习参考；中医药疗用请遵医嘱。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/bencao` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 1000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/bencao |
| Marketplace | https://apizero.cn/marketplace/bencao |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| msg | string | 是 | 药品名称（中文），如：人参、丁香、甘草、当归、枸杞。最长 50 个字符。 | 人参 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/bencao?msg=人参"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "name": "人参",
    "detail": "「释名」黄参、神草、土精、血参...\n「气味」（根）甘、温、无毒...\n「主治」补五脏，安精神...",
    "matched": "exact"
  },
  "request_id": "mqx8x12345abc",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="traffic-weather-alert"></a>

## 73. 限行天气联动 `traffic-weather-alert`

输入国内城市拼音（兼容中文），返回当天的限行尾号。如遇暴雨/台风等恶劣天气，附加居家办公建议。覆盖北京、天津、成都、杭州、贵阳、长春 6 个限行城市，天气支持所有国内主要城市。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/traffic-weather-alert` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 5000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/traffic-weather-alert |
| Marketplace | https://apizero.cn/marketplace/traffic-weather-alert |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| action | string | 否 | 固定 restriction（默认） | restriction |
| city | string | 是 | 城市拼音或中文（如 beijing / 北京） | beijing |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/traffic-weather-alert?city=beijing"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "city": "beijing",
    "city_cn": "北京",
    "date": "2026-07-31",
    "weekday": "周五",
    "restricted_numbers": "3,8",
    "restriction_active": true,
    "weather": {
      "weather": "Clear ",
      "temperature": "28°C",
      "is_severe": false,
      "severe_type": null
    },
    "work_from_home_advisory": null,
    "message": "今日北京（周五）限行尾号为 3,8"
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="dns-check"></a>

## 74. DNS 劫持检测 `dns-check`

通过 4 家公共 DoH（DNS over HTTPS）服务器并发查询同一域名，对比解析结果检测 DNS 是否被运营商劫持、终端 hosts 篡改或遭遇异常 GeoDNS 分流。

服务器列表：
  • AliDNS（阿里云 - 中国）
  • DNSPod（腾讯 - 中国）
  • 360 安全 DNS（中国）
  • Cloudflare（美国 - 在中国大陆服务器侧可能超时，会被标记为 timeout）

特性：
  • A + AAAA 记录同时查询（IPv4 / IPv6）
  • 提取 CNAME 链路（CDN 跳转可见）
  • TTL 信息汇总（缓存提示）
  • 智能风险分级算法：safe / safe_with_geodns / suspicious / hijack_likely / unknown
  • 支持各类输入：domain / https://domain / domain:port / domain/path（自动剥离）

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/dns-check` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 2000 次；匿名 50 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/dns-check |
| Marketplace | https://apizero.cn/marketplace/dns-check |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 要检测的域名（如 baidu.com，自动剥离 http(s):// 协议头与路径，最长 253 字符） |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/dns-check?domain=<domain>"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "domain": "taobao.com",
    "input": "https://www.taobao.com/page",
    "exec_ms": 312,
    "summary": {
      "status_text": "DNS 解析正常",
      "risk_level": "safe",
      "risk_score": 95,
      "explain": "4 家 DoH 全部相互验证通过，未检测到劫持迹象。",
      "cname_chain": [
        "www.taobao.com.danuoyi.tbcache.com"
      ],
      "success_count": 3,
      "total_count": 4,
      "unique_ipv4_count": 8,
      "unique_ipv6_count": 0
    },
    "unique_ipv4": [
      "59.82.121.163",
      "59.82.122.130",
      "59.82.122.140",
      "59.82.122.165",
      "59.82.43.234",
      "59.82.43.238",
      "59.82.43.239",
      "59.82.44.240"
    ],
    "unique_ipv6": [],
    "servers": [
      {
        "key": "alidns",
        "name": "AliDNS",
        "status": "ok",
        "error": null,
        "latency_ms": 105,
        "ipv4": [
          "59.82.121.163",
          "59.82.122.130",
          "..."
        ],
        "ipv6": [],
        "cname_chain": [
          "www.taobao.com.danuoyi.tbcache.com"
        ],
        "ttl_min": 60
      },
      {
        "key": "dnspod",
        "name": "DNSPod",
        "status": "ok",
        "latency_ms": 180,
        "ipv4": [
          "59.82.121.163",
          "..."
        ]
      },
      {
        "key": "china360",
        "name": "360",
        "status": "ok",
        "latency_ms": 117
      },
      {
        "key": "cloudflare",
        "name": "Cloudflare",
        "status": "timeout",
        "error": "Operation timed out after 6000 ms",
        "latency_ms": 6000
      }
    ]
  },
  "request_id": "mota...",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="idcard-region"></a>

## 75. 身份证归属地查询 `idcard-region`

根据身份证号前 6 位查询省/市/区三级归属地。支持完整 18 位身份证号自动脱敏回显。省份数据按需从 CDN 拉取并本地缓存 30 天，网关 Redis 缓存 24h。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/idcard-region` |
| Method | `GET` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 300 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/idcard-region |
| Marketplace | https://apizero.cn/marketplace/idcard-region |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| idcard | string | 是 | 6 位区划代码或 15/18 位身份证号 | 110101 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/idcard-region?idcard=110101"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "idcard": "110101************",
    "province": {
      "code": "110000",
      "name": "北京市"
    },
    "city": {
      "code": "110100",
      "name": "北京市"
    },
    "district": {
      "code": "110101",
      "name": "东城区"
    }
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="dns-query"></a>

## 76. DNS 记录查询 `dns-query`

查询域名的各类 DNS 记录，支持 A / AAAA / NS / CNAME / MX / TXT / CAA / SOA 共 8 种标准类型，以及 ANY（一次返回所有类型）。

✨ 特色：
  • 不依赖第三方工具站，完全自建 — 3 家国内 DoH 并发（AliDNS / DNSPod / 360）
  • 所有记录结构化解析：MX 拆 priority/exchange、CAA 拆 flags/tag/value、SOA 拆 mname/serial/...
  • 多家结果合并去重 + 各记录标注来自哪些 DoH（sources 字段）
  • 兼容数字 qtype（如 1=A / 15=MX / 257=CAA），不破坏旧调用方式
  • ANY 模式：单次请求拿到域名的全部 DNS 配置，免去多次查询

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/dns-query` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 500 次；匿名 100 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/dns-query |
| Marketplace | https://apizero.cn/marketplace/dns-query |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| host | string | 是 | 域名（自动剥离协议/路径/端口）；也兼容 domain | baidu.com |
| type | string | 否 | 记录类型，此处固定 A（也可用数字编码） | A |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/dns-query?host=baidu.com"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "host": "baidu.com",
    "input": "baidu.com",
    "type": "A",
    "type_code": 1,
    "records": [
      {
        "type": "A",
        "type_code": 1,
        "name": "baidu.com",
        "ttl": 424,
        "data": "110.242.74.102",
        "parsed": {
          "ip": "110.242.74.102"
        },
        "sources": [
          "alidns",
          "china360",
          "dnspod"
        ]
      },
      {
        "type": "A",
        "type_code": 1,
        "name": "baidu.com",
        "ttl": 424,
        "data": "111.63.65.103",
        "parsed": {
          "ip": "111.63.65.103"
        },
        "sources": [
          "alidns",
          "china360",
          "dnspod"
        ]
      },
      {
        "type": "A",
        "type_code": 1,
        "name": "baidu.com",
        "ttl": 424,
        "data": "111.63.65.247",
        "parsed": {
          "ip": "111.63.65.247"
        },
        "sources": [
          "alidns",
          "china360",
          "dnspod"
        ]
      },
      {
        "type": "A",
        "type_code": 1,
        "name": "baidu.com",
        "ttl": 424,
        "data": "124.237.177.164",
        "parsed": {
          "ip": "124.237.177.164"
        },
        "sources": [
          "alidns",
          "china360",
          "dnspod"
        ]
      }
    ],
    "total": 4,
    "exec_ms": 170,
    "sources": [
      "alidns",
      "dnspod",
      "china360"
    ],
    "notes": null
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="webmeta"></a>

## 77. 网页元数据提取 `webmeta`

提取网页的标题、描述、关键词、OG/Twitter Card、favicon，并自动识别使用的 30+ 项技术栈（React/Vue/Next.js/WordPress/Cloudflare 等）。适合 SEO 检测、技术调研、链接预览。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/webmeta` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 5000 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 网页 Meta 信息提取；适合链接预览、采集前预处理、站点分析。 |
| 官网文档 | https://apizero.cn/aidocs/webmeta |
| Marketplace | https://apizero.cn/marketplace/webmeta |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| url | string | 是 | 网页 URL，自动补 https:// | https://baidu.com |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/webmeta?url=https://apizero.cn"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "url": "https://www.baidu.com/",
    "title": "百度一下，你就知道",
    "tech_stack": [
      "jQuery",
      "Baidu Analytics"
    ],
    "http_code": 200
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="bili-dynamic"></a>

## 78. B 站用户动态 `bili-dynamic`

通过 B 站官方公开 API 拉取指定用户的最新动态列表（视频投稿/图文/纯文本/转发等），含发布时间、文本、视频/图片附件、点赞/评论/转发统计。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/bili-dynamic` |
| Method | `GET` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 200 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/bili-dynamic |
| Marketplace | https://apizero.cn/marketplace/bili-dynamic |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| uid | string | 是 | B 站用户 UID（纯数字） | 208259 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/bili-dynamic?uid=208259"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "uid": "208259",
    "count": 5,
    "list": [
      {
        "dynamic_id": "8xxx",
        "type": "DYNAMIC_TYPE_AV",
        "text": "...",
        "stats": {
          "comments": 100,
          "likes": 1000,
          "forwards": 50
        }
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="invoice"></a>

## 79. 增值税发票识别 `invoice`

增值税发票 OCR 识别，支持增值税专用发票、普通发票、电子普票，输出 22+ 个结构化字段。

• 双输入模式：
  - input_type=url：传入公网可访问的图片 URL（http/https）
  - input_type=base64：传入 base64 编码字符串（≤6MB，自动剥离 data:image/...;base64, 前缀）

• 完整识别字段：
  - 发票基本：发票名称、代码、号码、开票日期、校验码、机器编号
  - 金额：价税合计、税额、不含税金额、大写金额
  - 购销方：名称、纳税人识别号、地址电话、开户行账号
  - 经办人：收款人、复核人、开票人
  - 商品明细：items 数组，含品名/规格/数量/单价/金额/税率/税额
  - 备注与盖章信息

• OCR 结果缓存 1 小时（同图同结果），减少重复调用消耗。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/invoice` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 300 次；匿名 50 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/invoice |
| Marketplace | https://apizero.cn/marketplace/invoice |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 输入类型：url=图片URL / base64=图片base64编码 | url |
| input_data | string | 是 | 发票图片数据。input_type=url 时为 http/https 完整 URL；input_type=base64 时为 base64 字符串（最大 6MB，可选 data:image/jpeg;base64, 前缀） | https://example.com/invoice.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 输入类型：url=图片URL / base64=图片base64编码 | url |
| input_data | string | 是 | 发票图片数据。input_type=url 时为 http/https 完整 URL；input_type=base64 时为 base64 字符串（最大 6MB，可选 data:image/jpeg;base64, 前缀） | https://example.com/invoice.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/invoice.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/invoice.jpg"}' \
  "https://v1.apizero.cn/api/invoice"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "invoice_name": "增值税电子普通发票",
    "invoice_code": "011002000311",
    "invoice_no": "12345678",
    "invoice_date": "2024-08-15",
    "check_code": "12345 67890 12345 67890",
    "machine_num": "499099111111",
    "total_price": "94.34",
    "total_tax": "5.66",
    "total_price_and_tax": "100.00",
    "big_total_price_and_tax": "壹佰圆整",
    "buyer": {
      "name": "某某科技有限公司",
      "taxpayer_no": "91110000XXXXXXXXXX",
      "address_phone": "北京市XX区XX路XX号 010-12345678",
      "account": "中国银行 6217001234567890"
    },
    "seller": {
      "name": "某某商贸有限公司",
      "taxpayer_no": "91310000YYYYYYYYYY",
      "address_phone": "上海市XX区XX路XX号 021-87654321",
      "account": "工商银行 6222001234567890"
    },
    "payee": "张三",
    "reviewer": "李四",
    "drawer": "王五",
    "remarks": "",
    "items": [
      {
        "name": "*技术服务*软件开发服务",
        "specification": "",
        "unit": "",
        "quantity": "",
        "unit_price": "",
        "amount": "94.34",
        "tax_rate": "6%",
        "tax": "5.66"
      }
    ]
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="idcard-organ"></a>

## 80. 身份证签发机关查询 `idcard-organ`

通过身份证号前 6 位行政区划代码，查询对应的签发机关（地方公安局）。覆盖全国 3000+ 区划代码，本地数据零服务。仅供身份证真伪辅助核验、户籍查询等合规场景。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/idcard-organ` |
| Method | `GET` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 300 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/idcard-organ |
| Marketplace | https://apizero.cn/marketplace/idcard-organ |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| id | string | 是 | 6 位行政区划代码或完整身份证号（自动截取前 6 位） | 110101 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/idcard-organ?id=110101"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "code": "110101",
    "organization": "北京市公安局东城分局"
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="image-nsfw"></a>

## 81. 图片鉴黄 `image-nsfw`

图片NSFW内容检测。支持本地NudeNet推理（零调用费）及百度/腾讯/阿里云端三家，统一返回 decision（block/review/pass）+ 分类得分 + 检测框。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/image-nsfw` |
| Method | `POST` |
| 分类 | AI 能力 (`ai`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 100 次；匿名 10 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/image-nsfw |
| Marketplace | https://apizero.cn/marketplace/image-nsfw |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| image_url | string | 否 | 图片HTTP(S) URL（与image_b64二选一） | https://example.com/photo.jpg |
| image_b64 | string | 否 | 图片base64（兼容data:URI） |  |
| backend | string | 否 | 检测后端：auto/nudenet/baidu/tencent/aliyun | auto |
| timeout | int | 否 | 超时秒（3~60） | 20 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| image_url | string | 否 | 图片HTTP(S) URL（与image_b64二选一） | https://example.com/photo.jpg |
| image_b64 | string | 否 | 图片base64（兼容data:URI） |  |
| backend | string | 否 | 检测后端：auto/nudenet/baidu/tencent/aliyun | auto |
| timeout | int | 否 | 超时秒（3~60） | 20 |

请求体示例：

```json
{
  "image_url": "https://example.com/photo.jpg",
  "image_b64": "<image_b64>",
  "backend": "auto",
  "timeout": "20"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"image_url": "https://example.com/photo.jpg", "image_b64": "<image_b64>", "backend": "auto", "timeout": "20"}' \
  "https://v1.apizero.cn/api/image-nsfw"
```

### 响应示例 `200`

```json
{
  "code": 200,
  "desc": "success",
  "backend": "nudenet",
  "elapsed_ms": 115,
  "input": {
    "type": "url",
    "source": "https://i0.hdslb.com/bfs/article/922692ab728ebb5f284f64296f3590a0959110a3.jpg",
    "size_bytes": 993377,
    "sha256": "f9a414bd6925f6c870e18d75252cbd764ce964fbd20387639577c9455db5a598",
    "mime": "image/jpeg",
    "width": 1080,
    "height": 1920
  },
  "decision": "pass",
  "label": "normal",
  "score": 0.8511,
  "categories": {
    "porn": 0,
    "sexy": 0,
    "normal": 1
  },
  "detections": [
    {
      "cls": "FACE_FEMALE",
      "score": 0.8511,
      "box": [
        381,
        291,
        528,
        575
      ]
    }
  ],
  "raw": {
    "nudenet": [
      {
        "class": "FACE_FEMALE",
        "score": 0.8510541915893555,
        "box": [
          381,
          291,
          528,
          575
        ]
      }
    ]
  },
  "notes": [],
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="nine-grid-cutter"></a>

## 82. 九宫格切图 `nine-grid-cutter`

上传一张图片（multipart 文件 / base64 / URL 三选一），自动居中裁切为正方形后均分为 N×N 宫格小图，按朋友圈发图顺序返回（左到右、上到下编号 1..N²）。支持 2×2 / 3×3 / 4×4，可设置切片间留白，输出 base64 数组或直接下载 zip。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/nine-grid-cutter` |
| Method | `POST` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 5000 次；匿名 2000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/nine-grid-cutter |
| Marketplace | https://apizero.cn/marketplace/nine-grid-cutter |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| file | file | 否 | 图片文件（multipart 上传，三选一之一），支持 jpg/png/webp/gif |  |
| image_base64 | string | 否 | 图片 base64（dataURL 或纯 base64，三选一） |  |
| image_url | string | 否 | 公网图片 URL（http/https，三选一） |  |
| grid | number | 否 | 宫格数：2 / 3 / 4，默认 3 | 3 |
| gap | number | 否 | 切片间留白像素 0-20，默认 0 | 0 |
| output | string | 否 | 输出格式：base64（默认，JSON）/ zip（直接返回 application/zip） | base64 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| file | file | 否 | 图片文件（multipart 上传，三选一之一），支持 jpg/png/webp/gif |  |
| image_base64 | string | 否 | 图片 base64（dataURL 或纯 base64，三选一） |  |
| image_url | string | 否 | 公网图片 URL（http/https，三选一） |  |
| grid | number | 否 | 宫格数：2 / 3 / 4，默认 3 | 3 |
| gap | number | 否 | 切片间留白像素 0-20，默认 0 | 0 |
| output | string | 否 | 输出格式：base64（默认，JSON）/ zip（直接返回 application/zip） | base64 |

请求体示例：

```json
{
  "file": "<file>",
  "image_base64": "<image_base64>",
  "image_url": "<image_url>",
  "grid": "3",
  "gap": "0",
  "output": "base64"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"file": "<file>", "image_base64": "<image_base64>", "image_url": "<image_url>", "grid": "3", "gap": "0", "output": "base64"}' \
  "https://v1.apizero.cn/api/nine-grid-cutter"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "grid": "3x3",
    "total": 9,
    "gap": 0,
    "original_size": "1080x1920",
    "square_side": 1080,
    "cell_size": "360x360",
    "source": "multipart",
    "pieces": [
      {
        "index": 1,
        "size": "360x360",
        "base64": "iVBORw0K...",
        "data_url": "data:image/png;base64,iVBORw0K..."
      },
      {
        "index": 2,
        "size": "360x360",
        "base64": "...",
        "data_url": "..."
      }
    ]
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="cdn-ips"></a>

## 83. CDN 优选 IP `cdn-ips`

获取主流 CDN 服务商的官方公网 IP 段（CIDR）列表。当前支持 CloudFlare、AWS CloudFront、Gcore 三家，覆盖 IPv4 与 IPv6。常用于 CDN 优选、反向代理、流量分流、防火墙白名单等运维场景。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/cdn-ips` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 2000 次；匿名 100 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/cdn-ips |
| Marketplace | https://apizero.cn/marketplace/cdn-ips |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| server | string | 是 | CDN 服务商：cloudflare / cloudfront / gcore（兼容 1/2/3 数字） |  |
| type | string | 是 | IP 协议版本：v4（IPv4）/ v6（IPv6） |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/cdn-ips?server=<server>&type=<type>"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "server": "CloudFlare",
    "type": "v4",
    "count": 15,
    "ips": [
      "173.245.48.0/20",
      "103.21.244.0/22",
      "103.22.200.0/22",
      "...（共 15 条）"
    ],
    "update_time": "2026-05-06 07:55:00"
  },
  "request_id": "mota...",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="browser-fingerprint"></a>

## 84. 浏览器指纹风控 `browser-fingerprint`

接收前端 SDK 采集的浏览器指纹（UA / Canvas / WebGL / 字体 / 时区 / 硬件 / WebDriver / 自动化标记等 20+ 维度），综合 9 类规则输出 0-100 风险评分、等级（safe/low/medium/high/critical）、命中的风险因子和异常项，识别爬虫、Headless Chrome、Selenium、虚拟机等异常环境。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/browser-fingerprint` |
| Method | `POST` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 50 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/browser-fingerprint |
| Marketplace | https://apizero.cn/marketplace/browser-fingerprint |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| ua | string | 是 | navigator.userAgent | Mozilla/5.0 ... |
| platform | string | 否 | navigator.platform |  |
| language | string | 否 | 主语言（如 zh-CN） |  |
| timezone | string | 否 | IANA 时区（如 Asia/Shanghai） |  |
| timezoneOffset | number | 否 | getTimezoneOffset()，分钟 |  |
| screenWidth | number | 否 | screen.width |  |
| screenHeight | number | 否 | screen.height |  |
| colorDepth | number | 否 | screen.colorDepth |  |
| pixelRatio | number | 否 | devicePixelRatio |  |
| hardwareConcurrency | number | 否 | navigator.hardwareConcurrency |  |
| deviceMemory | number | 否 | navigator.deviceMemory（GB） |  |
| maxTouchPoints | number | 否 | navigator.maxTouchPoints |  |
| canvasHash | string | 否 | Canvas 指纹哈希 |  |
| webglVendor | string | 否 | WebGL UNMASKED_VENDOR_WEBGL |  |
| webglRenderer | string | 否 | WebGL UNMASKED_RENDERER_WEBGL |  |
| webglHash | string | 否 | WebGL 参数哈希 |  |
| fonts | array | 否 | 检测到的字体列表 |  |
| fontCount | number | 否 | 字体数量 |  |
| plugins | array | 否 | 插件列表 |  |
| pluginCount | number | 否 | 插件数量 |  |
| webdriver | boolean | 否 | navigator.webdriver |  |
| automation | array | 否 | 检测到的自动化框架（如 selenium / phantom） |  |
| cookieEnabled | boolean | 否 | navigator.cookieEnabled |  |
| audioHash | string | 否 | AudioContext 指纹 |  |
| webrtcIPs | array | 否 | WebRTC 检测到的本机 IP |  |
| storageAvailable | array | 否 | 可用的存储类型 |  |
| permissions | array | 否 | 权限状态 |  |
| connection | object | 否 | navigator.connection 信息 |  |
| battery | object | 否 | 电池状态 |  |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| ua | string | 是 | navigator.userAgent | Mozilla/5.0 ... |
| platform | string | 否 | navigator.platform |  |
| language | string | 否 | 主语言（如 zh-CN） |  |
| timezone | string | 否 | IANA 时区（如 Asia/Shanghai） |  |
| timezoneOffset | number | 否 | getTimezoneOffset()，分钟 |  |
| screenWidth | number | 否 | screen.width |  |
| screenHeight | number | 否 | screen.height |  |
| colorDepth | number | 否 | screen.colorDepth |  |
| pixelRatio | number | 否 | devicePixelRatio |  |
| hardwareConcurrency | number | 否 | navigator.hardwareConcurrency |  |
| deviceMemory | number | 否 | navigator.deviceMemory（GB） |  |
| maxTouchPoints | number | 否 | navigator.maxTouchPoints |  |
| canvasHash | string | 否 | Canvas 指纹哈希 |  |
| webglVendor | string | 否 | WebGL UNMASKED_VENDOR_WEBGL |  |
| webglRenderer | string | 否 | WebGL UNMASKED_RENDERER_WEBGL |  |
| webglHash | string | 否 | WebGL 参数哈希 |  |
| fonts | array | 否 | 检测到的字体列表 |  |
| fontCount | number | 否 | 字体数量 |  |
| plugins | array | 否 | 插件列表 |  |
| pluginCount | number | 否 | 插件数量 |  |
| webdriver | boolean | 否 | navigator.webdriver |  |
| automation | array | 否 | 检测到的自动化框架（如 selenium / phantom） |  |
| cookieEnabled | boolean | 否 | navigator.cookieEnabled |  |
| audioHash | string | 否 | AudioContext 指纹 |  |
| webrtcIPs | array | 否 | WebRTC 检测到的本机 IP |  |
| storageAvailable | array | 否 | 可用的存储类型 |  |
| permissions | array | 否 | 权限状态 |  |
| connection | object | 否 | navigator.connection 信息 |  |
| battery | object | 否 | 电池状态 |  |

请求体示例：

```json
{
  "ua": "Mozilla/5.0 ...",
  "platform": "<platform>",
  "language": "<language>",
  "timezone": "<timezone>",
  "timezoneOffset": "<timezoneOffset>",
  "screenWidth": "<screenWidth>",
  "screenHeight": "<screenHeight>",
  "colorDepth": "<colorDepth>",
  "pixelRatio": "<pixelRatio>",
  "hardwareConcurrency": "<hardwareConcurrency>",
  "deviceMemory": "<deviceMemory>",
  "maxTouchPoints": "<maxTouchPoints>",
  "canvasHash": "<canvasHash>",
  "webglVendor": "<webglVendor>",
  "webglRenderer": "<webglRenderer>",
  "webglHash": "<webglHash>",
  "fonts": "<fonts>",
  "fontCount": "<fontCount>",
  "plugins": "<plugins>",
  "pluginCount": "<pluginCount>",
  "webdriver": "<webdriver>",
  "automation": "<automation>",
  "cookieEnabled": "<cookieEnabled>",
  "audioHash": "<audioHash>",
  "webrtcIPs": "<webrtcIPs>",
  "storageAvailable": "<storageAvailable>",
  "permissions": "<permissions>",
  "connection": "<connection>",
  "battery": "<battery>"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ua": "Mozilla/5.0 ...", "platform": "<platform>", "language": "<language>", "timezone": "<timezone>", "timezoneOffset": "<timezoneOffset>", "screenWidth": "<screenWidth>", "screenHeight": "<screenHeight>", "colorDepth": "<colorDepth>", "pixelRatio": "<pixelRatio>", "hardwareConcurrency": "<hardwareConcurrency>", "deviceMemory": "<deviceMemory>", "maxTouchPoints": "<maxTouchPoints>", "canvasHash": "<canvasHash>", "webglVendor": "<webglVendor>", "webglRenderer": "<webglRenderer>", "webglHash": "<webglHash>", "fonts": "<fonts>", "fontCount": "<fontCount>", "plugins": "<plugins>", "pluginCount": "<pluginCount>", "webdriver": "<webdriver>", "automation": "<automation>", "cookieEnabled": "<cookieEnabled>", "audioHash": "<audioHash>", "webrtcIPs": "<webrtcIPs>", "storageAvailable": "<storageAvailable>", "permissions": "<permissions>", "connection": "<connection>", "battery": "<battery>"}' \
  "https://v1.apizero.cn/api/browser-fingerprint"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "fingerprint_id": "a1b2c3d4...",
    "risk": 72,
    "risk_level": "high",
    "risk_label": "高风险",
    "factors": [
      {
        "name": "webdriver",
        "score": 30,
        "desc": "WebDriver 标记为 true"
      },
      {
        "name": "virtual_gpu",
        "score": 15,
        "desc": "WebGL 渲染器包含虚拟/软渲染特征: SwiftShader"
      }
    ],
    "anomalies": [
      "UA 声称 Windows 但 platform 不匹配"
    ],
    "device_profile": {
      "os": "Windows",
      "browser": "Chrome 125",
      "device_type": "Desktop",
      "screen": "1920x1080",
      "gpu": "ANGLE (NVIDIA, GeForce RTX 3060)",
      "cores": 8,
      "memory": "8GB",
      "fonts_count": 42,
      "plugins_count": 3,
      "touch": false
    },
    "timestamp": 1715097600
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="blood-type"></a>

## 85. 血型遗传查询 `blood-type`

根据父母血型查询子女可能/不可能的血型。基于 ABO 显性遗传规律，覆盖全部 16 种父母组合，毫秒级返回。常用于科普教育、亲子问答场景。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/blood-type` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 20000 次；匿名 10000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/blood-type |
| Marketplace | https://apizero.cn/marketplace/blood-type |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| father | string | 是 | 父亲血型，A / B / O / AB（大小写不敏感） | A |
| mother | string | 是 | 母亲血型，A / B / O / AB | B |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/blood-type?father=A&mother=B"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "father": "A",
    "mother": "B",
    "possible": [
      "A",
      "B",
      "AB",
      "O"
    ],
    "impossible": [],
    "summary": "子女可能为 A、B、AB、O 型血；无不可能的血型"
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="bodyfat"></a>

## 86. 体脂率与 BMI 计算 `bodyfat`

一站式综合计算 BMI、体脂率（Deurenberg 公式）、基础代谢率（Mifflin-St Jeor）、理想体重区间、腰围身高比与健康风险评估。男女区分阈值，附带专业建议。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/bodyfat` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 200000 次；匿名 100000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/bodyfat |
| Marketplace | https://apizero.cn/marketplace/bodyfat |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| weight | number | 是 | 体重（kg） | 70 |
| height | number | 是 | 身高（米，非厘米！） | 1.75 |
| waist | number | 是 | 腰围（cm） | 80 |
| gender | string | 是 | 性别：男/female/m/f | 男 |
| age | number | 否 | 年龄，默认 30 | 30 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/bodyfat?weight=70&height=1.75&waist=80&gender=男"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "bmi": 22.86,
    "bfp": 18.43,
    "bmr": 1632.5,
    "category": "正常",
    "ideal_weight_min": 56.66,
    "ideal_weight_max": 76.25,
    "waist_height_ratio": 0.46,
    "health_risk": "低",
    "advice": "体脂率正常，保持现有的生活方式。"
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="idcard-2c"></a>

## 87. 身份证二要素核验 `idcard-2c`

校验「真实姓名 + 18 位身份证号」是否与公安权威库一致，秒级返回。

适用于注册实名、下单风控、账户绑定等场景。仅返回是否一致，不返回任何额外户籍信息；身份证号在响应中脱敏回显。请在取得被核验人授权后调用。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/idcard-2c` |
| Method | `POST` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 按次付费 · 点数包 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户  次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/idcard-2c |
| Marketplace | https://apizero.cn/marketplace/idcard-2c |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 真实姓名（中文） | 张三 |
| idcard | string | 是 | 18 位身份证号（末位可为 X） | 11010519491231002X |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 真实姓名（中文） | 张三 |
| idcard | string | 是 | 18 位身份证号（末位可为 X） | 11010519491231002X |

请求体示例：

```json
{
  "name": "张三",
  "idcard": "11010519491231002X"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "张三", "idcard": "11010519491231002X"}' \
  "https://v1.apizero.cn/api/idcard-2c"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "name": "张三",
    "idcard": "110***********002X",
    "valid": true,
    "result_code": 100,
    "message": "一致"
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="domain-trade"></a>

## 88. 域名交易市场 `domain-trade`

拉取 EDNS 域名交易市场公开数据，支持按价格、长度、后缀、交易类型筛选。适合站长扫货短米、行业研究、域名估值参考。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/domain-trade` |
| Method | `GET` |
| 分类 | 金融数据 (`finance`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 200 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/domain-trade |
| Marketplace | https://apizero.cn/marketplace/domain-trade |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| page | number | 否 | 页码（默认 1） |  |
| pagesize | number | 否 | 每页数量（≤100，默认 50） |  |
| max_price | number | 否 | 最高价格（元） |  |
| max_length | number | 否 | 域名最大长度 |  |
| suffix | string | 否 | 后缀，如 .com |  |
| sale_type | string | 否 | 交易类型 |  |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/domain-trade?page=<page>&pagesize=<pagesize>"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "total_pages": 1234,
    "current_page": 1,
    "count": 50,
    "list": [
      {
        "name": "abc.com",
        "price": "5000",
        "sale_type": "一口价"
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="text-censor"></a>

## 89. 文本审核 `text-censor`

对文本进行多维度违规内容审核，覆盖政治敏感、谩骂、色情、违规广告、暴恐、低俗等类别，返回审核结论 + 命中违规词详情列表。

• 5000 字以内（中英文均按 1 字符计），单次请求审核
• 三态结论：合规（is_compliant=true）/ 不合规（is_compliant=false）/ 疑似（is_suspected=true，需人工复核）
• 详细命中信息：每条违规含 category（类别）/ word（触发词）/ level（等级）/ msg（说明）
• 衍生字段：violations（去重违规词数组）/ violation_categories（命中类别去重）/ violation_count（违规条数），前端可直接展示「触发 X 项违规：政治、谩骂…」
• 隐私保护：缓存 key 用 sha256 哈希，原文不进入 key；错误日志不记录文本内容

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/text-censor` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 100 次；匿名 30 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/text-censor |
| Marketplace | https://apizero.cn/marketplace/text-censor |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 待审核文本，1-5000 个字符（中英文均按 1 字符计） | 今天天气不错，适合出门散步。 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 待审核文本，1-5000 个字符（中英文均按 1 字符计） | 今天天气不错，适合出门散步。 |

请求体示例：

```json
{
  "text": "今天天气不错，适合出门散步。"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "今天天气不错，适合出门散步。"}' \
  "https://v1.apizero.cn/api/text-censor"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "text": "法轮功是邪教组织",
    "text_length": 8,
    "conclusion": "不合规",
    "conclusion_type": 2,
    "is_compliant": false,
    "is_suspected": false,
    "violation_count": 2,
    "violation_categories": [
      "政治"
    ],
    "violations": [
      "法轮功",
      "邪教"
    ],
    "details": [
      {
        "category": "政治",
        "level": 3,
        "word": "法轮功",
        "msg": "存在政治内容不合规"
      },
      {
        "category": "政治",
        "level": 3,
        "word": "邪教",
        "msg": "存在政治内容不合规"
      }
    ]
  },
  "request_id": "abc123def456",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="desensitize"></a>

## 90. 数据脱敏（敏感信息掩码） `desensitize`

自动检测并脱敏文本中的手机号、身份证（15/18 位）、银行卡（16-19 位）、邮箱、中文姓名等敏感信息。支持按类型组合，纯本地正则匹配，毫秒级返回。默认不回显原文，避免日志泄漏。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/desensitize` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 50 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/desensitize |
| Marketplace | https://apizero.cn/marketplace/desensitize |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 要脱敏的文本，最长 50000 字节 | 联系人：张先生，手机13800138000，身份证11010519491231002X，卡号6222021234567890123，邮箱zhangsan@example.com |
| types | string | 否 | 脱敏类型，此处固定 all（也支持逗号组合） | all |
| with_original | bool | 否 | 是否在 detections 中回显原文，默认 false | false |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 要脱敏的文本，最长 50000 字节 | 联系人：张先生，手机13800138000，身份证11010519491231002X，卡号6222021234567890123，邮箱zhangsan@example.com |
| types | string | 否 | 脱敏类型，此处固定 all（也支持逗号组合） | all |
| with_original | bool | 否 | 是否在 detections 中回显原文，默认 false | false |

请求体示例：

```json
{
  "text": "联系人：张先生，手机13800138000，身份证11010519491231002X，卡号6222021234567890123，邮箱zhangsan@example.com",
  "types": "all",
  "with_original": "false"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "联系人：张先生，手机13800138000，身份证11010519491231002X，卡号6222021234567890123，邮箱zhangsan@example.com", "types": "all", "with_original": "false"}' \
  "https://v1.apizero.cn/api/desensitize"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "masked_text": "联系人：张**，手机138****8000，身份证110105********002X，卡号6222 **** **** 0123，邮箱zh******@example.com",
    "detection_count": 5,
    "summary": {
      "idcard": 1,
      "bankcard": 1,
      "phone": 1,
      "email": 1,
      "name": 1
    },
    "detections": [
      {
        "type": "idcard",
        "masked": "110105********002X"
      },
      {
        "type": "bankcard",
        "masked": "6222 **** **** 0123"
      },
      {
        "type": "phone",
        "masked": "138****8000"
      },
      {
        "type": "email",
        "masked": "zh******@example.com"
      },
      {
        "type": "name",
        "masked": "张**"
      }
    ],
    "types_applied": [
      "phone",
      "idcard",
      "bankcard",
      "email",
      "name"
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-qrcode"></a>

## 91. 二维码识别 `ocr-qrcode`

上传含二维码或条形码的图片（URL 或 base64），自动识别并返回解码文本、码类型和四角位置。支持一图多码。

适用于扫码核销、仓储入库、海报解析、条码录入等场景。需要登录后使用，匿名不可调用。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-qrcode` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 10 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-qrcode |
| Marketplace | https://apizero.cn/marketplace/ocr-qrcode |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传入方式：url 或 base64。也可省略本字段，改传 url / image | url |
| input_data | string | 是 | 图片 URL 或 base64（jpg/png，可带 data:image 前缀，最大 10 MB）。兼容别名 url、image | https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fwww.apizero.cn |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传入方式：url 或 base64。也可省略本字段，改传 url / image | url |
| input_data | string | 是 | 图片 URL 或 base64（jpg/png，可带 data:image 前缀，最大 10 MB）。兼容别名 url、image | https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fwww.apizero.cn |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fwww.apizero.cn"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://api.qrserver.com/v1/create-qr-code/?size=200x200&data=https%3A%2F%2Fwww.apizero.cn"}' \
  "https://v1.apizero.cn/api/ocr-qrcode"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "count": 1,
    "items": [
      {
        "text": "https://www.apizero.cn/",
        "type": "qrcode",
        "position": {
          "left_top": {
            "x": 40.5,
            "y": 40.5
          },
          "right_top": {
            "x": 410.5,
            "y": 40.5
          },
          "right_bottom": {
            "x": 410.5,
            "y": 410.5
          },
          "left_bottom": {
            "x": 40.5,
            "y": 410.5
          }
        }
      }
    ]
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="csdn-profile"></a>

## 92. CSDN 博主信息 `csdn-profile`

通过 CSDN 用户名查询博主公开档案：昵称、头像、码龄、博客等级、原创数、粉丝数、博客排名、IP 属地、原力等级、勋章列表与成就明细。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/csdn-profile` |
| Method | `GET` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 200 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/csdn-profile |
| Marketplace | https://apizero.cn/marketplace/csdn-profile |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| username | string | 是 | CSDN 用户名（仅字母/数字/下划线） | weixin_44906759 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/csdn-profile?username=weixin_44906759"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "nickname": "XXX",
    "code_age_years": 5,
    "fans_count": 1234
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="dns-hijack"></a>

## 93. DNS 劫持检测 `dns-hijack`

通过对比 5 大公共 DoH（Cloudflare / Google / AliDNS / DNSPod / OpenDNS）对同一域名的解析结果，检测是否存在 DNS 劫持/污染/篡改。一致 = 安全，多源不一致 = 高风险。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/dns-hijack` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 5000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/dns-hijack |
| Marketplace | https://apizero.cn/marketplace/dns-hijack |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 域名（不含 https://） | baidu.com |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/dns-hijack?domain=baidu.com"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "domain": "baidu.com",
    "is_hijacked": false,
    "risk_level": "low",
    "summary": "5 个 DoH 服务商解析结果一致，未检测到劫持迹象",
    "unique_ips": [
      "110.242.68.3",
      "110.242.68.4"
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="app-store"></a>

## 94. App Store 查询 `app-store`

输入 App 数字 ID 或应用商店链接，查询 App Store 应用的名称、开发者、版本、评分、价格、截图、兼容性等完整信息。

支持全球多国家/地区（cn/us/jp 等）查询，可用于应用竞品分析、上架状态监控、ASO 运营、开发者工具集成等场景。数据实时聚合、结构清晰，数值/日期已标准化。完全免费。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/app-store` |
| Method | `POST` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 1000 次；匿名 500 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/app-store |
| Marketplace | https://apizero.cn/marketplace/app-store |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| app_id | string | 否 | App 数字 ID（与 url 二选一，优先） | 414478124 |
| url | string | 否 | 应用商店链接，自动提取数字 ID（与 app_id 二选一） | https://apps.apple.com/cn/app/id414478124 |
| country | string | 否 | 两位国家/地区码，非法自动回退 cn | cn |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| app_id | string | 否 | App 数字 ID（与 url 二选一，优先） | 414478124 |
| url | string | 否 | 应用商店链接，自动提取数字 ID（与 app_id 二选一） | https://apps.apple.com/cn/app/id414478124 |
| country | string | 否 | 两位国家/地区码，非法自动回退 cn | cn |

请求体示例：

```json
{
  "app_id": "414478124",
  "url": "https://apps.apple.com/cn/app/id414478124",
  "country": "cn"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"app_id": "414478124", "url": "https://apps.apple.com/cn/app/id414478124", "country": "cn"}' \
  "https://v1.apizero.cn/api/app-store"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "app_id": 414478124,
    "name": "微信",
    "bundle_id": "com.tencent.xin",
    "developer": {
      "name": "WeChat",
      "seller_name": "Tencent Technology (Shenzhen) Company Limited",
      "url": "https://.../developer/..."
    },
    "icon": {
      "small": "https://.../60x60.jpg",
      "medium": "https://.../100x100.jpg",
      "large": "https://.../512x512.jpg"
    },
    "price": {
      "amount": 0,
      "currency": "CNY",
      "formatted": "免费",
      "is_free": true
    },
    "version": {
      "current": "8.0.75",
      "release_date": "2026-06-14",
      "release_notes": "本次更新：解决了一些已知问题。",
      "days_since_update": 17
    },
    "rating": {
      "average": 4.15,
      "count": 8010302,
      "current_version_average": 4.15,
      "current_version_count": 8010302
    },
    "category": {
      "primary": "Social Networking",
      "primary_id": 6005,
      "all": [
        "社交",
        "效率"
      ]
    },
    "compatibility": {
      "min_os_version": "15.0",
      "supported_devices_count": 128,
      "features": [
        "iosUniversal"
      ],
      "game_center": false
    },
    "content_rating": "12+",
    "advisories": [],
    "file_size": {
      "bytes": 851213312,
      "display": "811.78 MB"
    },
    "description": "微信是一个生活方式……",
    "screenshots": {
      "iphone": [
        "https://.../1.jpg"
      ],
      "ipad": [],
      "appletv": []
    },
    "languages": [
      "ZH",
      "EN",
      "JA"
    ],
    "language_count": 25,
    "store_url": "https://apps.apple.com/cn/app/id414478124",
    "first_release_date": "2011-01-21",
    "country": "CN"
  },
  "request_id": "a1b2c3d4",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="douyin-search"></a>

## 95. 抖音视频搜索 `douyin-search`

按关键词搜索抖音公开视频，返回前 10～20 条视频页链接、标题、作者、点赞、时长与封面。

调用方传入抖音网页登录 Cookie（须含 sessionid），一条或多条均可；多条服务端轮询。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/douyin-search` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 8 req/s |
| 每日免费额度 | 登录用户 20 次；匿名 2 次 |
| 增长层级 | C-caution |
| 推广动作 | 只做排错/合规指南 |
| 推广角度 | 抖音搜索对输入和平台策略敏感，只讲合法查询和常见错误。 |
| 官网文档 | https://apizero.cn/aidocs/douyin-search |
| Marketplace | https://apizero.cn/marketplace/douyin-search |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| keyword | string | 是 | 搜索关键词，最长 40 字；兼容别名 q | 手机 |
| cookie | string | 是 | 一条或最多 20 条完整 Cookie（须含 sessionid）。单条文本 / JSON 对象均可；多条用 JSON 数组或 \ | \ |
| count | int | 否 | 返回条数 1–20，默认 10 | 10 |
| offset | int | 否 | 翻页起点，默认 0 | 0 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| keyword | string | 是 | 搜索关键词，最长 40 字；兼容别名 q | 手机 |
| cookie | string | 是 | 一条或最多 20 条完整 Cookie（须含 sessionid）。单条文本 / JSON 对象均可；多条用 JSON 数组或 \ | \ |
| count | int | 否 | 返回条数 1–20，默认 10 | 10 |
| offset | int | 否 | 翻页起点，默认 0 | 0 |

请求体示例：

```json
{
  "keyword": "手机",
  "cookie": "\\",
  "count": "10",
  "offset": "0"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "手机", "cookie": "\\", "count": "10", "offset": "0"}' \
  "https://v1.apizero.cn/api/douyin-search"
```

### 响应示例 `200`

```json
{
  "list": [
    {
      "title": "2026年618什么手机值得买？",
      "aweme_id": "7512345678901234567",
      "duration": 847,
      "cover_url": "https://p3-pc-sign.douyinpic.com/example.jpeg",
      "video_url": "https://www.douyin.com/video/7512345678901234567",
      "like_count": 116000,
      "author_name": "小白测评",
      "publish_time": "2026-05-20 12:00:00",
      "duration_text": "14:07"
    }
  ],
  "asked": 10,
  "count": 10,
  "keyword": "手机",
  "has_more": true,
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="cf-dns"></a>

## 96. Cloudflare DNS 更新（DDNS） `cf-dns`

通过用户自有的 Cloudflare API Token 更新指定域名的 A/AAAA 记录。家庭宽带 DDNS、办公室外网 IP 自动同步等场景必备。Token 仅作转发使用，不持久化。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/cf-dns` |
| Method | `POST` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 5000 次；匿名 1000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/cf-dns |
| Marketplace | https://apizero.cn/marketplace/cf-dns |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 根域名 | example.com |
| host | string | 是 | 主机记录 @ / www | home |
| ip | string | 是 | 要设置的 IP |  |
| token | string | 是 | Cloudflare API Token |  |
| type | string | 否 | A / AAAA（默认 A） |  |
| ttl | number | 否 | TTL 120-86400（默认 120） |  |
| proxied | bool | 否 | 是否启用 CDN 代理（默认 false） |  |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 根域名 | example.com |
| host | string | 是 | 主机记录 @ / www | home |
| ip | string | 是 | 要设置的 IP |  |
| token | string | 是 | Cloudflare API Token |  |
| type | string | 否 | A / AAAA（默认 A） |  |
| ttl | number | 否 | TTL 120-86400（默认 120） |  |
| proxied | bool | 否 | 是否启用 CDN 代理（默认 false） |  |

请求体示例：

```json
{
  "domain": "example.com",
  "host": "home",
  "ip": "<ip>",
  "token": "<token>",
  "type": "<type>",
  "ttl": "<ttl>",
  "proxied": "<proxied>"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "example.com", "host": "home", "ip": "<ip>", "token": "<token>", "type": "<type>", "ttl": "<ttl>", "proxied": "<proxied>"}' \
  "https://v1.apizero.cn/api/cf-dns"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "message": "DNS 记录更新成功",
    "full_name": "home.example.com",
    "type": "A",
    "old_ip": "1.2.3.4",
    "new_ip": "5.6.7.8",
    "changed": true
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-cn-passport"></a>

## 97. 中国护照识别 `ocr-cn-passport`

结构化识别中国护照，提取护照号码、中英文姓名、出生日期、有效期至、签发地点共 6 个关键字段。

适用场景：出行实名核验、酒店/机构入住登记、跨境业务证件录入等。护照属于高敏感度身份证件，仅限已登录用户调用，匿名访问不开放。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-cn-passport` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-cn-passport |
| Marketplace | https://apizero.cn/marketplace/ocr-cn-passport |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/passport.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/passport.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/passport.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/passport.jpg"}' \
  "https://v1.apizero.cn/api/ocr-cn-passport"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "passport_number": "E12345678",
    "full_name_cn": "张三",
    "full_name_en": "ZHANG SAN",
    "date_of_birth": "1990-01-01",
    "date_of_expiry": "2034-12-31",
    "place_of_issue": "上海"
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="user-info"></a>

## 98. 账户信息查询 `user-info`

用你自己的 API Key，查询自己账户还剩多少钱、还剩多少次、套餐哪天到期。给监控告警用：余额不够自动提醒，避免额度突然用完业务中断。

怎么用（三步）：
1）登录控制台 → API Key，复制一把 sk_live_ 开头的密钥；
2）请求 GET https://v1.apizero.cn/api/user-info ；
3）请求头写 Authorization: Bearer 你的Key。没有城市、条码这类查询参数，也不要传 user_id（传了也会被忽略，不能查别人）。

本接口只读，不扣费、不改账户。预付费可售 Key 只能看到这把 Key 还剩几次，看不到卖家钱包。请把 Key 放在请求头，不要写进网页或 URL。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/user-info` |
| Method | `GET` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 1 req/s |
| 每日免费额度 | 登录用户 720 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/user-info |
| Marketplace | https://apizero.cn/marketplace/user-info |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/user-info"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "scope": "account",
    "as_of": "2026-09-09T10:00:00+08:00",
    "balance": {
      "fen": 12340,
      "yuan": "123.4000"
    },
    "points": {
      "remaining": 80
    },
    "usage": {
      "today_calls": 12,
      "month_calls": 340,
      "month_spent": {
        "fen": 256.5,
        "yuan": "2.5650"
      }
    },
    "vip": {
      "level": "黄金会员",
      "level_num": 1,
      "active": true,
      "expire_at": "2026-10-01 23:59:59",
      "days_left": 22,
      "auto_renew": false,
      "month_calls_used": 3
    },
    "trial": {
      "remaining": 5,
      "granted": 20,
      "used": 15
    },
    "plans": [
      {
        "api_id": "weather",
        "name": "天气包月",
        "plan": "monthly",
        "used": 80,
        "quota": 3000,
        "remaining": 2920,
        "expire_at": "2026-10-09 12:00:00"
      }
    ],
    "key": {
      "id": "key_xxxx",
      "kind": "standard",
      "last4": "ab12",
      "daily_limit": null,
      "expires_at": null
    }
  },
  "request_id": "req_example",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="carrier-3c"></a>

## 99. 运营商三要素核验 `carrier-3c`

运营商三要素实名核验：一次校验「姓名 + 手机号 + 身份证号」三者是否一致，返回核验结论。

适用于账户实名、风控准入、身份一致性校验等场景。仅返回是否一致的结论，不返回、不存储任何明文个人信息；接口需登录并按次计费，请在取得信息主体明确授权后合规调用。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/carrier-3c` |
| Method | `POST` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 按次付费 · 点数包 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户  次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/carrier-3c |
| Marketplace | https://apizero.cn/marketplace/carrier-3c |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 真实姓名（中文）；兼容别名 realname / xm | 张三 |
| mobile | string | 是 | 11 位手机号；兼容别名 phone / sj | 13800138000 |
| idcard | string | 是 | 18 位身份证号（末位兼容 X）；兼容别名 id_card / sf | 110101199001011234 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 真实姓名（中文）；兼容别名 realname / xm | 张三 |
| mobile | string | 是 | 11 位手机号；兼容别名 phone / sj | 13800138000 |
| idcard | string | 是 | 18 位身份证号（末位兼容 X）；兼容别名 id_card / sf | 110101199001011234 |

请求体示例：

```json
{
  "name": "张三",
  "mobile": "13800138000",
  "idcard": "110101199001011234"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "张三", "mobile": "13800138000", "idcard": "110101199001011234"}' \
  "https://v1.apizero.cn/api/carrier-3c"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "name": "张三",
    "mobile": "138****0000",
    "idcard": "110***********001X",
    "match": true,
    "result": "三要素一致"
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="car-owner-check"></a>

## 100. 车牌车主核验 `car-owner-check`

车牌号与车主姓名一致性核验，快速判断二者是否匹配。

适用于二手车交易、租车、物流承运、金融风控等场景的车辆归属初步核验。仅返回「相符 / 不符」结论，不返回车主任何隐私详情。本接口为身份核验类敏感能力，需登录并携带 API Key 调用，按次计费。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/car-owner-check` |
| Method | `POST` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 按次付费 · 点数包 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户  次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/car-owner-check |
| Marketplace | https://apizero.cn/marketplace/car-owner-check |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| cp | string | 是 | 车牌号（中文省份简称开头 + 6~7 位字母数字）；兼容别名 plate | 京A12345 |
| m | string | 是 | 车主姓名；兼容别名 name / owner | 张三 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| cp | string | 是 | 车牌号（中文省份简称开头 + 6~7 位字母数字）；兼容别名 plate | 京A12345 |
| m | string | 是 | 车主姓名；兼容别名 name / owner | 张三 |

请求体示例：

```json
{
  "cp": "京A12345",
  "m": "张三"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cp": "京A12345", "m": "张三"}' \
  "https://v1.apizero.cn/api/car-owner-check"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "plate": "京A12345",
    "owner": "张三",
    "matched": true,
    "result": "此车牌号与车主相符"
  },
  "request_id": "abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="football"></a>

## 101. 足球赛事 `football`

按日期查询足球赛程与比分，覆盖英格兰、西班牙、意大利、德国、法国足球甲级联赛，以及欧洲冠军联赛、欧洲联赛、中国足球协会超级联赛、英格兰足球协会挑战杯、国际足联世界杯。返回开赛时间、比分、比赛状态与场馆，不含赔率或门票。

调用说明：
1）默认 POST /api/football，查询北京时间当日主流联赛；
2）按子接口分别查询进行中、未开赛、已结束，或指定联赛；
3）联赛列表子接口返回联赛代码与名称，不请求上游数据源。

时间均为北京时间。赛程缓存约 45 秒。登录每日 20 次；黄金 4000、钻石 8000；企业走额度。单用户 QPS 与条码查询同档。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/football` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 按次付费 · 点数包 · VIP |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名 5 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 足球赛事赛程；适合比分看板和赛程提醒。 |
| 官网文档 | https://apizero.cn/aidocs/football |
| Marketplace | https://apizero.cn/marketplace/football |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| date | string | 否 | 比赛日期。格式 YYYY-MM-DD 或 YYYYMMDD，缺省为北京时间当日。 | 2026-09-12 |
| limit | int | 否 | 返回条数。取值范围 1–200，缺省 80。 | 80 |
| status | string | 否 | 比赛状态。本子接口取值为 live（进行中）。 | live |
| league | string | 否 | 联赛代码。用于限定单一联赛；缺省为全部已覆盖联赛。 | epl |
| action | string | 否 | 操作类型。本子接口取值为 leagues（返回联赛目录）。 | leagues |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| date | string | 否 | 比赛日期。格式 YYYY-MM-DD 或 YYYYMMDD，缺省为北京时间当日。 | 2026-09-12 |
| limit | int | 否 | 返回条数。取值范围 1–200，缺省 80。 | 80 |
| status | string | 否 | 比赛状态。本子接口取值为 live（进行中）。 | live |
| league | string | 否 | 联赛代码。用于限定单一联赛；缺省为全部已覆盖联赛。 | epl |
| action | string | 否 | 操作类型。本子接口取值为 leagues（返回联赛目录）。 | leagues |

请求体示例：

```json
{
  "date": "2026-09-12",
  "limit": "80",
  "status": "live",
  "league": "epl",
  "action": "leagues"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"date": "2026-09-12", "limit": "80", "status": "live", "league": "epl", "action": "leagues"}' \
  "https://v1.apizero.cn/api/football"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "summary": {
      "sport": "football",
      "date": "2026-09-12",
      "league": "all",
      "status": "all",
      "count": 1,
      "total": 7,
      "live": 0,
      "generated_at": "2026-09-11 17:40:00"
    },
    "matches": [
      {
        "id": "401879285",
        "league": "epl",
        "league_name": "英超",
        "start_at": "2026-09-12 22:00:00",
        "status": "upcoming",
        "status_text": "未开赛",
        "venue": "Vitality Stadium",
        "home": {
          "name": "AFC Bournemouth",
          "short": "BOU",
          "score": 0
        },
        "away": {
          "name": "Brentford",
          "short": "BRE",
          "score": 0
        }
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-bank-card"></a>

## 102. 银行卡识别 `ocr-bank-card`

识别银行卡图片中的卡号与有效期，支持 URL 和 base64 两种输入方式。

适用场景：在线开户填卡、支付绑卡辅助录入、卡号核对等。支持 jpg/png 格式，文件大小不超过 10MB，建议图片清晰、卡面完整以提高识别率。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-bank-card` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-bank-card |
| Marketplace | https://apizero.cn/marketplace/ocr-bank-card |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片二进制的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填写 http/https 图片链接；input_type=base64 时填写 base64 字符串（可含 data:image/xxx;base64, 前缀），文件大小不超过 10MB | https://example.com/bankcard.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片二进制的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填写 http/https 图片链接；input_type=base64 时填写 base64 字符串（可含 data:image/xxx;base64, 前缀），文件大小不超过 10MB | https://example.com/bankcard.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/bankcard.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/bankcard.jpg"}' \
  "https://v1.apizero.cn/api/ocr-bank-card"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "card_number": "6222 0202 0001 5920 8",
    "date_of_expiry": "12/28"
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ios-cert"></a>

## 103. iOS 证书与描述文件检测 `ios-cert`

解析 .p12 证书与 .mobileprovision 描述文件，输出证书有效期、吊销状态、Team ID、证书类型（开发/分发/企业）、设备列表、25 项 entitlements 权限以及证书与描述文件匹配性验证。iOS 开发者必备。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ios-cert` |
| Method | `POST` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 10000 次；匿名 5000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ios-cert |
| Marketplace | https://apizero.cn/marketplace/ios-cert |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| cert | string | 是 | Base64 编码的 .p12 文件内容 |  |
| provision | string | 是 | Base64 编码的 .mobileprovision |  |
| password | string | 否 | 证书密码，默认为空 |  |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| cert | string | 是 | Base64 编码的 .p12 文件内容 |  |
| provision | string | 是 | Base64 编码的 .mobileprovision |  |
| password | string | 否 | 证书密码，默认为空 |  |

请求体示例：

```json
{
  "cert": "<cert>",
  "provision": "<provision>",
  "password": "<password>"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cert": "<cert>", "provision": "<provision>", "password": "<password>"}' \
  "https://v1.apizero.cn/api/ios-cert"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "certificate": {
      "name": "iPhone Developer: ...",
      "status": "正常",
      "is_revoked": false
    },
    "mobileprovision": {
      "cert_type": "Development",
      "cert_end_days": 350
    },
    "permissions": {
      "aps": true,
      "keychain": true,
      "debug": true
    },
    "is_matching": true
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-train-ticket"></a>

## 104. 火车票识别 `ocr-train-ticket`

结构化识别国内全类型火车票（含高铁、动车、普通车票），提取出发/到达站、车次、姓名、座位号、票价、出发时间、身份证号、售卖站等 13 个字段。

适用场景：差旅费报销自动录入、行程管理、票据核对等。因返回内容含姓名和身份证号，仅限已登录用户调用，匿名访问不开放。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-train-ticket` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-train-ticket |
| Marketplace | https://apizero.cn/marketplace/ocr-train-ticket |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/train-ticket.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/train-ticket.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/train-ticket.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/train-ticket.jpg"}' \
  "https://v1.apizero.cn/api/ocr-train-ticket"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "start_station": "北京南",
    "end_station": "上海虹桥",
    "train_num": "G101",
    "time": "2024-01-15 09:00",
    "seat_cls": "二等座",
    "seat_num": "05车12A号",
    "name": "张三",
    "id_num": "110101199001011234",
    "ticket_num": "E123456789",
    "total_amount": "￥553.00",
    "price": "553.00",
    "sale_station": "北京南",
    "sale_num": "G123456"
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-vehicle-license"></a>

## 105. 行驶证识别 `ocr-vehicle-license`

结构化识别行驶证，提取号牌号码、车辆类型、所有人、住址、品牌型号、VIN、发动机号、注册日期、总质量、核定载质量、外廓尺寸、检验记录等 20 个字段。

适用场景：二手车交易核验、车辆过户信息录入、保险投保材料自动提取等。含所有人姓名及住址，仅限已登录用户调用，匿名访问不开放。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-vehicle-license` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-vehicle-license |
| Marketplace | https://apizero.cn/marketplace/ocr-vehicle-license |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/vehicle-license.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/vehicle-license.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/vehicle-license.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/vehicle-license.jpg"}' \
  "https://v1.apizero.cn/api/ocr-vehicle-license"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "plate_number": "沪A12345",
    "vehicle_type": "小型轿车",
    "owner": "张三",
    "address": "上海市XX路XX号",
    "use_character": "非营运",
    "model": "丰田CAMRY",
    "vin": "LSXXXXXXXXXXXXXXXXX",
    "engine_number": "4A123456",
    "register_date": "2020-06-01",
    "issue_date": "2020-06-05",
    "license_issuing_authority": "上海市公安局交通警察总队",
    "document_id": "SHXXXXXXXXXX",
    "approved_passengers_capacity": "5人",
    "total_mass": "1945",
    "curb_weight": "1495",
    "ratified_load_capacity": "",
    "gabarite": "4885x1840x1455",
    "traction_mass": "",
    "remarks": "",
    "inspection_record": "2022 2024"
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-tw-permit"></a>

## 106. 台胞证识别 `ocr-tw-permit`

结构化识别台湾居民来往大陆通行证（台胞证），提取中文姓名、英文姓名、出生日期、证件号码、有效期共 5 个关键字段。

适用场景：台湾居民实名认证、酒店入住登记、证件信息自动录入等。涉及个人身份信息，仅限已登录用户调用，匿名访问不开放。支持 URL 和 base64 两种输入方式，jpg/png 格式，建议证件图片完整清晰。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-tw-permit` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-tw-permit |
| Marketplace | https://apizero.cn/marketplace/ocr-tw-permit |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/tw-permit.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/tw-permit.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/tw-permit.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/tw-permit.jpg"}' \
  "https://v1.apizero.cn/api/ocr-tw-permit"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "full_name_cn": "张三",
    "full_name_en": "ZHANG SAN",
    "date_of_birth": "1990-01-01",
    "date_of_expiry": "2029-12-31",
    "card_number": "12345678901234567"
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-vehicle-invoice"></a>

## 107. 机动车发票识别 `ocr-vehicle-invoice`

结构化识别机动车销售发票，提取发票代码、号码、开票日期、购买方/销售方信息、车辆信息及价税明细等 20 个字段。

适用场景：二手车交易核验、购车报销录入、增值税抵扣材料整理等。支持 jpg/png 格式，文件大小不超过 10MB，建议发票平整、拍摄清晰以提高识别准确率。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-vehicle-invoice` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-vehicle-invoice |
| Marketplace | https://apizero.cn/marketplace/ocr-vehicle-invoice |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀），文件大小不超过 10MB | https://example.com/vehicle-invoice.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀），文件大小不超过 10MB | https://example.com/vehicle-invoice.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/vehicle-invoice.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/vehicle-invoice.jpg"}' \
  "https://v1.apizero.cn/api/ocr-vehicle-invoice"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "invoice_code": "31100000000",
    "invoice_num": "12345678",
    "date": "2024年01月15日",
    "print_code": "",
    "print_num": "",
    "machine_num": "499098765432",
    "buyer_name": "张三",
    "buyer_id": "",
    "vehicle_type": "小型轿车",
    "product_model": "丰田/CAMRY",
    "certificate_num": "LSXXXXXXXXXXXXX",
    "vin": "4A123456",
    "total_price": "壹拾柒万元整",
    "total_price_little": "170000.00",
    "tax_rate": "9%",
    "tax": "13944.95",
    "price": "156055.05",
    "saler_name": "XX汽车销售有限公司",
    "saler_id": "91310000XXXXXXXXXX",
    "saler_addr": "上海市XX路XX号 021-XXXXXXXX"
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="contact-parse"></a>

## 108. 联系人三要素解析 `contact-parse`

从乱序文本中抽取姓名、电话号码、地址，顺序任意

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/contact-parse` |
| Method | `POST` |
| 分类 | 地理位置 (`geo`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 500 次；匿名 100 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/contact-parse |
| Marketplace | https://apizero.cn/marketplace/contact-parse |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 乱序联系人文本，含姓名/电话/地址即可，顺序不限，长度 ≤ 1000。兼容 q / content / address | 魔法师 12345678901 广西桂林市秀峰区xx路yy号 |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| text | string | 是 | 乱序联系人文本，含姓名/电话/地址即可，顺序不限，长度 ≤ 1000。兼容 q / content / address | 魔法师 12345678901 广西桂林市秀峰区xx路yy号 |

请求体示例：

```json
{
  "text": "魔法师 12345678901 广西桂林市秀峰区xx路yy号"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"text": "魔法师 12345678901 广西桂林市秀峰区xx路yy号"}' \
  "https://v1.apizero.cn/api/contact-parse"
```

### 响应示例 `200`

```json
{
  "name": "魔法师",
  "phone": "12345678901",
  "address": "广西桂林市秀峰区xx路yy号",
  "original": "魔法师 12345678901 广西桂林市秀峰区xx路yy号",
  "formatted": "姓名=魔法师，电话号码=12345678901，地址=广西桂林市秀峰区xx路yy号",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="idcard-face-3c"></a>

## 109. 人像三要素核验 `idcard-face-3c`

将「真实姓名 + 身份证号 + 人脸照片」与公安库身份证头像做 1:1 比对，返回是否一致及相似度。适用于实名认证、开户核身等场景。请在取得被核验人授权后调用。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/idcard-face-3c` |
| Method | `POST` |
| 分类 | 身份核验 (`kyc`) |
| 计费 | 按次付费 · 点数包 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户  次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/idcard-face-3c |
| Marketplace | https://apizero.cn/marketplace/idcard-face-3c |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 真实姓名（中文），兼容别名 realname | 张三 |
| idcard | string | 是 | 18 位身份证号（末位可为 X），兼容别名 id_card | 11010519491231002X |
| image | string | 是 | 人脸照片 base64（可带 data URL 前缀），兼容别名 face_image | data:image/jpeg;base64,... |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 真实姓名（中文），兼容别名 realname | 张三 |
| idcard | string | 是 | 18 位身份证号（末位可为 X），兼容别名 id_card | 11010519491231002X |
| image | string | 是 | 人脸照片 base64（可带 data URL 前缀），兼容别名 face_image | data:image/jpeg;base64,... |

请求体示例：

```json
{
  "name": "张三",
  "idcard": "11010519491231002X",
  "image": "data:image/jpeg;base64,..."
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "张三", "idcard": "11010519491231002X", "image": "data:image/jpeg;base64,..."}' \
  "https://v1.apizero.cn/api/idcard-face-3c"
```

### 响应示例 `200`



<a id="ocr-taxi-invoice"></a>

## 110. 出租车发票识别 `ocr-taxi-invoice`

结构化识别全国出租车机打发票，提取车号、上下车时间、里程、金额、发票代码/号码、单价、附加费、印章信息等 16 个字段。

适用场景：差旅费报销自动录入、行程费用核对、财务审计等。支持 URL 和 base64 两种输入方式，发票图片建议拍摄平整清晰。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-taxi-invoice` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-taxi-invoice |
| Marketplace | https://apizero.cn/marketplace/ocr-taxi-invoice |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/taxi-invoice.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传输方式，支持 url（公网图片地址）或 base64（图片的 base64 编码） | url |
| input_data | string | 是 | 图片内容：input_type=url 时填 http/https 图片链接；input_type=base64 时填 base64 字符串（可含 data:image/xxx;base64, 前缀） | https://example.com/taxi-invoice.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/taxi-invoice.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/taxi-invoice.jpg"}' \
  "https://v1.apizero.cn/api/ocr-taxi-invoice"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "invoice_code": "31100000000",
    "invoice_no": "87654321",
    "title_trial": "出租汽车发票",
    "car_number": "沪A12345",
    "start_date": "2024-01-15",
    "start_time": "09:30",
    "end_time": "10:05",
    "distance": "12.3",
    "total_amount": "38.50",
    "price": "3.00",
    "dispatch_fee": "",
    "additional_fee": "1.00",
    "is_sealed": "true",
    "seller_name_in_seal": "XX出租汽车有限公司",
    "seller_taxpayer_no_in_seal": "91310000XXXXXXXXXX",
    "invoice_special_seal": "XX出租汽车发票专用章"
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="basketball"></a>

## 111. 篮球赛事 `basketball`

按日期查询篮球赛程与比分，覆盖美国男子职业篮球联赛、美国女子职业篮球联赛、美国大学体育协会男子篮球联赛、中国男子篮球职业联赛。返回开赛时间、比分、比赛状态与场馆，不含赔率或门票。

调用说明：
1）默认 POST /api/basketball，查询北京时间当日 NBA 与 WNBA；
2）按子接口分别查询进行中、未开赛、已结束，或指定联赛；
3）联赛列表子接口返回联赛代码与名称，不请求上游数据源。

时间均为北京时间。赛程缓存约 45 秒。登录每日 20 次；黄金 4000、钻石 8000；企业走额度。单用户 QPS 与条码查询同档。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/basketball` |
| Method | `POST` |
| 分类 | 生活服务 (`life`) |
| 计费 | 按次付费 · 点数包 · VIP |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名 5 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 篮球赛事赛程；适合 NBA/CBA 看板。 |
| 官网文档 | https://apizero.cn/aidocs/basketball |
| Marketplace | https://apizero.cn/marketplace/basketball |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| date | string | 否 | 比赛日期。格式 YYYY-MM-DD 或 YYYYMMDD，缺省为北京时间当日。 | 2026-09-11 |
| limit | int | 否 | 返回条数。取值范围 1–200，缺省 80。 | 80 |
| status | string | 否 | 比赛状态。本子接口取值为 live（进行中）。 | live |
| league | string | 否 | 联赛代码。用于限定单一联赛；缺省为全部已覆盖联赛。 | nba |
| action | string | 否 | 操作类型。本子接口取值为 leagues（返回联赛目录）。 | leagues |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| date | string | 否 | 比赛日期。格式 YYYY-MM-DD 或 YYYYMMDD，缺省为北京时间当日。 | 2026-09-11 |
| limit | int | 否 | 返回条数。取值范围 1–200，缺省 80。 | 80 |
| status | string | 否 | 比赛状态。本子接口取值为 live（进行中）。 | live |
| league | string | 否 | 联赛代码。用于限定单一联赛；缺省为全部已覆盖联赛。 | nba |
| action | string | 否 | 操作类型。本子接口取值为 leagues（返回联赛目录）。 | leagues |

请求体示例：

```json
{
  "date": "2026-09-11",
  "limit": "80",
  "status": "live",
  "league": "nba",
  "action": "leagues"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"date": "2026-09-11", "limit": "80", "status": "live", "league": "nba", "action": "leagues"}' \
  "https://v1.apizero.cn/api/basketball"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "summary": {
      "sport": "basketball",
      "date": "2026-09-11",
      "league": "nba",
      "status": "all",
      "count": 1,
      "total": 1,
      "live": 0,
      "generated_at": "2026-09-11 17:40:00"
    },
    "matches": [
      {
        "id": "401810001",
        "league": "nba",
        "league_name": "NBA",
        "start_at": "2026-09-11 09:00:00",
        "status": "finished",
        "status_text": "已结束",
        "venue": "Crypto.com Arena",
        "home": {
          "name": "Los Angeles Lakers",
          "short": "LAL",
          "score": 112
        },
        "away": {
          "name": "Golden State Warriors",
          "short": "GSW",
          "score": 108
        }
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="code-beautify"></a>

## 112. 代码美化图片 `code-beautify`

将代码片段渲染为精美的SVG/PNG卡片图片。支持16种编程语言语法高亮、8套设计主题，适合社交分享和技术文档配图。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/code-beautify` |
| Method | `POST` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 3000 次；匿名 2000 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/code-beautify |
| Marketplace | https://apizero.cn/marketplace/code-beautify |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| code | string | 是 | 代码内容 | const sum = (a, b) => a + b; |
| language | string | 否 | 语言：auto/python/javascript/typescript/json/bash/go/rust/java/c/cpp/html/css/sql/yaml/markdown | typescript |
| theme | string | 否 | 主题：aurora/sunset/forest/midnight/rose/ocean/volcano/mono | aurora |
| title | string | 否 | 卡片顶部标题 | snippet.ts |
| line_numbers | int | 否 | 是否显示行号 1/0 | 1 |
| scale | int | 否 | PNG放大倍数 1-4 | 2 |
| output | string | 否 | 输出格式：svg/png/json | json |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| code | string | 是 | 代码内容 | const sum = (a, b) => a + b; |
| language | string | 否 | 语言：auto/python/javascript/typescript/json/bash/go/rust/java/c/cpp/html/css/sql/yaml/markdown | typescript |
| theme | string | 否 | 主题：aurora/sunset/forest/midnight/rose/ocean/volcano/mono | aurora |
| title | string | 否 | 卡片顶部标题 | snippet.ts |
| line_numbers | int | 否 | 是否显示行号 1/0 | 1 |
| scale | int | 否 | PNG放大倍数 1-4 | 2 |
| output | string | 否 | 输出格式：svg/png/json | json |

请求体示例：

```json
{
  "code": "const sum = (a, b) => a + b;",
  "language": "typescript",
  "theme": "aurora",
  "title": "snippet.ts",
  "line_numbers": "1",
  "scale": "2",
  "output": "json"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "const sum = (a, b) => a + b;", "language": "typescript", "theme": "aurora", "title": "snippet.ts", "line_numbers": "1", "scale": "2", "output": "json"}' \
  "https://v1.apizero.cn/api/code-beautify"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "language": "typescript",
    "theme": "aurora",
    "theme_name": "极光",
    "title": "snippet.ts",
    "line_count": 3,
    "width": 680,
    "height": 180,
    "svg": "<svg>...</svg>",
    "png_base64": "iVBORw0..."
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="driving-license"></a>

## 113. 驾驶证识别 `driving-license`

上传驾驶证图片（URL 或 base64），自动识别证件字段，包括证号、姓名、性别、国籍、住址、出生日期、准驾车型、有效期等共 12 个关键字段信息。

适用于网约车平台司机资质核验、二手车交易身份核实、物流企业驾照信息录入等场景。支持 JPG / PNG / BMP，图片建议清晰、无遮挡。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/driving-license` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/driving-license |
| Marketplace | https://apizero.cn/marketplace/driving-license |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传入方式 | url |
| input_data | string | 是 | 图片 URL 或 base64 编码字符串（base64 最大 5 MB） | https://example.com/driving-license.jpg |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传入方式 | url |
| input_data | string | 是 | 图片 URL 或 base64 编码字符串（base64 最大 5 MB） | https://example.com/driving-license.jpg |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://example.com/driving-license.jpg"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://example.com/driving-license.jpg"}' \
  "https://v1.apizero.cn/api/driving-license"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "id_number": "310***********1234",
    "name": "张三",
    "sex": "男",
    "nationality": "中国",
    "address": "上海市浦东新区",
    "date_of_birth": "1990-01-01",
    "date_of_first_issue": "2010-05-20",
    "class": "C1",
    "valid_begin": "2020-05-20",
    "valid_end": "2026-05-20",
    "license_issuing_authority": "上海市公安局交通警察总队",
    "id_photo_location": "{\"x\":10,\"y\":10,\"w\":80,\"h\":100}"
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="drug-insert"></a>

## 114. 药品说明书查询 `drug-insert`

按药品名称搜索成药说明书，或用说明书 ID 拉取结构化全文（适应症、用法用量、不良反应、禁忌等）。

- 先用 `name` 搜索，从 `list[].id` 取说明书 ID
- 再用 `id` 拉详情；`sections` 按原文小节返回
- 一次搜索最多约 50 条；未命中时 `found=false`，不是错误
- 仅供信息参考，不能替代执业医师 / 药师指导，也不能替代药盒说明书

【调用额度说明】
本接口额度以本页为准（与平台 VIP 在多数接口上的默认日免费额度不同）：
- 匿名试用：每日 2 次
- 登录免费：每日 5 次
- 黄金 VIP：每日 5,000 次
- 企业 VIP：按平台 VIP 日额度
- 高频场景：建议购买本接口基础版月卡 / 年卡（更高总量与 QPS）；超出后也可按次计费

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/drug-insert` |
| Method | `GET` |
| 分类 | 生活服务 (`life`) |
| 计费 | 按次付费 · 点数包 · 月套餐 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 5 次；匿名 2 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | 药品说明书查询；先搜名称再拉详情，适合健康工具教程。 |
| 官网文档 | https://apizero.cn/aidocs/drug-insert |
| Marketplace | https://apizero.cn/marketplace/drug-insert |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| name | string | 是 | 药品名称关键词，1–50 字 | 阿莫西林 |
| id | string | 是 | 搜索结果返回的说明书 ID | sms125387 |

### cURL 模板

```bash
curl -sS \
  -X GET \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  "https://v1.apizero.cn/api/drug-insert?name=阿莫西林"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "mode": "search",
    "query": "阿莫西林",
    "found": true,
    "total": 3,
    "list": [
      {
        "id": "sms125387",
        "name": "阿莫西林胶囊",
        "approval_no": "国药准字H14023222",
        "indications": "阿莫西林适用于敏感菌（不产β内酰胺酶菌株）所致的下列感染：1.溶血链球菌、肺炎链球菌、葡萄球菌或流感嗜血杆菌所致中耳炎、鼻窦炎、咽炎、扁桃体炎等上呼吸道感染。"
      },
      {
        "id": "sms125344",
        "name": "阿莫西林胶囊",
        "approval_no": "国药准字H13020473",
        "indications": "阿莫西林适用于敏感菌（不产β内酰胺酶菌株）所致的下列感染。"
      },
      {
        "id": "sms125093",
        "name": "阿莫西林克拉维酸钾颗粒",
        "approval_no": "国药准字H20163326",
        "indications": "本品适用于产酶流感嗜血杆菌和卡他莫拉菌所致的下呼吸道感染，中耳炎、鼻窦炎。"
      }
    ]
  },
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ocr-text-box"></a>

## 115. OCR 文字坐标识别 `ocr-text-box`

从图片识别文字，并返回每条文字在原图上的像素坐标（外接矩形 rect + 四点 box）。适合图片编辑：定位后盖字、换字、打码。

和「OCR 文字识别」是两个接口：旧接口只回文字，本接口多回坐标。参数一样，还是 input_type + input_data。

坐标系：原图左上角为 (0,0)，单位像素。image.width / image.height 是原图宽高，请按这两项对齐你的画布。

额度比普通 OCR 略少：未登录每天 40 次，登录每天 200 次，黄金每天 4 万次，钻石每天 8 万次。超出按 0.02 元/次（也可用点数）。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/ocr-text-box` |
| Method | `POST` |
| 分类 | 文档识别 (`ocrdata`) |
| 计费 | 按次付费 · 点数包 · VIP |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 200 次；匿名 40 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ocr-text-box |
| Marketplace | https://apizero.cn/marketplace/ocr-text-box |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传入方式：url 或 base64 | url |
| input_data | string | 是 | 图片 URL（http/https）或 base64（可带 data:image 前缀，最大 10 MB） | https://dummyimage.com/400x100/000/fff.png&text=Hello |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| input_type | string | 是 | 图片传入方式：url 或 base64 | url |
| input_data | string | 是 | 图片 URL（http/https）或 base64（可带 data:image 前缀，最大 10 MB） | https://dummyimage.com/400x100/000/fff.png&text=Hello |

请求体示例：

```json
{
  "input_type": "url",
  "input_data": "https://dummyimage.com/400x100/000/fff.png&text=Hello"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"input_type": "url", "input_data": "https://dummyimage.com/400x100/000/fff.png&text=Hello"}' \
  "https://v1.apizero.cn/api/ocr-text-box"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "input_type": "url",
    "image": {
      "width": 906,
      "height": 1280
    },
    "text_count": 2,
    "items": [
      {
        "index": 0,
        "text": "拒绝褶皱告别尴尬",
        "score": 0.9876,
        "rect": {
          "x": 80,
          "y": 36,
          "width": 740,
          "height": 88
        },
        "box": [
          [
            80,
            36
          ],
          [
            820,
            40
          ],
          [
            818,
            124
          ],
          [
            78,
            120
          ]
        ]
      },
      {
        "index": 1,
        "text": "抗皱黑科技",
        "score": 0.9812,
        "rect": {
          "x": 620,
          "y": 690,
          "width": 210,
          "height": 48
        },
        "box": [
          [
            620,
            690
          ],
          [
            830,
            692
          ],
          [
            828,
            738
          ],
          [
            618,
            736
          ]
        ]
      }
    ],
    "full_text": "拒绝褶皱告别尴尬\n抗皱黑科技"
  },
  "request_id": "req_example",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="dns-lookup"></a>

## 116. DNS 查询 `dns-lookup`

零依赖DNS查询API。自实现DNS协议（RFC 1035），支持A/AAAA/MX/TXT/CNAME/NS/SOA/SRV/PTR/CAA记录类型，UDP自动fallback到DoH（DNS over HTTPS）防劫持。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/dns-lookup` |
| Method | `POST` |
| 分类 | 开发工具 (`dev`) |
| 计费 | 完全免费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户 500 次；匿名 300 次 |
| 增长层级 | B-support |
| 推广动作 | 补充推广 |
| 推广角度 | DNS 查询 API；适合开发者工具、域名诊断、运维脚本。 |
| 官网文档 | https://apizero.cn/aidocs/dns-lookup |
| Marketplace | https://apizero.cn/marketplace/dns-lookup |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 要查询的域名（别名 name/host） | example.com |
| type | string | 否 | 记录类型，逗号分隔；ALL=A,AAAA,MX,TXT,CNAME | A |
| server | string | 否 | 指定DNS服务器（逗号分隔） | 8.8.8.8,1.1.1.1 |
| timeout | int | 否 | 单请求超时秒（1~30） | 5 |
| doh | int | 否 | 1=强制走DoH（HTTPS） | 0 |
| doh_provider | string | 否 | DoH服务商：cloudflare/google/alibaba | cloudflare |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| domain | string | 是 | 要查询的域名（别名 name/host） | example.com |
| type | string | 否 | 记录类型，逗号分隔；ALL=A,AAAA,MX,TXT,CNAME | A |
| server | string | 否 | 指定DNS服务器（逗号分隔） | 8.8.8.8,1.1.1.1 |
| timeout | int | 否 | 单请求超时秒（1~30） | 5 |
| doh | int | 否 | 1=强制走DoH（HTTPS） | 0 |
| doh_provider | string | 否 | DoH服务商：cloudflare/google/alibaba | cloudflare |

请求体示例：

```json
{
  "domain": "example.com",
  "type": "A",
  "server": "8.8.8.8,1.1.1.1",
  "timeout": "5",
  "doh": "0",
  "doh_provider": "cloudflare"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "example.com", "type": "A", "server": "8.8.8.8,1.1.1.1", "timeout": "5", "doh": "0", "doh_provider": "cloudflare"}' \
  "https://v1.apizero.cn/api/dns-lookup"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "domain": "example.com",
    "type": "A",
    "server": "114.114.114.114",
    "transport": "udp",
    "rcode": 0,
    "rcode_text": "NOERROR",
    "elapsed_ms": 32,
    "answers": [
      {
        "type": "A",
        "name": "example.com",
        "ttl": 300,
        "value": "93.184.216.34"
      }
    ],
    "truncated": false
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="bili-danmaku"></a>

## 117. B站弹幕分析 `bili-danmaku`

输入B站BV/AV号，拉取视频弹幕并分析高频重复弹幕、热词/梗、整体情感倾向（正向/负向/中性）。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/api/bili-danmaku` |
| Method | `POST` |
| 分类 | 内容娱乐 (`content`) |
| 计费 | 完全免费 |
| QPS | 2 req/s |
| 每日免费额度 | 登录用户 20 次；匿名 10 次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/bili-danmaku |
| Marketplace | https://apizero.cn/marketplace/bili-danmaku |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| video | string | 是 | AV号或BV号 | BV1w8RBBUEYy |
| limit | int | 否 | 返回高频弹幕/热词数量 | 10 |
| timeout | int | 否 | 超时秒数 | 15 |
| page_mode | string | 否 | all=抓全部分P / first=只抓第一页 | all |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| video | string | 是 | AV号或BV号 | BV1w8RBBUEYy |
| limit | int | 否 | 返回高频弹幕/热词数量 | 10 |
| timeout | int | 否 | 超时秒数 | 15 |
| page_mode | string | 否 | all=抓全部分P / first=只抓第一页 | all |

请求体示例：

```json
{
  "video": "BV1w8RBBUEYy",
  "limit": "10",
  "timeout": "15",
  "page_mode": "all"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video": "BV1w8RBBUEYy", "limit": "10", "timeout": "15", "page_mode": "all"}' \
  "https://v1.apizero.cn/api/bili-danmaku"
```

### 响应示例 `200`

```json
{
  "code": 0,
  "msg": "成功",
  "data": {
    "video": {
      "bvid": "BV1w8RBBUEYy",
      "title": "视频标题",
      "duration": 300
    },
    "danmaku_summary": {
      "total_count": 1500,
      "top_meme": "哈哈哈哈",
      "top_repeat_comments": [
        {
          "text": "哈哈哈哈",
          "count": 120
        }
      ],
      "top_terms": [
        {
          "term": "牛逼",
          "count": 200
        }
      ]
    },
    "sentiment_summary": {
      "label": "positive",
      "average_score": 0.72
    }
  },
  "request_id": "req_abc123",
  "tips": "极数本源 · https://apizero.cn"
}
```

<a id="ai-video"></a>

## 118. AI 文生视频 `ai-video`

文生视频走大模型同一地址：POST https://v1.apizero.cn/v1/chat/completions。换视频模型只改 model。默认经济档。套餐请开通企业会员或大模型页已有视频月卡，本接口不另开套餐。

### 基础信息

| 字段 | 值 |
| --- | --- |
| Endpoint | `https://v1.apizero.cn/v1/chat/completions` |
| Method | `POST` |
| 分类 | AI 能力 (`ai`) |
| 计费 | 付费 |
| QPS | 3 req/s |
| 每日免费额度 | 登录用户  次；匿名  次 |
| 增长层级 | D-inventory |
| 推广动作 | 先收录 |
| 推广角度 | 先放入接口库，等站内调用量或搜索需求上来后再写专项内容。 |
| 官网文档 | https://apizero.cn/aidocs/ai-video |
| Marketplace | https://apizero.cn/marketplace/ai-video |

### 鉴权

推荐使用 Header：`X-API-Key: $APIZERO_API_KEY`。匿名额度适合测试，正式集成建议创建 Key；部分文档也兼容 `?key=YOUR_API_KEY` 或 `Authorization`。

### Query 参数

| 参数 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| model | string | 是 | 视频模型 ID，见本页模型表或 ?type=video | viduq3 |
| tier | string | 否 | 收费档：economy 经济（默认、最低）/ standard 适中 / plus 较贵 | economy |
| messages | array | 是 | OpenAI 风格 messages，提示词放在 user content | [{"role":"user","content":"一只金毛在草地上奔跑，慢镜头，阳光"}] |
| type | string | 否 | 固定 video 只看视频模型 | video |

### Request Body

- Content-Type：`application/json`
- Body 必填：是

| 字段 | 类型 | 必填 | 说明 | 示例 |
| --- | --- | --- | --- | --- |
| model | string | 是 | 视频模型 ID，见本页模型表或 ?type=video | viduq3 |
| tier | string | 否 | 收费档：economy 经济（默认、最低）/ standard 适中 / plus 较贵 | economy |
| messages | array | 是 | OpenAI 风格 messages，提示词放在 user content | [{"role":"user","content":"一只金毛在草地上奔跑，慢镜头，阳光"}] |
| type | string | 否 | 固定 video 只看视频模型 | video |

请求体示例：

```json
{
  "model": "viduq3",
  "tier": "economy",
  "messages": "[{\"role\":\"user\",\"content\":\"一只金毛在草地上奔跑，慢镜头，阳光\"}]",
  "type": "video"
}
```

### cURL 模板

```bash
curl -sS \
  -X POST \
  -H "Authorization: Bearer $APIZERO_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "viduq3", "tier": "economy", "messages": "[{\"role\":\"user\",\"content\":\"一只金毛在草地上奔跑，慢镜头，阳光\"}]", "type": "video"}' \
  "https://v1.apizero.cn/v1/chat/completions"
```

### 响应示例 `200`

```json
{
  "id": "chatcmpl-vid",
  "object": "chat.completion",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "https://example.com/generated.mp4"
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 20,
    "completion_tokens": 6,
    "total_tokens": 26
  },
  "tips": "极数本源 · https://apizero.cn"
}
```
