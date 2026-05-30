---
abbrlink: ''
categories: []
date: '2026-05-30T14:34:46.346043+08:00'
keywords: null
tags:
- cloudflare
- mail
title: cloudflare邮箱推荐——cloud-mail
updated: '2026-05-30T14:46:02.512+08:00'
---
> 一直想搞一个serverless的自建邮局，之前没找到什么好项目，最近发现了一个基于cloudflare的邮箱worker搭建的自建邮箱工具，感觉甚是方便顾推荐一二。

# 项目简介

项目名称：

[cloud-mail](https://github.com/maillab/cloud-mail)

项目地址：

https://github.com/maillab/cloud-mail

项目介绍：

只需要一个域名，就可以创建多个不同的邮箱，类似各大邮箱平台，本项目支持署到 Cloudflare Workers ，降低服务器成本，搭建自己的邮箱服务。

# 功能介绍

* 💰 低成本使用： 可部署到 Cloudflare Workers 降低服务器成本
* 💻 响应式设计：响应式布局自动适配PC和大部分手机端浏览器
* 📧 邮件发送：集成Resend发送邮件，支持群发，内嵌图片和附件发送，发送状态查看
* 🛡️ 管理员功能：可以对用户，邮件进行管理，RABC权限控制对功能及使用资源限制
* 📦 附件收发：支持收发附件，使用R2对象存储保存和下载文件
* 🔔 邮件推送：接收邮件后可以转发到TG机器人或其他服务商邮箱
* 📡 开放API：支持使用API批量生成用户，多条件查询邮件
* 🔢 验证码识别：使用Workers AI，自动识别邮件验证码
* 📈 数据可视化：使用ECharts对系统数据详情，用户邮件增长可视化显示
* 🎨 个性化设置：可以自定义网站标题，登录背景，透明度
* 🤖 人机验证：集成Turnstile人机验证，防止人机批量注册
* 📜 更多功能：正在开发中...

# 部署教程

该项目可以自己手动在cloudflare中一步一步部署，也可以直接用github actions一键部署。

相关教程可以查看官方文档：[https://doc.skymail.ink/](https://doc.skymail.ink/)

![](https://image.m-l.cc/file/1780123580345_1000010716.jpg)

# 成果展示

![](https://image.m-l.cc/file/1780123735259_1000010717.jpg)

邮箱部署好之后可以正常在邮箱内收发邮件，连接s3储存桶后，也可以支持收发附件，功能基本齐全。

虽然不支持smtp、imap之类的第三方邮箱客户端，但是可以设置自动转发到telegram或其他邮箱（例如转发到QQ邮箱实现用微信接收邮件提醒）

总体来说方便快捷且好用。
