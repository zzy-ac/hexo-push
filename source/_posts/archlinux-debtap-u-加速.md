---
title: archlinux debtap -u 加速
date: 2021-03-30 23:35:58
uuid: 13e4f02a-6938-b5dd-033e-97c856f72b88
tags: linux
keywords: debtap
categories: archlinux
---
在使用arch一段时间后，大家会发现一个叫做“debtap”的神器，他可以帮助不会打包的小白，轻松的完成对deb格式linux软件包的重新打包。

然而在日常的使用中，大家会发现一个严峻的问题，那就是<code>debtap -u</code>实在是太慢了！！！
这能忍吗？！
这不能忍！

在经过了第一波草率的观察后笔者发现，debtap的bin文件竟然是一个shell脚本？？？

又经过一番草率的观察后笔者发现，原来debtap的更新之所以那么慢，是因为它还需要同步debian和ubuntu的软件源来解决部分依赖问题。然而设计者，在设计之初，并未考虑到中国网络环境的影响，使用的debian、ubuntu的官方源。

因此，我们只需要将<code>/bin/debtap</code>文件中的包含有
```
http://ftp.debian.org/
```
字样的部分替换为任意国内镜像站的域名例如中科大源的
```
https://mirrors.ustc.edu.cn/
```
即可

同理将后文中的ubuntu源的替换为国内镜像源即可
搜索debtap文件中的
```
http://archive.ubuntu.com/
```
替换为
```
https://mirrors.ustc.edu.cn/
```
至此，你已经完成了对debtap本地换源的任务，接下来使用
```bash
debtap -u
```
来尽情的享受丝滑的更新体验吧！～
