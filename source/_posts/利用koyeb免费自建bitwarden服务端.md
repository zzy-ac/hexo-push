---
abbrlink: ''
categories:
- bitwarden
date: '2023-03-21 11:52:34'
tags:
- 网页部署
title: 利用koyeb免费自建bitwarden服务端
updated: 2023-11-19T10:44:47.294+8:0
---
# 起因

最近收到了github发来的“两步验证(F2A)最后通牒”,说是5月4日之前还不开启F2A的话,就会限制github网页端的访问,并自动跳转到F2A的设置页面去。这就很烦,无奈只能去把F2A打开咯。
可以用于接收TOTP的程序有很多,官方给出的建议有1password、authy等等,还有开源的Free
OTP和FreeOTP以及国产程序“神锁离线版”等等,可以自己选择合适的产品。
不过对于博主个人而言,bitwarden本身的多平台支持、以及支持自建服务的几个属性,使之成为博主的不二选择。(关键是早就在用它存密码了,习惯而已)

# 项目

本博客使用的bitwarden服务端为rust编写的开源替代客户端[vaultwarden](https://github.com/dani-garcia/vaultwarden),[用 Rust 编写并与上游 Bitwarden 客户端](https://bitwarden.com/download/),该项目是兼容的 Bitwarden 服务器 API 的替代实现*,非常适合运行官方资源密集型服务可能不理想的自托管部署。

![image-20230321123328198](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321123328198.png)

# 部署

首先,注册一个koyeb,(如果你有其他可以部署docker的PaaS平台,你也可以自己看着弄)

之后,登陆你的koyeb:

![image-20230321123534246](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321123534246.png)

接着,点击 `create app +`来创建应用,并选择docker选项

![image-20230321123737038](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321123737038.png)

在images栏填入 `vaultwarden/server`,点击 `next`、`Advanced`、将端口从8000修改为80

![image-20230321124112083](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321124112083.png)

---

# 此处为2023年4月7日更新内容

此前的教程内容部署出来的容器可以用,单koyeb每个月会自动重新部署容器,从而导致使用内置数据库的服务端丢失所有用户数据。故而今天琢磨了以下把永久保存数据库的方法给总结出来了,并在此写下

## 申请一个在线mysql数据库

网上有很多白嫖在线mysql数据库的平台,大部分还是比较稳妥可靠的,如果你实在还是不放心,那就干脆买服务器自建好了。博主这里选择使用[db4free.net](https://db4free.net)提供的免费数据库。

打开db4free,点击左侧菜单栏中的数据库一栏:

![https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/4/7/image_3baed74f62a0cde5b46d4f1547b1cccc.png](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/4/7/image_3baed74f62a0cde5b46d4f1547b1cccc.png)

之后在新页面点击 `马上建立你的免费MySQL账号 »`按钮

![https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/4/7/image_511f1f647fa585bf245aca3f1389e65e.png](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/4/7/image_511f1f647fa585bf245aca3f1389e65e.png)

依次填入数据库名称、数据库用户名、数据库密码以及你的邮箱(此处可用临时邮箱)这样你就申请到了一个免费的mysql数据库。在接下来的文字中我将用[dbname]、[username]、[password]来分别代表你输入的数据库名、用户名和密码。

![https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/4/7/image_3e2d17bf5f6c81c90564b470c9179c51.png](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/4/7/image_3e2d17bf5f6c81c90564b470c9179c51.png)

---

2023.11.19更新

经过反馈和确认，现在新建的数据库直接被koyeb中的vaultwarden调用会导致表创建失败暂时没去研究原因，偷个懒直接把创建好的空白数据库放上来。

使用步骤打开db4free自带的phpMyAdmin
![https://s2.loli.net/2023/11/19/RamsK8PjCIVFrDy.png](https://s2.loli.net/2023/11/19/RamsK8PjCIVFrDy.png)

输入数据库的帐号密码

![https://s2.loli.net/2023/11/19/QMZGHS5sNjr4bRq.png](https://s2.loli.net/2023/11/19/QMZGHS5sNjr4bRq.png)

点击你的数据库名称

![https://s2.loli.net/2023/11/19/WoxQzBlm5p7jPJt.png](https://s2.loli.net/2023/11/19/WoxQzBlm5p7jPJt.png)

点击导入

![https://s2.loli.net/2023/11/19/Zh52a6P9dLsmtCK.png](https://s2.loli.net/2023/11/19/Zh52a6P9dLsmtCK.png)

选择已创建好的[空白数据库](https://gh.m-l.cc/https://raw.githubusercontent.com/zzy-ac/My-Selves-Cloud/main/vaultwarden.sql)并导入：

![https://s2.loli.net/2023/11/19/7ZQxUjAd4f58JnS.png](https://s2.loli.net/2023/11/19/7ZQxUjAd4f58JnS.png)

---

至此你已经配置好了你的在线数据库,由于[vaultwarden](https://github.com/dani-garcia/vaultwarden)项目的设置,你需要将数据库的用户名、密码、数据库名重新排列成mysql数据库的链接形式来方便docker容器将其使用,即:

```html
mysql://[username]:[password]@db4free.net:3306/[dbname]
```

## 添加环境变量

接下来你只需要回到koyeb容器的创建页面,如果已经创建了的话,你只需要进入该项目的设置页面,找到 `Environment variables`在其下创建如图的两个环境变量,其中 `DATABASE_URL`的值为上面排列好的 `mysql://[username]:[password]@db4free.net:3306/[dbname]`而 `RUST_BACKTRACE`的值则为1。
![https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/4/7/image_c762ffb85dfaaa764e380b362b017d84.png](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/4/7/image_c762ffb85dfaaa764e380b362b017d84.png)

之后的步骤没有区别,照做就行。

---

修改你的应用名称,也就是你koyeb默认生成的网站的前缀

![image-20230321124200568](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321124200568.png)

点击 `deploy`,等待程序状态变为healthy,即可正常使用

![image-20230321124344526](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/03/21/image-20230321124344526.png)

# 使用

打开bitwarden(手机、插件、pc客户端都行),在添加账户时点右上角设置,将你的获取的域名填入 `服务器URL`选项中,保存即可。

自此你就可以使用完全自建,不用担心泄露问题的全平台密码管理器了,不管是安卓手机还是iphon亦或者谷歌内核的各个浏览器以及firefox浏览器等,均可直接自动填充密码。并且由于密码全都加密保存在你自建的koyeb容器中,也可以不用担心密码泄露问题。

# 总结

以上就是用koyeb搭建bitwarden服务端的全部流程,是不是非常无脑且快捷?有需要的话就赶紧去部署起来吧!
