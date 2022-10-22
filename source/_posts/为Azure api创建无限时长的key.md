---
title: 为Azure AD应用创建无限时长的key
date: 2022-09-23 15:15:08
tags: 网页部署 
categories: 网页部署
---

> 早在2021年4月微软就移除了AzureAD应用程序注册中永不过期的选项（Never Expire），出于对用户安全的考虑，这一变更显然是有其价值的，但也为广大开发者带来了不便。因此，本文章经过探索找到了一个可以绕过限制创建终结日期为任意年份密钥的方法。

# 登陆Azure AD平台

Azure AD 地址：[https://portal.azure.com/](https://portal.azure.com/)

## 选择应用注册选项：

![Azure-1](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/1663918066000.png)
## 创建新的应用：

![Azure-2](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/Azure-2.webp)
## 填入相关信息创建应用程序

![Azure-3](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/Azure-3.webp)
## 在概述中可以看到该程序的Client_ID

![Azure-4](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/Azure-4.webp)
## 选择证书和密码—>新客户端密码创建key

![Azure-5](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/Azure-5.webp)
## F12打开浏览器开发者模式模拟手机版页面

![Azure-6](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/Azure-6.webp)

## 填入想要的key名称并选择自定义截止期限

![Azure-7](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/Azure-7.webp)
如图所示如果直接填入超范围的时间会有红字提示，并且下面的添加按钮为灰色不可选中状态。
因此我们要先随意选择一个2年范围内的合理日期，然后点击页面空白处点亮下方的添加按钮。
之后将日期的年份修改为2099、2333或9999这样超过了两年范围的日期。

![Azure-8](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/Azure-8.webp)
![Azure-9](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/Azure-9.webp)

之后直接点击添加，就可以看到我们已经成功创建了一个截止日期为2333年的api，你也可以将2333换成任意你想要的值（四位数）

![Azure-10](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/hexo-plus-plus/Azure-10.webp)

至此你就成功的创建了一个永不过期的Azure AD的应用程序密钥。（相信我你活不到2333年的）