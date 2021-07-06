---
title: ark-zip包中文乱码解决
date: 2021-06-24 23:39:47
uuid: a97a698d-dd7d-87bd-0085-bc382c089638
tags: linux
categories: archlinux
---
>方舟（存档工具）是 KDE 开发的工具。该程序是一个压缩工具，使用户能够从多个文件创建存档。

　　在archlinux日常使用中ark是一个常用的图形化压缩/解压缩工具，经常用于各种压缩包的处理。
　　然而在面对由windows打包的很多zip格式压缩包时，会由于编码错误的原因，导致文件及文件夹的名称出现乱码。
　　解决的方法很简单，首先在安装位于aur仓库的<code>p7zip-natspec</code>软件包
　　之后打开ark→设置→配置ark→插件菜单，并将菜单中的Info-zip和Libzip两个插件反选，之后选中P7zip插件，然后关闭所有ark窗口，即可正确的显示zip文件的文件名了。
