---
abbrlink: ''
categories:
- - Linux
date: '2023-07-25T01:13:21.981263+08:00'
keywords: null
tags:
- linux
- armbian
- 机顶盒
title: CM311-1a机顶盒刷armbian日记
updated: 2023-7-25T1:13:26.527+8:0
---

> 前言：进来机顶盒刷机人群日多，其中cm311-1a以其物美价廉，一度广受玩家喜爱，故而本人也采购一台开始了曲折的刷机之路!

## DAY1（失败的尝试。）

自信满满——有点不对啊？——寄了寄了！

由于第一日还未准备好写笔记，所以第一日的折腾内容忘记拍照/截图了，只有两张拆机后的图，不过不要紧，今天的步骤明天都得再来1～N遍的(TдT) ，写到明天的笔记去吧。

### 自信满满

刚拿到机子，回家开机，adb连接，芜湖都没问题十分丝滑！

做系统盘，挎挎完成，哎呦好像挺简单？

装启动U盘系统！挎挎，毫无压力的进入armbian。

哎呦到这里似乎都还蛮简单的？

### 有点不对啊？

继续按照教程重启！

哎？怎么关机命令无效？怎么回事？要不我直接关电源算了？试试吧

啊寄！

灯亮了，但是路由器识别不到设备了，找不到设备ip了。貌似砖了？

### 寄了寄了！

至此day1的折腾宣告结束，直接变砖了QAQ。只能去京东斥7元巨资买了usb公对公的数据线准备明天的救砖吧。

然后就是研究怎么拆机，一开始以为是只有卡扣的设计，所以尝试硬掰QaQ结果好几个卡扣断裂了的说。

后来查明是后盖还有俩螺丝要拧，星夜去附近小商店2元斥巨资购入一个小螺丝刀，嘤嘤嘤，至此，额外的消费已经达到9元了(╯TдT)╯

成功拆解机顶盒并找到了需要短接的焊点。第一天的瞎折腾到此结束，明天救砖回来再继续弄吧。

![image-20230724211329657](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/07/24/image-20230724211329657.png)

![image-20230724211537108](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/07/24/image-20230724211537108.png)

## DAY ~~2~~ 1.5

## 不用等到day2了！

突然发现电脑有type-C口，试了一下，果然可以用type-C转usb-a的这种普通手机充电线来刷机顶盒！！！哇咔咔卡卡！！！立省7元！

直接短接、刷入救砖包！

![捕获](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/07/25/捕获.PNG)

等进度条走完后拔掉数据线，关闭电源不再短接，正常开机进入安卓！

## 正常的刷机流程

### 制作启动盘

打开balena-etcher，下好armbian镜像，解压镜像，用balena-etcher将镜像写入U盘。

### 开心盒子（其实感觉琢磨琢磨，直接用adb指令也可以，不过懒得琢磨了）

直接打开开心盒子输入机顶盒ip（进路由器查，或者连上hdmi在屏幕里看。
adb连接上机顶盒！

![捕获-1](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/07/25/捕获-1.PNG)

点击调试，点击从U盘/SD卡开启，并在点击后迅速将U盘插入！

![捕获-3](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/07/25/捕获-3.PNG)

稍等片刻后，在路由器上确定armbian的ip,并ssh进入u盘系统。

首次进入需要修改root用户密码，创建普通用户，确立时区和语言等：

![捕获-4](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/07/25/捕获-4.png)

然后使用armbian-install -m no开始将U盘系统写入机顶盒！

![捕获-6](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/07/25/捕获-6.png)

这里我用的cm311-1a-yst版本所以直接选择305,并使用习惯的ext4文件系统，选择1。

稍等片刻后没有报错并按照提示poweroff关机即可。

![捕获-7](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/07/25/image-20230725010716968.png)

关机后，关闭电源，拔掉U盘，重新开机之后即可正常进入机顶盒内的armbian系统！！！

![捕获-8](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2023/07/25/image-20230725010851979.png)

## 芜湖！！起飞啦！！！

至此，一个艰苦朴素颇为曲折的armbian就终于装到我们的cm311-1a上去了！！！

（一定要选对内核版本，例如7月24日发布的6.1.40版本内核的包就存在问题，无法正常安装，各种怪事，鬼知道我在意识到是内核问题之前反复救砖了多少回(╯TдT)╯！

获得一台舒适的armbian主机之后应该干些什么呢？今夜过于晚了，博主先睡了，内容留到8月份再水一篇博客啦！哈哈哈哈哈哈！
