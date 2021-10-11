---
title: 利用Onedrive空间搭建自己的图床
date: 2021-10-11 08:57:13
tags: 图床建设
keywords:
categories: 网页部署
---
## 前言
***
在日常的网站部署中，我们常常需要引用到许多图片，而如果由于各种原因，我们通常希望减少从我们自己的服务器中消耗这部分流量，因此一个合适的图床便显得尤为重要，可以帮助我们在不影响网站运行的同时减少硬盘空间和流量的消耗，达到节省资源的目的。而Ondrive无疑为人们提供了一个很棒的平台，如果你是e5用户/教育用户或者付费的个人用户，那么普遍都拥有较大的存储空间如E5开发者账户就可以拥有25个容量达到5t的帐号，那么利用这个空间不管是用于搭建自己的网盘亦或者图床都是极为便利的。

实现效果：映射你Onedrive的特定文件夹内容，并允许访客在这一文件夹下上传、下载、获取图片直链或引用方式，并为了保护隐私防止其访问到你的其他页面。

## 前提
***
有一台个人服务器（或使用公共免费虚拟空间）
有读写权限的世纪互联版Onedrive或Office365附赠的Onedrive
有个人域名（非必须）

## 最终效果图
***
<center>
<img src="/pictures/tc_picture_00.png" alt="tc_picture_00" style="height: 400px;width: 700px;">
<img src="https://imagehost.mintimate.cn/post_oneindex/effect1.png" alt="tc_picture_02" style="height: 400px;width: 700px;">
<img src="/pictures/tc_picture_01.png" alt="tc_picture_01" style="height: 400px;width: 700px;">
</center>

<br>
搭建好处：

  * 映射自己Onedrive内容
  * 图片提供网络直链（图床功能）
  * 避免消耗服务器流量和空间（直接映射Onedrive）
## 环境准备
***
无个人服务器用户申请免费虚拟空间：https://www.000webhost.com/

有个人服务器用户安装PHP（你也可以使用一些PHP的Serverless服务）

【推荐】为了 方便操作，我这边使用宝塔面板：

宝塔官网：https://www.bt.cn/?invite_code=MV9rd3Jmbno=

服务器安装宝塔后，安装PHP（建议5.6～7.4版本）、Nginx（版本随意）：

<img src="https://imagehost.mintimate.cn/post_oneindex/install.png" alt="install" style="height: 400px;width: 700px;">

之后，选择网站–添加网站：

<img src="https://imagehost.mintimate.cn/post_oneindex/install1.png" alt="install1" style="height: 400px;width: 700px;">

