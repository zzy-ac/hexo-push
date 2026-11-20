---
abbrlink: ''
categories:
- - kindle
date: '2026-11-20T22:10:08.279763+08:00'
keywords: null
tags:
- kindle
title: 原创插件分享：为 Kindle 打造一个极简、原生且常驻屏幕的 FTP 传书服务
updated: '2026-11-20T22:10:14.286+08:00'
---
项目地址：**https://github.com/zzy-ac/kindle-ftp-server**

**前言**
对于很多  Kindle 老玩家来说，越狱后的第一件事就是寻找一个优雅的无线传书方案。虽然 KOReader 的 SFTP、或者是老牌的  FileBrowser  网页版已经非常成熟，但对于追求“极简主义”和“原生体验”的极客来说，用电脑自带的资源管理器直接拖拽传书，才是最无感的体验。

今天，我为大家分享一款由零开始编写的 **Kindle FTP 插件**。它直接调用 Kindle 底层 BusyBox 内置的 `ftpd` 服务端，轻量且无需后台，最棒的是——**它能像filebrowser插件一样在 Kindle 屏幕最顶端常驻显示 ftp 链接，且完全不影响你正常的看书翻页。**

### 一、 为什么选择纯 FTP 方案？

相比其他无线方案，这个插件的优势在于：

1. **极度轻量**：不依赖 Python，不依赖 Go 语言编译的庞大体，直接唤醒 Kindle 系统自带的 `busybox ftpd`，零内存占用压力。
2. **单次点击启动**：完美融入 KUAL 菜单，点一下“Start”，无需掏出手机或电脑查看 IP，链接直接浮现在屏幕顶端。
3. **常驻且透明**：通过底层的 `eips` 命令结合守护进程，将 `ftp://IP:21` 的文字“印”在最顶端，即使你正常翻页看书，它也会每隔2秒自动覆盖上来，永远不走丢。
4. **完美清理**：在 KUAL 中点击“Stop”后，会执行系统级的进程清洗，并在屏幕上短暂显示 `killall ftpd` 字样，3秒后自动擦除所有痕迹，不留残影。

---

### 二、 功能展示与运行原理

* **启动服务**：点击 `Start FTP` 时，脚本会检查防火墙、放行 21 端口，并映射 root 权限到 `/mnt/us` 目录。随后后台拉起一个显示脚本，将 IP 居中固定在屏幕最上方。
* **客户端连接**：电脑浏览器或 FileZilla 地址栏直接输入 `ftp://你的Kindle IP:21`，账户名为 `anonymous`，密码留空，即可直接读写 `/mnt/us` 下的所有文件。（客户端需要调整为**主动模式**）
* **停止服务**：点击 `Stop FTP` 时，脚本会瞬间清理后台的驻留进程，关闭 21 端口，解除 Kindle 的防休眠状态，然后干净地抹去屏幕上的字迹。

---

### 三、 插件安装教程

**前置条件**：
你的 Kindle Voyage 等机型已完成越狱，并安装了 KUAL（Kindle Unified Application Launcher）。

**kual版本**

之后将下载到的[插件包](https://github.com/zzy-ac/kindle-ftp-server/releases/download/1.0.0/kindle-ftp.zip)解压，并将其中的extensions文件夹拷贝到kindle根目录下。

**Koreader版本**

将koreader的插件包[ftpmanager.koplugin](https://github.com/zzy-ac/kindle-ftp-server/releases/download/1.0.0/ftpmanager.koplugin.zip "ftpmanager.koplugin")解压并放置到kindle根目录下的koreader/plugins目录下。 

---

### 四、 使用方法与注意事项

1. 在 Kindle 上打开 KUAL，找到 `FTP服务器`。
2. 点击 ` 启动FTP服务 `。此时如果一切正常，你的 Kindle 屏幕最顶端正中央会出现 `ftp://192.168.x.x:21`。
3. 在电脑上打开文件管理器（Windows 资源管理器或 Mac 访达），输入该地址。**用户名填 `anonymous`，密码留空**，即可无线上传电子书。
4. 传书完成后，记得在 KUAL 中点击 `关闭FTP`。
5. koreader中同理，在插件中找到`ftp manager`。
6. 点击`start ftp`。
7. 其它跟原生版本一样。
8. 点击`stop ftp`关闭程序。
9. koreader版中增加了一个`status`显示按钮用于查看相关的端口等信息。

**⚠️ 安全与耗电提示：**

* 由于该插件使用了 `-a root` 映射匿名登录，并放行了本地端口，**请仅在绝对可信的局域网环境下使用**。
* 为了防止屏幕被系统刷新覆盖，插件在运行期间会阻止 Kindle 休眠。因此，传完书后**务必点击 Stop**，以免设备持续耗电。
* 如果在使用中遇到部分 FTP 客户端无法列出目录，请在客户端设置中切换为**主动模式 (Active)**。
* 本程序直接调用kindle自带的接口，所以程序极度精简，仅仅2kb左右的空间占用

附上使用效果截图：

![kual页面](https://image.m-l.cc/file/1795184025022_screenshot_2026_11_20T21_23_09_0800.png)

![原生显示效果](https://image.m-l.cc/file/1795184060155_screenshot_2026_11_20T21_23_16_0800.png)

![koreader插件效果](https://image.m-l.cc/file/1795184095025_FileManager_2026-11-20_215357.png)

![koreader插件的信息显示](https://image.m-l.cc/file/1795184121722_FileManager_2026-11-20_212146.png)
