---
abbrlink: ''
categories:
- - 网页部署
- - OpenAI
date: '2024-03-01T11:29:42.557224+08:00'
keywords: null
tags:
- GPT
- ChatGPT
- OpenAI
- 网页部署
title: 谷歌大模型AI—Gemini白嫖api攻略
updated: '2024-03-01T11:30:03.687+08:00'
---
> 近日一直在寻找一款稳定靠谱用着踏实的大模型ai自建方案，openai的api需要收费，用token则非常不稳定；使用azure提供的openai的api很快、稳定，但需要收费。最近突然发现谷歌新出的gemini大模型ai,其功能基本对标chatgpt,使用体验上也区别不大，但是，谷歌提供了每分钟60条的免费api套餐，很是划算！于是采取gemini的api结合广受好评的chatgpt-next-web项目提供的网页，自建专属的免费智能AI！

# 申请Gemini的api


**打开谷歌开放平台：**

[https://ai.google.dev/pricing](https://ai.google.dev/pricing)

![谷歌开放平台](https://img.m-l.cc/2024-08-12-66b9b0634679b.webp)

往下拉可以看到2个版本的API。

选择左边的免费版。

![选择左边的免费版](https://img.m-l.cc/2024-08-12-66b9aef115743.webp)

登录@[gmail.com](https://gmail.com)邮箱。(需要自行寻找合适的节点进行科学上网)

之后同意下图所示的第一个协议（二三个复选框是允许推广，可选可不选）

![同意协议](https://img.m-l.cc/2024-08-12-66b9adc21d198.webp)


在这个界面选择第二项。

获取API秘钥

![获取API秘钥](https://img.m-l.cc/2024-08-12-66b9ad3513373.webp)

![](https://img.m-l.cc/2024-08-12-66b9ad9844476.webp)

这里会生成一个API的秘钥，

复制记录一下。保存好。

没有保存，就需要重新生成了。

![](https://img.m-l.cc/2024-08-12-66b9aef61bf3f.webp)

OK 这样我们的免费API就申请好了。

（注：本节为了省事和避免重复造轮子，引用了[李飞笔记](https://zhuanlan.zhihu.com/p/673300213)的部分内容和图片）

# 创建chatgpt-next-web

具体教程参考作者[README.md](https://github.com/ChatGPTNextWeb/ChatGPT-Next-Web/blob/main/README_CN.md)

在此我采用的作者提供的Vercel方案。

## 改环境变量

在按照教程搭建好chatgpt-next-web后，进入项目设置的环境变量部分：

![https://img.m-l.cc/2024-08-12-66b9ad0f3c075.webp](https://img.m-l.cc/2024-08-12-66b9ad0f3c075.webp)

删除多余的环境变量（如，没有openai的token你就删掉它。）

保留如下三项：

```
CUSTOM_MODELS=-all,+gemini-pro # 只保留gemini-pro一个ai选项，避免默认选项导致需要手动选择。
CODE=<passwd> # 这里填入你想设置的任何密码就好
GOOGLE_API_KEY=<apikey>  # 这里填入你刚刚申请到的gemini的api-key
```

然后点击项目的`deployments`按钮，创建新的部署

![https://img.m-l.cc/2024-08-12-66b9af5d369bc.webp](https://img.m-l.cc/2024-08-12-66b9af5d369bc.webp)

等待部署完毕后，你的私人大模型ai就创建成功了，开始享用你的ai吧！

![https://img.m-l.cc/2024-08-12-66b9acc919b84.webp](https://img.m-l.cc/2024-08-12-66b9acc919b84.webp)

# 完毕

打开你的vercel.app链接开始享用你的ai

如果vercel.app被墙了，请自行解析一个自定义域名用于访问你的ai网站。

![https://img.m-l.cc/2024-08-12-66b9ae2ad8e35.webp](https://img.m-l.cc/2024-08-12-66b9ae2ad8e35.webp)