之后打开这个网站的目录，下载这个Oneindex项目master到本目录：

  [众多Ondeindex项目相继倒台后基于Oneindex、OneindexN的OneindexM，作者：Mintimate](https://github.com/Mintimate/OneindexM)
  
### 下载源码
***

<img src="https://imagehost.mintimate.cn/post_oneindex/install2.png" lazyload alt="下载源码"  style="height: 400px;width: 700px;">

之后设置权限，给www用户全部读写权限，进入网站：

<img src="https://imagehost.mintimate.cn/post_oneindex/install3.png" lazyload alt="环境检测"  style="height: 400px;width: 700px;">

之后，点击下一步以后，出现界面：

<img src="https://imagehost.mintimate.cn/post_oneindex/install4.png" lazyload alt="等待参数"  style="height: 400px;width: 700px;">

我们的环境准备就完成了。

## 应用ID和机密

可以从这张图里看到：

<img src="https://imagehost.mintimate.cn/post_oneindex/install4.png" lazyload alt="等待参数"  style="height: 400px;width: 700px;">

我们需要三个参数：

* client_secret：应用机密，即：**客户端密码。**
* client_id：应用ID，即：**应用代号。**
* URL：这个URL用于创建应用时，授权验证。

### 创建应用
***
如果你是Office365送的OneDrive，也就是Onedrive国际版本，到[Microsoft Azure App registrations](https://portal.azure.com/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)内创建。
如果你是世纪互联版本OneDrive，到[Microsoft Azure.cn App registrations](https://portal.azure.cn/#blade/Microsoft_AAD_RegisteredApps/ApplicationsListBlade)内创建。


<img src="https://imagehost.mintimate.cn/post_oneindex/createApplication0.png" lazyload alt="创建应用"  style="height: 400px;width: 700px;">

之后，我们填入需要的参数：

* 名称：最好为纯英文。
* 受支持的帐户类型：如图：选择任何组织目录的账号和个人
* 重定向 URI：这里填入作者Mintimate建立的API：     <code>https://tool.mintimate.cn/oneindexM/ </code>

<img src="https://imagehost.mintimate.cn/post_oneindex/createApplication1.png" lazyload alt="填入参数"  style="height: 400px;width: 700px;">

之后，点击注册即可。

### 获取应用ID
***
应用ID很好获取，注册了后，即可获得：
<img src="https://imagehost.mintimate.cn/post_oneindex/getID0.png" lazyload alt="填入参数"  style="height: 400px;width: 700px;">

### 设置权限
*** 
在获取应用机密前，我们需要设置权限，点击：<code>API权限</code>-<code>Microsoft Graph</code>:

<img src="https://imagehost.mintimate.cn/post_oneindex/setAPI.png" lazyload alt="设置权限"  style="height: 400px;width: 700px;">

依此勾选：

* offline_access
* Files.Read
* Files.Read.All

最后**更新权限**即可：


<img src="https://imagehost.mintimate.cn/post_oneindex/setAPIFinished.png" lazyload alt="设置权限-完成"  style="height: 400px;width: 700px;">

到此，设置权限结束，接下来，我们可以去获取机密了。

### 获取机密
***
最后，我们可以获取应用机密（密钥）了，点击：<code>证书和密码</code>-<code>新建客户端密码</code>：
<img src="https://imagehost.mintimate.cn/post_oneindex/newPasswd.png" lazyload alt="获取密钥"  style="height: 400px;width: 700px;">

按提示设置即可得到：
<img src="https://imagehost.mintimate.cn/post_oneindex/newPasswdFinished.png" lazyload alt="获取密钥-完成"  style="height: 400px;width: 700px;">

## 初始化OneIndex
***
上一步，我们已经得到了**应用ID和机密**，现在我们填入即可：
<img src="https://imagehost.mintimate.cn/post_oneindex/inputID.png" lazyload alt="输入ID和密钥"  style="height: 400px;width: 700px;">

之后，点击<code>下一步</code>-<code>绑定账号</code>，即可完成绑定：
<img src="https://imagehost.mintimate.cn/post_oneindex/makeConnection.png" lazyload alt="绑定确认"  style="height: 400px;width: 700px;">

<img src="https://imagehost.mintimate.cn/post_oneindex/Connection.png" lazyload alt="绑定成功"  style="height: 400px;width: 700px;">

你可以选择**进入后台**,也可以选择直接浏览效果页面。（默认为你OneDrive的根目录）

## 搭建图床
首先，我们需要初始化网盘，进入后台后点击**页面缓存**，选择**重建所有缓存**：

<img src="/pictures/tc_picture_03.png" lazyload alt="tc_picture_03.png"  style="height: 400px;width: 700px;">

之后按顺序点击**图床设置(OneImages)** ，勾选**作为网站首页**以及**允许游客上传图片**：
<img src="/pictures/tc_picture_03.png" lazyload alt="tc_picture_03.png"  style="height: 400px;width: 700px;">
至此我们就完成了一个完整的图床搭建过程，只需要绑定上我们自己的域名，就可以愉快的使用了。（非必须）

 * 注：本文部分内容转载自 <code>Mintimate's Blog</code>[原文地址](https://www.mintimate.cn/2020/09/22/oneindex/)
