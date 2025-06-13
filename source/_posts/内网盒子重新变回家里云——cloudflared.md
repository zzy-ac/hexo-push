---
abbrlink: ''
categories:
- - 网页部署
date: '2024-08-01T08:45:32.625+08:00'
keywords: null
tags:
- 网页部署
title: 内网盒子重新变回家里云——cloudflared
updated: '2024-08-01T13:37:35.072+08:00'
---
> 噩耗，因为工作原因搬家了，之前的宽带也用不了了，可能在未来挺长一段时间里没法用上家宽的公网ip了 QaQ！

> 这也就导致了原本用cloudflare origin rules反代一下就可以正常用的家里云彻底say byebye了。搞得挺被动的，于是几番琢磨下，采用cloudflared内网穿透的方式来重新恢复家里云服务。

# 服务端

服务器内还是之前的那些服务，通过1panel面板，搭建了几个alist程序、lsky-pro图床、几个静态网页等等。搭建了什么服务不重要，你只需要把它们安置在不同的端口上就好了。

例如：1panel在 `1234`，alist-1在 `12341`，alist-2在 `12342`，lsky-pro在 `12343`这样就好。当然还有ssh的服务也是需要被反代的，你可以就用默认的22,当然也不排除你用其他端口例如 `2222`

# Cloudflared

## web控制台

服务端安排好之后，进入cloudflare，打开zero trust，选择 `Networks`-`tunnels`，创建一个新的tunnel。

![https://img.dmnb.cf/2024-08-12-66b9acd37e4aa.webp](https://img.dmnb.cf/2024-08-12-66b9acd37e4aa.webp)

选 `cloudflared`

![https://img.dmnb.cf/2024-08-12-66b9ad60c0e7c.webp](https://img.dmnb.cf/2024-08-12-66b9ad60c0e7c.webp)

随便来个喜欢的名字

![https://img.dmnb.cf/2024-08-12-66b9afa750503.webp](https://img.dmnb.cf/2024-08-12-66b9afa750503.webp)

选择你所用的服务端系统版本和架构，并复制对应的cloudflared安装命令。在这里我的家里云盒子是armbian的系统，所以选到得便和arm64-bit就行。

![https://img.dmnb.cf/2024-08-12-66b9af9fb8451.webp](https://img.dmnb.cf/2024-08-12-66b9af9fb8451.webp)

## 服务端安装cloudflared

让你的电脑和家里云盒子在同一个路由器下面（确保其在同一个局域网内）

ssh通过内网ip进入你的盒子

通过刚刚复制的命令安装cloudflare的并启动cloudflared服务，保持它能每次都开机自启。

回到web端，返回 `tunnels`页面查看到status变绿为 `HEALTHY`则表示已经顺利连上了。

![https://img.dmnb.cf/2024-08-12-66b9b093c3c02.webp](https://img.dmnb.cf/2024-08-12-66b9b093c3c02.webp)

## 配置隧道代理的各个web服务的端口

在web页面的 `Public hostname`下面创建各个Public hostnames，将你的各个http服务的站点添加进来例如：

![https://img.dmnb.cf/2024-08-12-66b9aed7325b9.webp](https://img.dmnb.cf/2024-08-12-66b9aed7325b9.webp)

保存后会自动创建DNS记录，将你的域名绑定过去，这样就可以顺利的通过域名访问你的对应的服务了。

对于自建的网站，你可以用OpenResty、nginx等web服务来将它们设定到不同的端口。

这样就恢复对家里云内所有web服务的访问。

## 代理SSH！

配置域名和转发方式如下：

![https://img.dmnb.cf/2024-08-12-66b9b05b3fc82.webp](https://img.dmnb.cf/2024-08-12-66b9b05b3fc82.webp)

在需要连接ssh的设备上如，你的PC电脑、你的手机termux等等，也安装好cloudflared，并在 `.ssh/config`添加好对应的配置如下：

```
Host armbian
    HostName ssh.example.com
    ProxyCommand cloudflared access ssh --hostname %h
    User admin
    Port 2222
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_armbian
```

这样你就能通过 `ssh armbian`命令来连接到你的ssh服务器了

# 结束

至此，家里云盒子上的各个web服务和ssh都已经恢复正常使用，除了rustdesk的服务端被迫放弃掉公网访问之外，我的其它家里云服务全部恢复正常。完结，撒花～！
