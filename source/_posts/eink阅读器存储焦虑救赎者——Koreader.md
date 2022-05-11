---
title: Eink阅读器存储焦虑救赎者——Koreader
date: 2022-05-11 09:29:14
tags: eink
keywords: 
categories: eink
---

# 背景介绍

　　经常使用kindle、kobo等eink阅读器的朋友们，尤其是某些屯书党和漫画党，常会感觉到2G、4G甚至8G、32G的存储空间都有些不够用（反正博主个人是2G的老年机完全够了，不是很理解）。

　　这时一个不限速的超大云空间就显得非常有价值了，如果可以有一个数T乃至数十T大小的云空间，那还有什么书是存不下的呢？但是大多数eink阅读器并不携带这一功能，国内唯一有类似服务的就是和百度网盘合作的小米多看，但百度网盘的下载速度也实在是令人不齿。

　　再此向大家推荐一个方案用于让每一台eink设备都能共享超大的私有云端书库（至少kindle越狱机、kobo、PocketBook和任意安卓设备均可使用）。

# 准备材料

1. 一个eink阅读器
2. koreader最近版与您设备对应的程序
3. 一个天翼云盘、阿里云盘、onedrive、123云盘、和彩云、夸克网盘（或其他alist工具支持云盘）
4. 一个alist列表程序

# 步骤

## 1、给你的eink安装上koreader

　　从官网[KOReader](https://github.com/koreader/koreader/releases)下载最新的koreader安装包用对应的方式安装到你的阅读器上。

## 2、部署一个alist列表程序

　　[alist](https://alist-doc.nn.ci/docs/)是一个将各类网盘挂载并解析出直链的工具，自带的可以方便的白嫖云盘的资源用来当作下载站或仅作为自己的一个在线云盘、影音站等使用。这里将用到alist自带的webdav服务为eink提供一个普适性较强的网盘工具。

### vps部署

　　如果你有一台服务器的话，可以直接用服务器将alist部署到上面。详情参考[官方文档](https://alist-doc.nn.ci/docs/install/script)。

### PaaS部署

　　PaaS是（Platform as a Service）的缩写，是指平台即服务。是一种把服务器平台作为一种服务提供的商业模式。常用的PaaS平台有[Heroku](https://heroku.com/)、[Render](https://render.com/)等。

　　alist官方提供了对多种PaaS平台的支持，具体操作可以查看[官方文档](https://alist-doc.nn.ci/docs/install/paas)，可以从中选择任意一种方案部署你的alist（笔者个人推荐[Heroku](https://github.com/alist-org/alist-heroku-postgres)和[Repl.it](https://github.com/alist-org/alist-replit)）。

## 3、挂载你的云盘

　　alist本身支持如下所示的多种云盘，挑选你自己觉得合适的挂载。（具体挂载流程操作请自行翻阅alist官方文档）

![image-20220511095921873](https://zzy-ac1.coding.net/p/picbed/d/file/git/raw/master/e84f052f25d91cd50b2c15d2b4e4131557c52a91c5bdf6d13c302c38845afb74.png)

*注：阿里云盘、天翼云盘、123云盘、和彩云、夸克网盘、都是在国内能比较方便获取的不限速的大容量网盘，其中阿里云新号完成一些任务后可以获得永久800G左右的空间和十余T的限时空间（一般是几年）；天翼云电信卡、宽带一般都有送数T空间的黄金或铂金会员帐号，也可以去淘宝买永久10T的帐号使用；123是个小企业的云盘，注册就给2t，下载不限速，不过不知道能活多久；和彩云是移动的，注册送1年的1t空间，活动也不少；夸克的话咸鱼可以低价买到88会员送的夸克网盘会员也很大。

## 上传你的书库

　　既然你有那么大的空间需求，那么你一定有自己的一个书库将它按你的习惯分类好并上传到你的云盘（虽然alist可以用来上传，但依然更建议用官方的客户端上传这些大量的文件）

　　分类的话最好是只有单级英文目录，该目录下的所有书都放在着一个文件夹下。例如：新建一个名为Network_novel的目录，然后将所有网络小说放入这一文件夹。

　　到此你已经拥有了属于你自己的云书库。

## 配置alist的webdav账户密码

　　在alist的`管理⇉设置⇉后端`页面下找到`webdav username`和`webdav password`两个选项，设置为自己想要的账户和密码。

## 在koreader上挂载你的云盘

在koreader的`工具`页面找到`云储存`选项并进入：

![image-20220511101702433](https://zzy-ac1.coding.net/p/picbed/d/file/git/raw/master/2afe1921e646de40f694b8946ee1dc2baba94aa813fbb5e28ce2616226e326d8.png)

点击左上角的+号：

![image-20220511101800154](https://zzy-ac1.coding.net/p/picbed/d/file/git/raw/master/67d927825409b11cc9f882c8ab637926d7a904f1bb85104b3ccb7809569b6fa2.png)

在弹出窗口中选择`WebDAV`选项：

![image-20220511101853401](https://zzy-ac1.coding.net/p/picbed/d/file/git/raw/master/4ff095dd9895c4a41dd21bbeead1647572b2fa5f77753dd4d21c63dbfdda2142.png)

服务器显示名称栏填入你想要显示的标签名如：Network novel；

WebDAV地址填入你的https://alist域名/dav/路径，如：https://alist.xxx.xxx/dav/Network_novel (/Network_novel是上文提到存放网络小说的文件夹，在此你需要将你挂载的这一网盘的虚拟目录设置为/)；

`用户名`和`密码`填入刚刚设置的`webdav username`和`webdav password`;

点击添加按钮添加云盘，依次操作将你的各个目录添加到koreader。

![image-20220511102625792](https://zzy-ac1.coding.net/p/picbed/d/file/git/raw/master/b07c55f3568766deeef45246d7801a9cd235dda1d7851ffa5a4243144077be3d.png)

点击刚刚添加好的云盘

![image-20220511102856888](https://zzy-ac1.coding.net/p/picbed/d/file/git/raw/master/72d06f3e0e29476cfb9a25bd633400692ed4927907bcf97162ee3d5ae58137d2.png)

![image-20220511103405124](https://zzy-ac1.coding.net/p/picbed/d/file/git/raw/master/8dc5019fcdb06bb59778ba53137bf8e1d17d7b46ca850f1aa6313c3c0b96b612.jpg)



# 结语

　　至此你已经拥有了一个属于自己的超大、不限速的在线书库。可以随时下载你的海量书库进行查阅与观看。

　　同时koreader、alist也还有更多有趣的用途，读者可以自行发觉、尝试
