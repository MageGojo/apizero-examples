# 视频元数据解析排错示例

这个接口不作为拉新主入口。原因是视频解析成功率受链接有效期、平台状态、隐私权限、上游反爬和合法使用范围影响。

## 运行

```bash
export VIDEO_SHARE_URL="你的公开视频分享链接"
python examples/video-parse/python_video_parse_debug.py
```

## 排错清单

- 链接必须是公开可访问的分享链接。
- 私密、过期、删除、地区限制内容可能失败。
- 大规模抓取、下载站、二次传播等用途不适合使用。
- 返回错误时优先检查 `msg`、`request_id` 和原始链接是否仍可打开。

## 文档

https://apizero.cn/aidocs/video-parse

