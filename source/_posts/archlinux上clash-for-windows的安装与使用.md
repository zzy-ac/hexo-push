---
title: archlinux上clash-for-windows的安装与使用
date: 2022-09-24 18:11:04
tags: clash 
keywords:
categories: archlinux哟
---

>由于近日对魔法上网工具有了新的需求，需要对部分程序单独设置绕过代理，导致原本的v2raya有了很大的不足。在了解到clash能够满足该需求后，与群友展开了探讨，并成功换上clash。

## 安装

这里选择使用aur库中的`clash-premium-bin`  和 `clash-for-windows-electron-bin`两个相对开源且功能齐全一些的包。

```bash
yay -Sa clash-premium-bin clash-for-windows-electron-bin
```

## 配置

配置的话主要就装好包、打开服务之后自己随便调调，把订阅添加好，并打开TUN模式就好。按我的喜好我选择打开了开机自启和并且不要弹出clash主页面。

![image-20220924001912096](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/09/24/image-20220924001912096.png)



![image-20220924002020166](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/09/24/image-20220924002020166.png)

![image-20220924002118836](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/09/24/image-20220924002118836.png)

## 完成

至此你的clash for windows在archlinux上就基本配置好了，如果喜欢你还可以添加自己想要的其他配置，以满足你的个性化需求。
