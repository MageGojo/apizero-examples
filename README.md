# ApiZero Examples

可运行的极数本源 API 示例代码，面向 CSDN、GitHub 和独立开发者转化。

官网：https://apizero.cn  
API 文档：https://apizero.cn/aidocs  
申请 Key：https://apizero.cn/account/keys

## 为什么建这个仓库

很多开发者搜索的不是“聚合 API 平台”，而是一个具体问题：

- Python 怎么查天气？
- Node.js 怎么查 DNS / 热搜 / 票房？
- 扫条码怎么自动补全商品名称、品牌和图片？
- QQ 头像和昵称能不能直接接口查询？

这个仓库只放这些具体问题的最短可运行示例。示例默认使用匿名免费额度；生产环境建议设置 `APIZERO_API_KEY`。

## 快速开始

### Python

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

python examples/weather/python_weather.py
python examples/barcode/python_barcode_lookup.py
python examples/qq-info/python_qq_info.py
```

### Node.js

需要 Node.js 18+。

```bash
node examples/weather/node_weather.mjs
node examples/barcode/node_barcode_lookup.mjs
node examples/qq-info/node_qq_info.mjs
```

### 使用 API Key

匿名额度适合测试。如果要稳定调用，建议设置环境变量：

```bash
export APIZERO_API_KEY="你的_API_Key"
```

所有示例都会自动读取 `APIZERO_API_KEY`，没有设置时走匿名额度。

## 示例目录

| 主题 | 示例 | 文档 |
| --- | --- | --- |
| 免费天气 API | `examples/weather` | https://apizero.cn/aidocs/weather |
| 墨迹天气 API | `examples/weather` | https://apizero.cn/aidocs/moji-weather |
| 商品条码查询 API | `examples/barcode` | https://apizero.cn/aidocs/barcode-lookup |
| 商品条码查询 PRO | `examples/barcode` | https://apizero.cn/aidocs/barcode-gs1 |
| QQ 头像昵称 API | `examples/qq-info` | https://apizero.cn/aidocs/qq |
| 百度热搜 API | `examples/content` | https://apizero.cn/aidocs/hot-baidu |
| 实时电影票房 API | `examples/content` | https://apizero.cn/aidocs/movie-box |
| 基金估值 API | `examples/content` | https://apizero.cn/aidocs/fund |
| 视频元数据解析排错 | `examples/video-parse` | https://apizero.cn/aidocs/video-parse |

## 平台发布包

`docs/platforms` 里放了下一批平台的发布材料：

- Apifox API Hub 发布包
- Postman Public API Network 发布包
- 掘金文章标题和摘要
- 知乎回答模板
- V2EX 求测帖
- Gitee / GitCode 镜像说明

## 接口导出

官网暂时没有后台导出功能，所以这个仓库用公开文档整理了一份可重复生成的接口清单：

- `data/apis.csv`：表格版，适合导入飞书/Excel 做筛选。
- `data/apis.json`：结构化版，适合后续做脚本、看板、自动生成 README。
- `docs/api-inventory.md`：全量 105 个接口清单。
- `docs/api-growth-priority.md`：按拉新优先级整理的主推/补充/谨慎接口。

重新生成：

```bash
python scripts/export_interfaces.py
```

## 当前主推接口

根据站内近 30 天 API 调用热度，先主推低错误率、高调用量的接口：

1. `weather`：天气查询，调用量最高，适合小程序、站点天气模块、脚本自动化。
2. `barcode-lookup` / `barcode-gs1`：条码查询，适合库存、扫码录入、电商资料补全。
3. `qq`：QQ 头像、昵称、邮箱、空间链接查询，适合头像展示和轻量用户资料补全。
4. `moji-weather`：墨迹天气，适合需要更完整天气字段的场景。

`video-parse` 当前只作为合法使用和排错示例，不作为拉新主入口。

## 常见问题

### 不设置 Key 能跑吗？

可以。多数示例支持匿名额度。生产环境建议设置 `APIZERO_API_KEY`，避免共享匿名额度耗尽。

### 返回 `4015` / `4030` 怎么办？

通常是匿名额度用完、接口要求 Key、或当天免费额度用完。去 https://apizero.cn/account/keys 创建 Key 后再运行。

### 返回 `4000` 怎么办？

参数格式错误。先确认必填参数、手机号/QQ/条码等格式是否符合文档。

### 视频解析为什么不放在主推？

视频元数据解析对输入链接、上游平台状态和合法使用场景要求更高。为了避免新用户复制失败，本仓库只放排错指南和合规示例。

## CSDN 发文规则

本仓库配套 CSDN 文章草稿在 `docs/csdn`，当前已准备 20 篇稿件和一份发布顺序说明。

- 标题必须包含搜索词，如 `免费天气API`、`商品条码查询API`、`QQ头像API`、`Python`、`Node.js`。
- 开头 3 行直接给结果，不写平台介绍。
- 代码必须可复制运行。
- 每篇只放两个链接：本仓库示例 + 对应官网文档。
