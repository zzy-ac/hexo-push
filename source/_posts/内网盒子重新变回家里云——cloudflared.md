---
abbrlink: ''
categories:
- - 网页部署
date: '2024-08-01T07:56:52.050346+08:00'
keywords: null
tags:
- 网页部署
title: 内网盒子重新变回家里云——cloudflared
updated: '2024-08-01T08:16:50.785+08:00'
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

让你的电脑和家里云盒子在同一个路由器下面（确保其在同一个局域网内）

ssh通过内网ip进入你的盒子

通过刚刚复制的命令安装cloudflare的并启动cloudflared服务，保持它能每次都开机自启。

回到web端，返回`tunnels`页面查看到status变绿为`HEALTHY`则表示已经顺利连上了。

![https://pic.m-l.cc/Qexo/2024/08/01/36ee0c442e6ac4be19ee578a9c2e5feb.png](https://pic.m-l.cc/Qexo/2024/08/01/36ee0c442e6ac4be19ee578a9c2e5feb.png)

## 配置隧道代理的各个web服务的端口

在web页面的`Public hostname`下面创建各个Public hostnames，将你的各个http服务的站点添加进来例如：

![https://pic.m-l.cc/Qexo/2024/08/01/053b44bbf43a2127809925a9ffd5845f.png](https://pic.m-l.cc/Qexo/2024/08/01/053b44bbf43a2127809925a9ffd5845f.png)

保存后会自动创建DNS记录，将你的域名绑定过去，这样就可以顺利的通过域名访问你的对应的服务了。

对于自建的网站，你可以用OpenResty、nginx等web服务来将它们设定到不同的端口。

这样就恢复对家里云内所有web服务的访问。

## 代理SSH！

配置域名和转发方式如下：

![https://pic.m-l.cc/Qexo/2024/08/01/05e773da58bcae0b77151e798354b778.png](https://pic.m-l.cc/Qexo/2024/08/01/05e773da58bcae0b77151e798354b778.png)

在需要连接ssh的设备上如，你的PC电脑、你的手机termux等等，也安装好cloudflared，并在`.ssh/config`添加好对应的配置如下：

```
Host armbian
    HostName ssh.example.com
    ProxyCommand cloudflared access ssh --hostname %h
    User admin
    Port 2222
PreferredAuthentications publickey
IdentityFile ~/.ssh/id_rsa_armbian
```

这样你就能通过`ssh armbian命令来连接到你的ssh服务器了`

# 结束

至此，家里云盒子上的各个web服务和ssh都已经恢复正常使用，除了rustdesk的服务端被迫放弃掉公网访问之外，我的其它家里云服务全部恢复正常。完结，撒花～！
