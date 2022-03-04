---
title: kobo切换系统字体插件
date: 2022-01-09 18:16:05
tags: kobo
keywords:
categories: kobo
---
# 前言
近日介于某群友的需求和建议，决定写一个可以在kobo中一键切换系统字体的插件。于是就抽两分钟写了一个。

# 所需材料

1. 集成了第三方系统字体的KoboRoot.tgz文件和包含了原版字体的KoboRoot.tgz文件
2. 已经安装好了NikelMenu（必须！！！）



# 写入插件

## 1、添加字体固件和脚本

首先将[freefont.zip](https://d-m.club/J6eBPR)解压到`.add`文件夹下

默认的固件包包括一个原生字体和一个由群友[喻米](https://wpa.qq.com/msgrd?v=3&uin=1581755776&site=qq&menu=yes)提供的书刻字体

## 2、添加NikelMenu选项

然后在NikelMenu配置文件中加入下列内容

```bash
  menu_item :main   :Rescan_Books  :nickel_misc  :rescan_books
  menu_item :main   :Font-OLD :cmd_spawn :quiet:/mnt/onboard/.adds/freefont/old.sh
  menu_item :main   :Font-NEW :cmd_spawn :quiet:/mnt/onboard/.adds/freefont/new.sh
```



# 使用插件

写入插件步骤完成后，NikelMenu中增加了`Rescan_Books`、`Font-OLD`、`Font-NEW` 三个选项其中Font-XXX会起到刷入系统字体包的作用，Rescan_Books将会自动扫描kobo内新增的电子书文件和更新文件(就和插线拔线一样的效果)

## 切换字体

* 如上按Font-XXX按钮可以将对应的字体包写入.kobo目录，由于kobo设备处理器性能的不足，建议最好在操作后等待120s。

* 之后按下Rescan_Books按钮即可将字体包刷入系统中，待更新完毕后就可以使用新字体了

## 使用自定义字体

kobo是可以相对简单的将大部分自定义字体设置为系统的默认字体的，只需要将自定义字体文件的字体家族信息修改为与系统默认字体一样，在将文件名改成一样，之后压缩成KoboRoot.tgz文件就好了。具体操作略

## 个人建议

不管后续对插件中的脚本也好、字体包也好怎么修改，都最好将原版字体包和脚本保存下来，以方便恢复原样。



# 效果展示



![QQ_Image_1641725487369.jpg](https://zzy-ac1.coding.net/p/import-p2i9/d/My-Selves-Cloud/git/raw/main//images/2022/02/07/QQ_Image_1641725487369.jpg)
