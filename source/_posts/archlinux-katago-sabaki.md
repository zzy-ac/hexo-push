---
title: 在archlinux中使用sabaki运行围棋ai引擎katago
date: 2022-08-11 16:27:34
tags: katago
keywords:
categories: archlinux
---

> 作为一个常年使用archlinux桌面操作系统的业余围棋爱好者，在经历了围棋ai给围棋界带来的巨大变革之后，能使用强劲的开源围棋ai实时分析、指导下棋，辅助磨炼棋力，实在让人难以拒绝。
>
> 同时，作为一个图形界面使用者，为ai引擎们寻找一个功能全面而使用方便的gui程序，属实重要。

近年来各类强大的开源围棋ai兴起，基于个人喜好，本文选用katago进行介绍。

# 简介

## Katago

截至 2021 年 1 月，KataGo 是最强大的在线开源围棋机器人之一。KataGo 使用类似于 AlphaZero 的过程进行训练，并进行了许多增强和改进，并且能够在没有外部数据的情况下完全从零开始快速达到顶级水平，仅通过自我游戏即可实现提高。

## Sabaki

一个优雅的围棋棋盘和 SGF 编辑器，适合更文明的时代。

sabaki是一款功能全面而简单易用且支持包括gnugo、katago以及leela等引擎的开源图形化围棋工具。



# 安装教程



## sabaki

aur源中已经有人将sabaki打包，因此开源直接使用yay/paru等aur-help程序进行安装例如：

```sh
yay -S sabaki
# 或者
paru -S sabaki
```

此外，博主还将本程序打包进了自己的私人仓库，因此如果不想自己编译，也可以直接添加博主的私人仓库，之后直接从仓库中下载编译好的包进行安装：

```sh
# 添加[zzy-ac]仓库
[zzy-ac]
SigLevel=Never
Server = https://github.com/zzy-ac/repo/releases/download/x86_64/
Server = https://gh.m-l.cc/https://github.com/zzy-ac/repo/releases/download/x86_64/

# 更新源

sudo pacman -Syu

# 安装sabaki
sudo pacman -S sabaki

```

## 安装Katago

由于katago的编译过程过于繁琐（博主电脑不大行编译起来太慢了）所以博主这里选择直接从[releases](https://github.com/lightvector/KataGo/releases/)页面下载最新版本[katago-v1.11.0-cuda11.1-linux-x64.zip](https://github.com/lightvector/KataGo/releases/download/v1.11.0/katago-v1.11.0-cuda11.1-linux-x64.zip)的二进制包，直接使用。

由于使用的cuda版，因此需要安装依赖：

```sh
sudo pacman -S cudnn
```

之后需要下载Katago训练形成的权重文件：https://katagotraining.org/networks/，如下图：

![image-20220811165920792](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/08/11/image-20220811165920792.png)

之后，解压缩katago的压缩包，将文件名为kata1-b60c320-s6372316160-d2964581281.bin.gz(kata1-后面的字符可能随版本不同有所不同，请自行辨别)放入文件夹下。

![image-20220811171236578](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/08/11/image-20220811171236578.png)在终端打开该文件夹，执行如下指令：

```sh
./katago genconfig -model kata1-b60c320-s6372316160-d2964581281.bin.gz -output sabaki.cfg
```

之后会问你如下一些问题，你可以照着我的来，也可以根据自己的情况选择性的自定义配置或使用默认配置

![image-20220811171149406](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/08/11/image-20220811171149406.png)

此后，katago将会根据训练形成的权重文件生成文件名为sabaki.cfg的配置文件。

将该文件夹重命名为katago并移动至/opt目录下



## 在Sabaki中启用Katago

1. 打开sabaki
2. 点击下图图标，并选择管理引擎：

![image-20220811171622719](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/08/11/image-20220811171622719.png)

3. 新增配置如下图
![image-20220811171713071](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/08/11/image-20220811171713071.png)

## 完成

之后你就可以自由的在Sabaki中使用Katago引擎进行围棋训练了。

![image-20220811172125906](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/08/11/image-20220811172125906.png)
