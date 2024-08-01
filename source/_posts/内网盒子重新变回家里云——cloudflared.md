---
abbrlink: ''
categories: []
date: '2024-08-01T07:56:52.050346+08:00'
keywords: null
tags: []
title: 内网盒子重新变回家里云——cloudflared
updated: '2024-08-01T07:56:52.474+08:00'
---
> 噩耗，因为工作原因搬家了，之前的宽带也用不了了，可能在未来挺长一段时间里没法用上加宽的公网ip了 QaQ！

> 这也就导致了原本用cloudflare origin rules反代一下就可以正常用的家里云彻底say byebye了。搞得挺被动的，于是几番琢磨下，采用cloudflared内网穿透的方式来重新恢复家里云服务。

# 服务端

服务器内还是之前的那些服务，通过1panel面板，搭建了几个alist程序、lsky-pro图床、几个静态网页等等。搭建了什么服务不重要，你只需要把它们安置在不同的端口上就好了。

例如：1panel在`1234`，alist-1在`12341`，alist-2在`12342`，lsky-pro在`12343`这样就好。当然还有ssh的服务也是需要被反代的，你可以就用默认的22,当然也不排除你用其他端口例如`2222`

# Cloudflared

## web控制台

服务端安排好之后，进入cloudflare，打开zero trust，选择`Networks`-`tunnels`，创建一个新的tunnel。

![https://pic.m-l.cc/Qexo/2024/08/01/84b33ec02b87c7763ffe5cb02ce52d9d.png](https://pic.m-l.cc/Qexo/2024/08/01/84b33ec02b87c7763ffe5cb02ce52d9d.png)

选`cloudflared`

![https://pic.m-l.cc/Qexo/2024/08/01/b9e3b6084fda5900ffde3500ab17e854.png](https://pic.m-l.cc/Qexo/2024/08/01/b9e3b6084fda5900ffde3500ab17e854.png)

随便来个喜欢的名字

![https://pic.m-l.cc/Qexo/2024/08/01/2bc527688b89c3bb9fdb9a98fd298342.png](https://pic.m-l.cc/Qexo/2024/08/01/2bc527688b89c3bb9fdb9a98fd298342.png)

选择你所用的服务端系统版本和架构，并复制对应的cloudflared安装命令。在这里我的家里云盒子是armbian的系统，所以选到得便和arm64-bit就行。

![https://pic.m-l.cc/Qexo/2024/08/01/fdb6ee5356704410c0ccfa8967f1079d.png](https://pic.m-l.cc/Qexo/2024/08/01/fdb6ee5356704410c0ccfa8967f1079d.png)

## 服务端安装cloudflared
