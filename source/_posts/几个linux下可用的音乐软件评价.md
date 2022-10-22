---
title: 几个linux下可用的音乐软件评价
date: 2022-10-22 19:27:29
tags: music
categories: music
---

> 音乐在我们每个人的生命中常常发挥出重要的价值，一首动听的曲子常常能给人带来欢乐，因此今天简单的向大家介绍几款适合中国人的音乐程序：

# 闭源系列

## QQ音乐

QQ音乐作为腾讯旗下众多音乐app中的扛把子，在版权上有着先天的优势，同时随着近年来的不断努力，腾讯的QQ音乐也终于凑齐了win、mac、linux、iphone、android全平台的官方客户端。

![image-20221022193629599](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022193629599.png)

其中linux客户端是基于electron架构运行的，目前已可以正常的流畅运行于全部的linux发行版中：

![image-20221022193957231](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022193957231.png)

![image-20221022194010776](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022194010776.png)

### 优势

* QQ音乐庞大的曲库
* 简洁优美现代感十足的界面
* 有HD版本，对安卓平板也有较好的支持

### 不足

* 相比于其它平台的版本，linux端存在严重的功能缺失，很多功能没有实现，例如：本地音乐播放和封面歌词识别、听歌识曲等



## 网易云音乐

网易云音乐是网易在几年前与deepin合作出品的linux客户端，最后一次更新于2019年，linux端的网易云音乐基于自研架构，基本实现的当年windows版客户端的全部功能。

与QQ音乐一样，网易云音乐也推出了全平台的客户端，并且均实现了完善的功能体系：

![image-20221022194939491](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022194939491.png)

![image-20221022195041144](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022195041144.png)

### 优势

* 功能完善，基本实现了和其它平台同样的功能
* 自建架构，内存占用较低
* 协议正确，播放音乐可以正常被MPRIS识别出来，并显示于系统的媒体播放器中。
* 可以播放本地音乐，并且自动为其识别封面和歌词

### 不足

* 随着linux版本的更新，和软件的长久停止维护以及网易云自身api的变动，目前发现音乐栏的个性推荐页面已经无法访问（至少在archlinux上是这样）

![image-20221022200440403](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022200440403.png)

* 与QQ音乐相比曲库不那么全面
* 界面比较陈旧，与现代软件存在一定的脱节（不过又不是不能用）
* 虽然支持全平台，但是对安卓平板并没有专门的适配，体验不佳

## 闭源系列总结

国产音乐程序的linux客户端好像就是这俩了，各有千秋吧，个人比较喜欢网易云一些。



# 开源系列

## lx-music

落雪音乐集合了QQ音乐、网易云音乐、酷狗、酷我、咪咕五大国产音乐平台的api。

![image-20221022201533992](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022201533992.png)

![image-20221022201601777](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022201601777.png)

![image-20221022201959981](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022201959981.png)

![image-20221022202113541](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022202113541.png)

### 优势

* 支持除iphone之外的全部平台，并且对安卓平板也有良好的适配
* 拥有国内五大家的音乐资源
* 界面简洁
* 在线功能相对完善

### 不足

* 不能播放本地音乐
* 界面简洁得有点简陋了

## listen1

Listen 1可以搜索和播放来自网易云音乐，QQ音乐，酷狗音乐，酷我音乐，Bilibili，咪咕音乐网站的歌曲，让你的曲库更全面。

![platform](http://i.imgur.com/R6bTXkY.gif)

还支持歌单功能，你可以方便的播放，收藏和创建自己的歌单。

![platform](http://i.imgur.com/Ae6ItmA.png)

### 优势

* 相比lx-music更多了一个bilibili源，曲库更加丰富
* 可以创建自己的歌单，而lx-music只能导入其他平台的现有歌单
* 可以播放本地音乐，并正确识别歌词
* 拥有四种主题，均体现出了简洁、美观、现代化的特征
* 创造性的增加了浏览器插件的版本，用此方式实客户端开源的音乐程序就相对比较多了，个人感觉目前比较出彩的也就listen1、lx-music这两个，其他的一些客户端如网易云音乐的electron客户端之类的，个人感觉在有原生客户端的情况下，似乎并没有多少存在的必要性。现了更为出色的多平台兼容性。

### 不足

* 没有本地音乐无法正常识别封面
* 现代白、黑主题存在一定的bug,在部分设备上比较卡
* 使用的electron13版本相对比较陈旧，用较新版本的electron打开时会存在各种bug
* 虽然做了android端，但更新与桌面端不同部，存在较多问题，目前无法正常使用，并且没有iphone端。

## YesPlayMusic

一款高颜值的第三方网易云播放器

![image-20221022203124553](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022203124553.png)

拥有如下图所示的超多特性：

![image-20221022203225962](https://cdn.dmnb.cf/gh/zzy-ac/My-Selves-Cloud@main/images/2022/10/22/image-20221022203225962.png)

支持linux、mac以及windows系统，可以部署在vercel或vps搭建网页版程序。

### 优势

* 可以自己搭建到vercel或vps上部署一个自己的在线音乐平台
* 界面比较美观、现代

### 不足

* 没有移动端
* 部署的网页版也无法在移动端安卓苹果设备上使用
* 只有网易云这一个音乐源



## 开源系列总结

客户端开源的音乐程序就相对比较多了，个人感觉目前比较出彩的也就listen1、lx-music这两个，其他的一些客户端如网易云音乐的electron客户端之类的，个人感觉在有原生客户端的情况下，似乎并没有多少存在的必要性。



# 总结

目前各类国产音乐软件中由官方出品的两款都实现了全平台的兼容，并且都有着官方的支持，相较之下的确各有千秋。

开源客户端中，个人看好listen1和lx-music，其中在电脑端主要使用listen1的桌面版，而移动端和平板上主要使用lx-music。

其实listen1的浏览器插件版与桌面版区别不大，个人感觉最大的区别就是本地音乐的功能以及桌面歌词。