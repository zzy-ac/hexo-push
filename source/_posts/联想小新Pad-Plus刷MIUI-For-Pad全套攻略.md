---
title: 联想小新Pad_Plus刷MIUI_For_Pad全套攻略
date: 2022-11-27 13:32:50
tags: Android
categories: Android
---

联想自20年起推出的小新系列平板，一度以极高的性价比和完善的品牌保障著称，各个型号均有其优势，但联想自研的ZUI系统属实令人困扰，各种奇奇怪怪的BUG令人无语至极，虽然总体来说使用体验还不错，但社会拒绝更好的体验呢？因此[@老大的小跟班](https://wpa.qq.com/msgrd?v=3&uin=2277216453&site=qq&menu=yes)利用小米平板的底包制作了适配联想小新系列的MIUI_Fro_Pad包，并提供持续的维护。

本教程讲述了博主给自己联想小新Pad_Plus刷入MIUI的全过程，和使用体验。

# 一、刷机过程

## 备份文件

自己想办法把要用的应用全都提取出来，把要保存的文件都提取出来，如果之前以及root了，那甚至可以直接把应用数据等也一起备份出来，直接用，博主之前没有root所以自己单独把apk全提取出来后把要用的文件复制出来了。

## 解锁BL

### 1.开启USB调试
在平板设置里【关于本机】→【ZUI版本】（多点几下）→【开发者选项】→【USB调试】→【一律允许调试】

### 2.获取解锁文件
~~先在ZUI解锁官网解锁，需要输入序列码（S/N）。获取序列码有三种方法：购买小新的盒子说明、平板背面贴的小字条、fastboot模式（如有遗漏，欢迎评论区补充）。提交申请后去邮箱查看，要是【收件箱】找不到就在垃【圾广告邮箱】里找~~

现在官网已经收回了自助获过程取解锁文件的权限，如今解锁平板需要自己发邮件给hucy4@lenovo.com，写明详细需求包括解锁用途、设备序列号等，然后等待人工回复提供解锁文件。

![image-20221127135505818](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/11/27/image-20221127135505818.png)

获取解锁文件后，将解压出来的img文件重命名为sn.img后放入`联想解锁回锁工具`目录，运行`联想解锁.bat`脚本。

## 9008刷入ZUI12.6线刷包

大部分人反应直接从ZUI13刷到MIUI会因为System分区过小失败，因此先刷回ZUI12.6。

### 1.安装QPST高通9008刷机工具（如果已经安装过软件可以不用重复安装，本次演示针对首次使用的童鞋）
①双击setup.exe安装升级工具，出现如图界面 点击Install（安装）；

②勾选“我已阅读并接受许可条款”，点击安装；
③安装过程，简单说就是一路选择 I Agree，点击NEXT，直到提示安装完成（installation complete）时，点击Close关闭安装界面。

### 2.刷机/降级
①点击“QFIL”打开升级工具；（Windows 7路径：开始菜单- 所有程序-QPST-QFIL，Windows 10路径：开始菜单→QPST→QFIL）
②进入“QFIL”的“Configuratiion”标签页的 “FireHoseConfiguration”，按如下红框部分进行配置，device type选择“UFS”,点击OK确认保存；

![img](http://image.coolapk.com/feed/2021/0906/13/797820_54a95e73_7682_9864@488x581.png.m.jpg)

③重新返回QFIL主界面，选择“Meta Build”；
④点击“Load Content“，找到解压后的固件包，选择“contents.xml”文件，点击“打开”；

![img](http://image.coolapk.com/feed/2021/0906/13/797820_301d5c0c_7682_9866@942x591.png.m.jpg)过程

⑤平板关机，按住音量上键（只需要按住音量上键，别和别的按键凑数同时按），USB数据线插入手机，然后放开音量键，大概等待2s左右，QFIL软件自动识别到9008端口，这个时候才可以点击“Download Content”， 开始刷写固件，然后蓝色进度条开始走动。 （请注意操作方式，如果没有进入9008端口，就刷不了机）

![img](http://image.coolapk.com/feed/2021/0906/13/797820_56345c0d_7682_9868@1000x693.png.m.jpg)

(注意：如果QFIL工具提示 please select an existing port，请点击右上角select a port，勾选9008点击OK）

![img](http://image.coolapk.com/feed/2021/0906/13/797820_6322731d_7682_987@796x554.png.m.jpg)

⑥升级成功后提示“Download Succeed”，此时可以看到蓝色进度条走完。
此时平板自行重启，待重启好了之后，平板已经降级成功！

## 刷入第三方TWRP

其实官方rec也可以刷，不过用上第三方的后续备份、root之类的更方便。

解压`联想小新PadPlus-twrp.zip`文件，运行`残芯专用TWRPRecovery刷入工具Win版V2.1.exe`将目录下的`联想小新PadPlus-twrp3.6.0-11_0-recovery-自动解密-21.12.15-残芯专用工具刷入.img`刷入即可。

## 刷入MIUI

下载MIUI的刷机包，解压后找到对应型号的bat脚本，运行它，跟着一步步走就好了，基本只需要回车。（当然你也可以读完脚本之后自己手动一步步来）



1. 手机关机进入第三方twrp,点重启，重启至fastbootd，，，大概这样子

![image-20221127142332627](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/11/27/image-20221127142332627.png)

2. 点开一键刷入MIUI13.bat(一共三个bat文件，请点开对应机型的bat文件)

![image-20221127142343138](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/11/27/image-20221127142343138.png)



3. 按着bat上的提示按回车键，完成一个按一下。如果没反应请检查驱动

   ![image-20221127142357068](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/11/27/image-20221127142357068.png)

   ![image-20221127142424793](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/11/27/image-20221127142424793.png)

   ![image-20221127142431348](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/11/27/image-20221127142431348.png)

   ![image-20221127142437041](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/11/27/image-20221127142437041.png)

   ![image-20221127142443323](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/11/27/image-20221127142443323.png)

   ![image-20221127142451106](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2022/11/27/image-20221127142451106.png)

4. bat执行完成后手机将自动进入twrp
过程
5. 清除，格式化data，然后点返回，然后点重启（已经是MIUI的，在后续版本维护时不需要格式化data）

6. 开机进开机向导不要连接WiFi！！！有跳过就点跳过即可成功进入系统。

## 完成
至此MIUI就刷入完成，总体来说并不复杂，接下来讲讲使用体验。

# 二、使用体验

## 免费版

免费版的固件是用最后一个开发版的MIUI做的，目前几天用下来的感觉是BUG不少。

1. 蓝牙音量锁死最大无法调节
2. 会经常性黑屏，失灵，无法操作
3. 部分应用无法自适应深色模式
4. 默认情况下dpi设置有问题，图标排布会乱，要自己手动改成700才行
5. 没法使用杜比音效
6. 没法启用护眼模式
7. 等等

排除上诉这些bug的因素的话，免费版的系统还是很够用的，MIUI的智慧分屏、对微信hd的适配、与小米手机间的妙享和应用流转、文件互联等等都非常方便，MIUI的动画也相对舒适。

## 付费版

付费版的固件是用稳定版的MIUI制作，总体来说和免费版没太大差别，只是修复了上述的bug,让MIUI系统在联想小新Pad_Plus上的体验几乎达到了与小米平板本身同等层次的水准。

不过目前付费版的第四版在我的实际体验中，维护者宣称已经修复了的上述BUG-6依然存在，不过我一般也用不到，所以无所谓了。

上述提到的需要用到除付费版固件之外的文件目前已经上传到网盘：

https://cloud.189.cn/web/share?code=VzUBVnUfaUnq

（访问码：3uce）

免费版第八版的固件直接使用作者发布的123网盘：

https://www.123pan.com/s/Y2iRVv-GaYX

（提取码:6666）

需要付费版固件的可以自己从酷安等地方联系开发者，给他们捐赠6.66进群获取。（虽然博主不太赞成这种行为，但是也尊重开发者的选择，毕竟不是所有人都可以为爱发电）
