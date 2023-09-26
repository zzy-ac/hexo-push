---
abbrlink: ''
categories:
- - linux
date: '2023-09-26T14:18:54.220415+08:00'
excerpt: ''
keywords: null
tags:
- linux
title: frp隧道开通实现内网穿透
updated: 2023-9-26T21:13:7.744+8:0
---
# 一、起因

在日常的使用中我们可能会需要向我们的朋友临时的分享自建的各种服务，因此申请公网ip的意义变得十分重要。然而在日常的使用中我们并不能时时刻刻守候在公网的环境下，无论是无法申请到亦或者申请到了但却不得不出差外地，都会导致我们一段时间内无法正常的向朋友们分享服务。因此frp作为面对这种情况而生的开源工具，很有介绍的价值

# 二、介绍

frp 是一种快速反向代理，允许您将位于 NAT 或防火墙后面的本地服务器暴露给 Internet。目前支持TCP和UDP，以及HTTP和HTTPS协议，可以将请求通过域名转发到内部服务。

frp还提供P2P连接模式。

# 为什么使用 frp ？

通过在具有公网 IP 的节点上部署 frp 服务端，可以轻松地将内网服务穿透到公网，同时提供诸多专业的功能特性，这包括：

* 客户端服务端通信支持 TCP、QUIC、KCP 以及 Websocket 等多种协议。
* 采用 TCP 连接流式复用，在单个连接间承载更多请求，节省连接建立时间，降低请求延迟。
* 代理组间的负载均衡。
* 端口复用，多个服务通过同一个服务端端口暴露。
* 支持 P2P 通信，流量不经过服务器中转，充分利用带宽资源。
* 多个原生支持的客户端插件（静态文件查看，HTTPS/HTTP 协议转换，HTTP、SOCK5 代理等），便于独立使用 frp 客户端完成某些工作。
* 高度扩展性的服务端插件系统，易于结合自身需求进行功能扩展。
* 服务端和客户端 UI 页面。

# 使用

当我们安装frp后会得到它的服务端（frps）以及客户端（frpc），部分发行版将其分开打包（如archlinux），当我们使用时需要分别在服务器和pc上配置并启动对应程序。

## 服务端

安装好frps后我们将获得frps.ini以及frps_full.ini两份配置文件，前者为简易版，仅提供最基本的配置，后者则列出了我们可能需要的各种配置及其示例。

在我们的使用中需要首先确定自己的需求并部署对应的配置，如，在此我的需求仅仅是为了跟远方的好朋友连接minecraft，所以我选择仅仅打通TCP和UDP通道用于联机即可。故而采用最基本的默认配置。

```
[common]
bind_port = 7000
```

之后使用命令启动程序

```bash
frps -c /etc/frp/frps.ini
```

## 客户端

同上编写配置文件frpc.ini并启动程序：

```bash
[common]
server_addr = <ip/address>
server_port = 7000

[Minecraft]
type = tcp
local_ip = 127.0.0.1
local_port = 25565
remote_port = 25565

[Minecraft-Voice]
type = udp
local_ip = 127.0.0.1
local_port = 24454
remote_port = 24454
```

启动程序为：

```bash
frpc -c /etc/frp/frpc.ini
```

之后允许minecraft的服务端或者正常客户端，并邀请好友测试即可知晓成果。
