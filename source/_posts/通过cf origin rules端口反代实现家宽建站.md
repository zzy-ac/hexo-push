---
abbrlink: ''
categories:
- - 网页部署
date: '2023-12-01T11:11:28.363299+08:00'
keywords: null
tags:
- 网页部署
title: 通过cf origin rules端口反代实现家宽建站
updated: 2023-12-1T11:11:36.119+8:0
---
# 起因

无意间发现cloudflare的origin rules规则，可以进行端口反向代理，将对应端口上的页面代理到正常的80、443上，直接访问。于是开始琢磨起它的使用方法。

# 应用场景

这个功能的应用场景非常广泛，据我简单思考大致有以下几点，欢迎补充：

1. 家宽，运营商拦截了80、443端口的，可以绕过限制建站。
2. 没有公网ipv4但有ipv6的家宽，可以实现1的同时将ipv6单栈解析转为ipv4、ipv6双栈的。
3. 让限制了端口数量的nat小鸡建站
4. 让纯ipv6小鸡也可以建站（同2）

# 原理解析

要实现上述功能原理非常简单，首先我有一个工具域名`tool.example.com`ddns解析到了我的家宽。

然后将需要用到的域名如`aaa.example.com`cname到工具域名`tool.example.com`并打开cf的cdn按钮。

最后创建一条origin rules规则，将`aaa.example.com`重写到置顶端口。如此即可实现不带端口直接通过域名访问搭建在家宽的站点。

不过cf的免费服务只能创建10个origin rules规则。

# 具体操作步骤

## 方法一：使用nginx、OpenResty等webserver来搭建网页

优势：

1. 可以绕开10条规则的限制，仅仅用一条规则就可以将多个家宽搭建的站点反代出来直接访问。
2. 便于管理

不足：

1. 如果不使用如宝塔、1panel之类的面板工具的话搭建比较麻烦

### 步骤

我这里直接用1panel面板建站了，各位有什么独特的需求或者可以手搓的，请自便。

#### 1、安装1panel

参考官方文档采取合适方式安装：[在线安装 - 1Panel 文档](https://1panel.cn/docs/installation/online_installation/)

安装成功后，控制台会打印面板访问信息，可通过浏览器访问 1Panel：

```
http://目标服务器 IP 地址:目标端口/安全入口
```

* **如果使用的是云服务器，请至安全组开放目标端口。**
* **ssh 登录 1Panel 服务器后，执行 1pctl user-info 命令可获取安全入口（entrance）**

安装成功后，可使用 [1pctl](https://1panel.cn/docs/installation/cli/) 命令行工具来维护 1Panel

#### 2、安装所需应用

![https://s2.loli.net/2023/12/01/iUvAB38617uWwVN.png](https://s2.loli.net/2023/12/01/iUvAB38617uWwVN.png)

如果需要自己建站的话，可以安装OpenResty、PHP、Mysql等常用工具。

此外1panel还提供大量相关应用程序如Alist、Cloudreve、WordPress等可供直接下载使用。

#### 3、安装OpenResty时记得设置好http站点的默认端口如设成1234，https的端口可以不管。

![https://s2.loli.net/2023/12/01/dN4rvnFItqfX1C8.png](https://s2.loli.net/2023/12/01/dN4rvnFItqfX1C8.png)

#### 4、在ddns脚本中将`tool.example.com`工具域名解析到你的家宽ip上。

![https://s2.loli.net/2023/12/01/dTGQVApgIJPFO5X.png](https://s2.loli.net/2023/12/01/dTGQVApgIJPFO5X.png)

#### 5、1p创建一个网站，将域名设为`aaa.example.com`

![https://s2.loli.net/2023/12/01/kRNFnKEpDtdCis9.png](https://s2.loli.net/2023/12/01/kRNFnKEpDtdCis9.png)

#### 6、在cloudflare创建一个cname记录，将`aaa.example.com`解析到`tool.example.com`上，并开启cf cdn。

![https://s2.loli.net/2023/12/01/d4wz9HBtAWmoQYC.png](https://s2.loli.net/2023/12/01/d4wz9HBtAWmoQYC.png)

#### 7、创建一个Origin rules，将域名aaa.example.com重写到1234端口

![https://s2.loli.net/2023/12/01/VO69giJMjSAdPve.png](https://s2.loli.net/2023/12/01/VO69giJMjSAdPve.png)

完成，访问你的aaa.example.com就能打开你的网站了。

### 方法二，直接一个端口搭一个网页，然后每个端口分辨创建一条Origin rules来转发端口

优势：可能省了点事？不需要使用额外的webserver啥的

不足：站点不多还好，站点多了管理麻烦，而且10条规则可能不够用。


# 以上，完毕
