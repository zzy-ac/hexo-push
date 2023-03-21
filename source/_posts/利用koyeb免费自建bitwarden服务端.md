---
title: 利用koyeb免费自建bitwarden服务端
date: 2023-03-21 11:52:34
tags: 网页部署
categories: bitwarden
---

# 起因

最近收到了github发来的“两步验证（F2A）最后通牒”，说是5月4日之前还不开启F2A的话，就会限制github网页端的访问，并自动跳转到F2A的设置页面去。这就很烦，无奈只能去把F2A打开咯。
可以用于接收TOTP的程序有很多，官方给出的建议有1password、authy等等，还有开源的Free
OTP和FreeOTP以及国产程序“神锁离线版”等等，可以自己选择合适的产品。
不过对于博主个人而言，bitwarden本身的多平台支持、以及支持自建服务的几个属性，使之成为博主的不二选择。（关键是早就在用它存密码了，习惯而已）

# 项目

本博客使用的bitwarden服务端为rust编写的开源替代客户端[vaultwarden](https://github.com/dani-garcia/vaultwarden)，[用 Rust 编写并与上游 Bitwarden 客户端](https://bitwarden.com/download/)，该项目是兼容的 Bitwarden 服务器 API 的替代实现*，非常适合运行官方资源密集型服务可能不理想的自托管部署。

![image-20230321123328198](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321123328198.png)

# 部署

首先，注册一个koyeb,（如果你有其他可以部署docker的PaaS平台，你也可以自己看着弄）

之后，登陆你的koyeb：

![image-20230321123534246](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321123534246.png)

接着，点击`create app +`来创建应用，并选择docker选项

![image-20230321123737038](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321123737038.png)

在images栏填入`vaultwarden/server`，点击`next`、`Advanced`、将端口从8000修改为80

![image-20230321124112083](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321124112083.png)

修改你的应用名称，也就是你koyeb默认生成的网站的前缀

![image-20230321124200568](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321124200568.png)

点击`deploy`，等待程序状态变为healthy，即可正常使用

![image-20230321124344526](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321124344526.png)

# 使用

打开bitwarden（手机、插件、pc客户端都行），在添加账户时点右上角设置，将你的获取的域名填入`服务器URL`选项中，保存即可。

自此你就可以使用完全自建，不用担心泄露问题的全平台密码管理器了，不管是安卓手机还是iphon亦或者谷歌内核的各个浏览器以及firefox浏览器等，均可直接自动填充密码。并且由于密码全都加密保存在你自建的koyeb容器中，也可以不用担心密码泄露问题。

# 总结

以上就是用koyeb搭建bitwarden服务端的全部流程，是不是非常无脑且快捷？有需要的话就赶紧去部署起来吧！

