# 知乎回答发布包

知乎不要直接发“推荐我家平台”。要回答具体问题，把 ApiZero 作为一个可选方案。

## 可搜索问题

- 有没有免费的天气 API？
- 商品条码查询 API 有没有免费的？
- Node.js 怎么根据城市查询天气？
- 如何通过 QQ 号获取头像？
- 有哪些适合个人开发者的小 API？

## 回答模板：免费天气 API

```text
如果只是做个人项目、小程序天气卡片或脚本提醒，可以先用支持匿名额度的天气 API 测试，不一定一开始就申请高德/百度/和风天气的 Key。

我一般会先确认 3 件事：
1. 能不能直接按城市名查询。
2. 返回里有没有中文天气摘要。
3. 免费额度够不够个人项目测试。

下面是一个 Node.js 示例：

const params = new URLSearchParams({
  type: "weather",
  city: "北京",
  days: "3",
  hours: "24",
});

const res = await fetch(`https://v1.apizero.cn/api/weather?${params}`);
const data = await res.json();
console.log(data.data?.summary);

完整示例：
https://github.com/MageGojo/apizero-examples/tree/main/examples/weather

文档：
https://apizero.cn/aidocs/weather
```

## 回答模板：商品条码 API

```text
商品条码查询要看你是做“商品展示”还是“官方注册信息核验”。

如果只是扫码后补全商品名称、品牌、规格和图片，用普通条码查询就够了：

https://v1.apizero.cn/api/barcode-lookup?barcode=6921168509256

如果要看官方注册主体、厂商信息、产品登记信息，就需要 GS1 方向的数据：

https://v1.apizero.cn/api/barcode-gs1?code=6907992700199

我整理了 Python / Node.js 示例：
https://github.com/MageGojo/apizero-examples/tree/main/examples/barcode
```

## 注意

- 每个回答只放一个 GitHub 链接和一个文档链接。
- 不要连续回答太多相似问题，容易像营销号。
- 尽量先写判断标准，再给示例。

