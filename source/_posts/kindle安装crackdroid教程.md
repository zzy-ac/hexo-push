---
abbrlink: ''
categories:
- - kindle
date: '2026-08-22T13:37:15.569203+08:00'
keywords: null
tags:
- kindle
- eink
title: kindle(7代之前)安卓系统(CrackDroid)刷机指南
updated: '2026-08-22T13:37:17.031+08:00'
---
# 1、确认机型是否支持

![确认kindle型号](https://image.m-l.cc/file/1787377523764_图片.png)

然后在这个网址比对 MobileRead Wiki - Kindle Serial Numbers
再看是否支持刷安卓

## 1.1 支持机型

Kindle 499（第七代、Kindle Basic 2、KT2）
Kindle Paperwhite 2（Kindle Paperwhite 第六代）
Kindle Paperwhite 3（Kindle Paperwhite 第七代）（日版 32G 漫画版仅支持安卓单系统）
Kindle Voyage
Kindle Oasis 1（仅支持安卓单系统）
Kindle 558 （第八代、Kindle Basic 3、KT3）（仅支持刷安卓 5.1.1 单系统）
Kindle 咪咕版 （KindleXMigu）（仅支持刷安卓 5.1.1 单系统，且需要拆机 TTL）
上面未提到的机型都不能刷安卓

## 1.2 安卓刷机包链接

固件原链接因作者厌恶免费资源被第三方在咸鱼收取手工费代刷，故而选择撤除网盘链接表示抵制（无法理解的请问逻辑，不应该是越免费越公开，贩子才越没法通过信息差赚钱吗？）。所以目前互联网无法获取到作者本人发布的原始文件了。

以下是在互联网搜集到的目前可以找到的最新版本刷机包文件。

[CracKDroid.Flash.Guide.English.Version.2.1.pdf]([https://](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/))

[fastboot.driver.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/fastboot.driver.zip)

[kindle7.230303.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/kindle7.230303.zip)

[kindle8.230118.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/kindle8.230118.zip)

[kindleXmigu.230118.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/kindle8.230118.zip )

[kpw2.230303-duokan.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/kpw2.230303-duokan.zip)

[kpw3.230303.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/kpw3.230303.zip)

[kpw332g.230305.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/kpw332g.230305.zip)

[kpw332g.restore.230305.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/kpw332g.restore.230305.zip)

[oasis.220826.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/oasis.220826.zip)

[oasis.restore.220708.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/oasis.restore.220708.zip)

[voyage.230303.zip](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/voyage.230303.zip)

[安卓系统使用说明.220707.pdf](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/安卓系统使用说明.220707.pdf)

[安卓系统刷机指南.pdf](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/安卓系统刷机指南.pdf)

[原生系统越狱增强包.7z](https://dl.m-l.cc/d/189Open/eink/kindle刷安卓教程/原生系统越狱增强包.7z)

# 2、刷机步骤

刷安卓的前提是越狱并安装了 KUAL
[KUAL 是一款插件启动器，这里用来实现安装安卓]

## 2.1 我的 Kindle 没有越狱？

越狱教程（5.12.2.2 或 5.13.4-5.14.2）：
[Kindle 通用越狱教程：适用固件版本 5.12.2.2-5.14.2 – 书伴 (bookfere.com)](https://bookfere.com/post/970.html)
越狱教程（5.10.3-5.13.3）：
[Kindle 通用越狱教程：适用固件版本 5.10.3-5.13.3 – 书伴 (bookfere.com)](https://bookfere.com/post/892.html)
如固件低于 5.10.3 请升级到 5.12.2 后根据“越狱教程（5.10.3~5.13.3）”进行越狱。
如固件高于 5.14.2 请查看书伴最新的越狱教程

## 2.2 越狱后安装 KUAL

[Kindle 越狱插件资源下载及详细安装步骤 – 书伴 (bookfere.com)](https://bookfere.com/post/311.html#p_2)
注：在步骤 2.2 链接内先安装 1：MRPI 再安装 2：KUAL

越狱完成后，即可开始安装安卓系统。

## 2.3 根据机型下载安卓固件，在电脑上解压缩固件，鼠标右键解压缩到当前目录即可。

注意：目录中不能有特殊字符（例如括号，中文等）
《kindle7.xxxxxx.zip》入门版 499
《kpw2.xxxxxx.zip》Paperwhite 二代
《kpw3.xxxxxx.zip》Paperwhite 三代
《kpw332g.xxxxxx.zip》Paperwhite 三代漫画 32G 版
《kpw332g.restore.xxxxxx.zip》Paperwhite 三代漫画 32G 版恢复原生系统固件
《voyage.xxxxxx.zip》Kindle Voyage
《oasis.xxxxxx.zip》Kindle Oasis
《oasis.restore.xxxxxx.zip》Kindle Oasis 恢复原生系统固件
《kindle8.xxxxxx.zip》入门版 558
《kindleXmigu.xxxxxx.zip》咪咕版
【咪咕/558 刷安卓请参照 B 站 Ygjsz_首页对应视频教程】

## 2.4 在电脑上安装 fastboot 驱动。

![fastboot驱动](https://image.m-l.cc/file/1787377899562_图片.png)

* 注：此处驱动指：

  ![驱动](https://image.m-l.cc/file/1787377958361_图片.png)

解压到新建文件夹并打开

安装提示【Y/ N】请输入 Y 并回车安装【需要多次】

## 2.5 拷贝固件

打开上一步解压缩的固件目录，用 USB 数据线把 Kindle 连接到电脑，直到出现 Kindle磁盘。
把 uboot 目录里的 main-htmlviewer.tar.gz 拷贝到 Kindle 根目录（无需解压缩）。
把 extensions.zip 解压缩到 Kindle 根目录（注意这个文件要解压缩）。
弹出 Kindle 磁盘回到 Kindle 界面（不用拔 USB 线），依次打开【KUAL】、【FlashAndroid】。

如果 Kindle 屏幕闪动并重启，等 Kindle 启动进度条不动（停留在大树界面）就可以继续下面的步骤了。（此时电脑应该会有反复的硬件插入/拔出提示音）注意 Kindle 重启过程中不要操作电源按键。

## 2.6 刷入安卓系统

确保 Kindle 连接到电脑，运行电脑固件目录 Start.exe 程序，若杀毒软件报毒请信任。如果电脑提示安卓系统升级，则输入选项开始更新固件，首次刷机请选择转换为安卓/双系统。

如未出现系统升级提示，可以按住电源键 15 秒重启 Kindle，重新进入下载模式。
如长按电源键 15 秒重启 Kindle 后仍未出现系统升级提示，请检查 fastboot 驱动是否安装到位。
【注：Build 1.6 后的版本系统重置时间较长（4~5 分钟），请耐心等待】

## 2.7 刷回原生系统/转换为双系统

确保 Kindle 连接到电脑，运行电脑固件目录 Start.exe 程序，若杀毒软件报毒请信任。

按住电源键 15 秒重启 Kindle 或者在开机时点击[Enter] Updating Mode。

进入下载模式后打开 Start.exe，选择转换为原生/双系统。

## 2.8 Kindle Paperwhite 3 32G 版刷入方式

KUAL 打开点击 FlashAndroid 等待系统自动重启至进度条卡死。
参照 2.4 安装 fastboot 驱动

打开包内 Start.bat

眼睛盯着 Kindle 屏幕当 Kindle 屏幕左上角出现[Enter] Updating Mode 时，点击[Enter] Updating Mode。（需要耐心等待 4-5分钟）。

工具识别后选择 "2.升级&重置安卓" ，等待自动开机。

如要刷回原生系统，请先把 Kindle 连接到电脑，打开还原包内的 Start.bat 并重启 Kindle，并在 Kindle 屏幕左上角出现[Enter] Updating Mode 时，点击[Enter] Updating Mode，根据提示刷回。

# 3 安卓下越狱原生方法

刷完双系统后进入安卓系统，打开 Eink 设置点击【越狱】按钮；
重启进入原生系统（不要连接 WiFi，不要登录账号），把刷机包目录内的 原生系统越狱增强包.7z 解压到设备根目录，重启；
再次重启进入原生系统，搜索框输入;log mrpi 进行越狱；
把系统语言调节回中文。

# 4 原生系统更新包制作工具

使用场景：
刷了安卓原生双系统后想单独更新原生系统。
使用说明：
下载解压原生系统更新包制作工具，把从官网/书伴下载的官方的升级包（后缀为.bin）放到 工具的 Upd 目录下，打开 Start.bat，选择你的机型后输入升级包的系统版本号，回车等待执行。

执行完成后在工具的 Out 目录下可找到制作出来的原生系统升级包，把Kindle 连接到 电脑后长按电源键重启即可开始升级原生系统。

使用此工具制作出来的升级包可智能识别当前系统为双系统/原生单系统，因此原生单系统也可以使用此工具制作出来的升级包进行原生系统的升级/降级操作。

注意！使用此工具前请保证您的 Kindle 已经升级到 CracKDroid Build 1.5 以上版本，如不是 Build 1.5 以上版本请升级到 Build 1.5 以上版本后再操作。



# 总结

这个包的安卓系统系原来[kdroid](https://kdroid.club)的延续和第三放后续开发版本，总的来说体验与原kdroid没有本质区别，各方面体验均类似。仅去除了kdroid 160元一个的收费验证，并且做了些细节上的细微调整。

总体使用上安卓4.4.2的版本已经无法运行太多有价值的程序，可能对于微信读书有高依赖的用户可以考虑安装，不然没有太多意义。同时这个第三方的安卓包本身对于kindle eink屏幕的支持也稍欠火候，在安卓系统中的刷新体验和显示效果并不尽如人意。总的来说体验不算太好，对于习惯了阅读高质量本地电子书或自制电子书的笔者而言，体验不如直接原生越狱安装koreader的好。甚至因为koreader近期大量高品质插件如simpleUI、ZenUI这类UI插件带来的现代化阅读器外观，或者觅阅、legado、fanqie等第三方阅读平台的支持，都让koreader这个阅读程序重新走上前台获得了更多人的喜欢。

某种意义上来说CrackDroid的发布打破了原kdroid的市场垄断地位，将kindle刷安卓的成本打下来了，目前市场上可见的kindle刷安卓商家价格基本稳定在40元以下，有大量提供低价远程代刷的服务。私以为本刷机包的目的之一是实现了的。至于作者因这些收费较低的代刷服务提供者而毫无通知的全网撤回发布，私以为稍欠些许理智。物以稀为贵，越缺乏，才越滋生昂贵的付费服务。正是因为作者免费包的推出，才让原本160的代刷变成了30-40。若因不满自己的作品被倒卖，而撤回发布，岂不更加滋长了倒卖者的气焰？

该作者目前正在尝试将安卓5.1移植到上述的这些设备上去运行，目前kpw3的公测包已经发布，采取在qq群免费发包、免费进行手动激活的形式，来试图避免作品被倒卖......只能说，祝他好运吧。
