---
abbrlink: ''
categories:
- - 图床建设
date: '2024-02-02T19:50:35.455203+08:00'
keywords: null
tags:
- 网页部署
title: 白嫖cf的r2储存桶与Lsky-Pro图床
updated: '2024-02-02T19:50:35.623+08:00'
---
> 之前尝试过不少图床方案：smms、github+反代、知乎图床等等，但每种方案均有其自身的问题，如smms数据不在自己手中、github+反代速度玄学、知乎做图床相对麻烦且随时可能跑路。故而最近决定认真部署一个属于自己的、速度稳定些的图床。
>
> 经过几番查询后决定采用cf r2储存桶+lsky图床程序的形式来部署。主要原因有：
>
> 1. r2储存桶拥有全球加速，且可以选择东亚节点，在大陆与非大陆地区均可以获得不错的访问速度。
> 2. lsky-pro图床支持多种储存策略（甚至包括alist的webdav都可以）哪怕有天r2用不了，也能及时更换到其它方案。
> 3. 这俩都可以免费白嫖。

# 注册R2储存桶

CloudFlare R2 是 Cloudflare 公司推出的一款兼容 S3 API  的免费云存储服务，它允许用户在全球范围内的分布式网络上存储和检索数据。 这项服务的设计目标之一是提供低延迟、高吞吐量的存储体验，利用横跨 100  多国家中 275 个城市的内容交付网络来实现这一目标。

## 准备工作

1. CloudFlare 账号注册：[www.cloudflare.com/](https://link.juejin.cn?target=https%3A%2F%2Fwww.cloudflare.com%2F "https://www.cloudflare.com/")
2. 购买域名：选择一个合适的域名，并在 CloudFlare 上进行域名解析。
3. 绑定信用卡（只用于验证)

## 创建储存桶

在侧边菜单找到 `R2 服务`,然后点击`创建存储桶`，名称随意喜欢就好，地区选亚太地区即可

![https://pic.m-l.cc/Qexo/2024/02/02/5aa03430cbcde5be276d2a14657c7f30.png](https://pic.m-l.cc/Qexo/2024/02/02/5aa03430cbcde5be276d2a14657c7f30.png)

![https://pic.m-l.cc/Qexo/2024/02/02/12683dc876afc117ca7c32210fc303d5.png](https://pic.m-l.cc/Qexo/2024/02/02/12683dc876afc117ca7c32210fc303d5.png)

## 绑定域名



刚创建好的桶虽然可以上传图片、文件之类的，但是默认不可通过公网访问。

虽然可以用cloudflare提供的二级域名访问，但是有一些频率速率方面的限制，而且.dev的域名也可能被大防火墙拦截，所以还是绑定自己域名更好一些。

再桶的设置里找到自定义域选项，添加自定义域名即可

打开你创建的储存桶，点击设置然后：

![https://pic.m-l.cc/Qexo/2024/02/02/e3de520060ea559c124c45665c9e5495.png](https://pic.m-l.cc/Qexo/2024/02/02/e3de520060ea559c124c45665c9e5495.png)

选择自定义域，并连接到你自己的域名，即可自定义图片的直链了。（其实不绑定域名的话也会提供一个R2.dev子域名给你，也能够正常使用，只不过这里的域名有些过于长了，不好记。）


## 创建 R2 的 API token


提示：**api 令牌只会显示 1 次。需记录到本地备用。**

* 在 R2 的控制台右侧 点击 `管理 R2 API 令牌` —>`创建API令牌`**。**
* 权限选对象读和写都可
* 指定存储桶选择你刚创建的桶
* TTL选永久。其他不变。

![https://pic.m-l.cc/Qexo/2024/02/02/2a3409ed33a8d90a10fcfd11c83d79aa.png](https://pic.m-l.cc/Qexo/2024/02/02/2a3409ed33a8d90a10fcfd11c83d79aa.png)

# 部署Lsky-pro图床



参考官方教程：[https://docs.lsky.pro/docs/free/v2](https://docs.lsky.pro/docs/free/v2/)

或使用docker部署的话参考docker教程：[https://github.com/HalcyonAzure/lsky-pro-docker/blob/master/README.md](https://github.com/HalcyonAzure/lsky-pro-docker/blob/master/README.md)


## Lsky-pro与R2对象存储对接

直接看图吧：

![教程图片](https://r2.pnglog.com/2022/11/09/636b1b55c3986.png)


\* 访问域名：如上图，此域名可以自己解析**公开访问**里的域名，也可以在**域访问**哪里添加绑定。

\* URL 额外参数：可不写

\* AccessKeyId：R2 访问密钥ID

\* SecretAccessKey：R2 机密访问密钥

\* 连接地址区域(region)：`auto`(自动最佳地区，**推荐**)，或者`us-east-1`(美区)

\* 储存桶名称：之前创建储存桶时设置的储存桶名称

## 我的备选储存方案

出于多重方案多重保险的目的，我还添加了备用的储存方案，即使用alist提供的webdav来存储图片，alist是一款支持部署多重网盘解析直链的强大工具，利用alist的webdav服务，我们可以将图床存储到任何可能的网盘中，如：阿里云盘、onedrive、谷歌云盘、百度网盘甚至是可以提供无限图片存储空间的一刻相册。

在这里为了给有兴趣使用我的图床的其它用户提供服务并防止小小10G的免费R2被刷爆，我这里选择使用无限空间的一刻相册来部署。

[alist部署教程](https://alist.nn.ci/zh/guide/)

[alist挂载一刻相册教程](https://alist.nn.ci/zh/guide/drivers/baidu.photo.html)

![https://pic.m-l.cc/Qexo/2024/02/02/16dee514acf9d1f5559e6521285eb762.png](https://pic.m-l.cc/Qexo/2024/02/02/16dee514acf9d1f5559e6521285eb762.png)

如此这般我的备选lsky存储方案也部署好了。

之后只用简单配置一下用户组和默认的储存桶，就可以毫无顾忌的开放注册为网友提供服务了。

# 最后

如果使用alist+网盘的储存方案时用到如`一刻相册`这样的国内网盘，那么为了放置被恶意上传色图、血腥图片等18禁内容，还应该打开lsky-pro的图片审核功能，识别到色图直接删除，避免风险。

如果希望体验一下我的图床的话，欢迎注册使用!：[lsky.m-l.cc](https://lsky.m-l.cc)

![https://pic.m-l.cc/Qexo/2024/02/02/3f8b547fdc41f2e174360e65813b0942.png](https://pic.m-l.cc/Qexo/2024/02/02/3f8b547fdc41f2e174360e65813b0942.png)
