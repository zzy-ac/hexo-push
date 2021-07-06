---
title: fcitx5使用搜狗ssf主题
date: 2021-05-30 16:12:38
uuid: 90415473-1395-f199-c263-3f4a69075237
tags: linux
keywords: fcitx5
categories: fcitx5-themes
---

>Fcitx (Flexible Input Method Framework) ──即小企鹅输入法，它是一个以 GPL 方式发布的输入法平台,可以通过安装引擎支持多种输入法，支持简入繁出，是在 Linux 操作系统中常用的中文输入法。它的优点是，短小精悍、跟程序的兼容性比较好。并且fcitx支持多种多样的主题，可以非常美观。
>
>然而随着时间的更替，fcitx5的出现，很显然，fcitx已经跟不上时代了。但最初fcitx5的皮肤似乎非常简陋，只能在极其有限的范围内改一改颜色。
然而笔者今日在交流群里聊天时，突然注意到，原来fcitx5也是可以更换主题的，那么下面开始正题：

* 首先，准备fcitx5一整套，这里不详细介绍过程。

* 然后准备工具ssfconv
archlinux使用<code>pacman -S ssfconv</code>安装，其余发行版自行查阅<a href="https://github.com/fkxxyz/ssfconv">ssfconv的项目地址</a>查看

* 然后使用下列命令来生成需要的fcitx5主题文件。
```bash
ssfconv 目标主题.ssf 目标文件夹 --type fcitx5
```


* 之后将包含fcitx5主题文件的目标文件夹放到<code>~/.local/share/fcitx5/themes</code>目录下。进入fcitx5配置切换主题即可

### 效果展示
<img src="/pictures/fcitx5_en.png" style="width: 380px;height: 240px;">
<img src="/pictures/fcitx5_py.png" style="width: 380px;height: 240px;">
<img src="/pictures/fcitx5_dan.png" style="width: 380px;height: 240px;">
<img src="/pictures/fcitx5_shuang.png" style="width: 380px;height: 240px;">
