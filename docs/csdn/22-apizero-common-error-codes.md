# API 调用常见错误码排查：4015、4029、4030、4000 分别是什么意思？

接 API 时，跑不通不一定是代码错了，也可能是额度、Key 或参数问题。
下面整理几个常见错误码，适合先排查。
示例基于天气 API，但大多数接口排查思路类似。

## 4015：需要 API Key 或匿名额度不足

常见原因：

- 当前接口不支持匿名调用。
- 匿名额度已经用完。
- Key 没传或传错。

处理方式：申请 Key 后设置环境变量。

```bash
export APIZERO_API_KEY="你的_API_Key"
```

## 4029：QPS 超限

常见原因：

- 循环里请求太快。
- 并发过高。
- 前端重复触发请求。

处理方式：降低频率，批量任务里加 `sleep`。

## 4030：今日额度用完

常见原因：

- 当天免费额度用完。
- 多个脚本共用同一个 Key。

处理方式：等次日额度恢复，或调整调用频率。

## 4000：参数错误

常见原因：

- 必填参数为空。
- 城市、条码、QQ 号、域名等格式不符合要求。
- POST 接口没有传正确的 JSON 或表单。

## 天气 API 最小检查代码

```python
import requests

resp = requests.get(
    "https://v1.apizero.cn/api/weather",
    params={"city": "北京", "type": "weather"},
    timeout=15,
)

print(resp.status_code)
print(resp.text[:500])
```

GitHub 示例：https://github.com/MageGojo/apizero-examples  
接口文档：https://apizero.cn/aidocs/weather

