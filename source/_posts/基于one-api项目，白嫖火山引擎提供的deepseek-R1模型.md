---
abbrlink: ''
categories:
- - 网页部署
date: '2025-02-28T15:23:34.994996+08:00'
keywords: null
tags:
- OpenAI
- 网页部署
- DeepSeek
title: 基于one-api项目，白嫖火山引擎提供的deepseek-R1模型
updated: '2025-02-28T15:23:47.086+08:00'
---
> 好久不见，时隔数月，笔者重新有空折腾这些乱七八糟的玩意儿，因此撰写本文。

# 去火山引擎申请一个deepseek的api

如何注册帐号、点击页面等步骤省略，看截图自行摸索

![1740727666202.webp](https://img.dmnb.cf/2025-02-28-67c16585d9184.webp)

火山提供的api有50w免费token,够用一段时间了。

# 搭建一个one-api

one-api项目为LLM API 管理 & 分发系统，支持 OpenAI、Azure、Anthropic Claude、Google  Gemini、DeepSeek、字节豆包、ChatGLM、文心一言、讯飞星火、通义千问、360 智脑、腾讯混元等主流模型，统一 API  适配，可用于 key 管理与二次分发。单可执行文件，提供 Docker 镜像，一键部署，开箱即用。

通过标准的 OpenAI API 格式访问所有的大模型，开箱即用

具体教程请看[官方项目](https://github.com/songquanpeng/one-api)

![1740728179251.webp](https://img.dmnb.cf/2025-02-28-67c1677bcc34b.webp)

# 将火山引擎的deepseek api填入one-api

如图：

![1740728251658.webp](https://img.dmnb.cf/2025-02-28-67c167c32cfad.webp)

模型部分，填入Deepseek-R1,密钥部分填入火山的token,其他如图。

# one-api中创建key

如图：

![1740728409981.webp](https://img.dmnb.cf/2025-02-28-67c1686020264.webp)



之后将one-api的地址，作为BASE_URL，将one-api的令牌作为OPENAI_API_KEY，填入你的NextChat环境变量，即可获得一个白嫖的Deepseek自建web客户端。

![1740727376076.webp](https://img.dmnb.cf/2025-02-28-67c1645be7cbe.webp)
