---
title: win-to-go安装记录
date: 2023-01-29 10:56:07
tags: win-to-go
categories: 系统安装
---

# win to go安装记录

## 起因

近日因更换电脑的缘故，从旧笔记本上拆下来一块旧的sata口固态，正好前段时间还买了个sata转usb3.0的硬盘盒。于是就决定把windows从我的电脑上彻底删除，在移动硬盘上整个win to go，有需要时临时用用就好。

## 方案选择

做win to go的方法有很多，最基本的是直接把系统装进这块硬盘。但是私以为这样装的系统还是没有跟硬盘隔离开来，平时用这块硬盘还是会有些不爽。所以我选择采用ventoy方案。

## 步骤

### 1、Ventoy的安装于配置

* 根据你的系统，从ventoy官网下载最新的ventoy安装程序[https://ventoy.net/cn/download.html](https://ventoy.net/cn/download.html)

* 运行Ventoy2Disk安装ventoy.

* 根据需要配置一下ventoy插件（可选）

* 把ventoy分区格式化为ntfs

### 2、安装win10

* 用虚拟机程序（qemu、vm、vbox...都可以）把win10的镜像安装到vhd格式的虚拟硬盘中

* 安装Windows VHD 文件启动插件
> Ventoy 使用此插件来支持直接启动 VHD(x) 文件 （Win7以上）。
支持 Legacy BIOS 和 UEFI 模式。支持固定大小以及动态扩展类型的 VHD/VHDX 格式。
使用说明
从下面任意一个链接中下载 ventoy_vhdboot.img 文件即可（几个链接中的文件都是一样的）。
https://github.com/ventoy/vhdiso/releases
https://ventoy.lanzoub.com/b01dlxuaj (蓝奏云，密码: 7my4)
把下载后的文件放在U盘第1个分区（就是放ISO文件的分区）的 ventoy 目录下（默认没有这个目录，需手动创建，注意大小写），即 /ventoy/ventoy_vhdboot.img 就可以了。
注意是放在容量大的、存放ISO文件的那个分区中，不要放到那个 32MB 的 VTOYEFI 分区里面。

* 把装有windows的vhd文件拷贝到ventoy分区内你用于存放ISO的文件夹（没配置的话直接扔根目录也行）

### 3、测试与验收
经过上面步骤之后你已经可以重启后从ventoy进入你的win to go系统了，可以试试各方面是否正常运行。

至此就收获了一个装有win to go,同时还可以加载各种系统镜像以及linux to go的移动硬盘。

通过VentoyPlugson程序，我们可以很方便的设置ventoy插件，从而设置ventoy仅识别某个目录内的镜像。如此可以避免在硬盘内其他目录中有些可以被ventoy自动识别到的又不是系统镜像的文件被ventoy误识。
