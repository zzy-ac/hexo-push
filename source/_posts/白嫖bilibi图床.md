---
title: 白嫖bilibi图床
date: 2021-11-27 12:42:22
tags: 网页部署
keywords:
categories: 图床建设
---

> 本文目标：通过脚本上传图片到B站，并获得外链，以作为图床使用。
> 要求：
> 1. 在kde桌面环境中对图片文件支持右键上传并返回链接到剪贴板，并显示系统通知。
> 2. 在typora中支持从剪贴板粘贴进编辑器自动使用图床

# 一、获取并修改脚本

某群友[阿雅](https://github.com/Brx86/)已经为我们提供了功能完善的[bilibili-picpool](https://github.com/Brx86/bilibili-picpool)脚本，该脚本实现了基本的在终端选择通过图片路径将图片上传到bilibili并输出对应的长、短链接的功能，并且实现了网页端图床的功能。我们只需将其克隆下来稍作修改即可。

```bash
git clong https://github.com/Brx86/bilibili-picpool.git
```

## 配置config.py

首先登录Bilibili，查看Cookie，找到`bili_jct`和`SESSDATA`（必要参数）并填入`config.py`的对应位置

我们找到其中的`uplouder.py`，将其复制并重命名为`uploader-url.py`并修改为如下内容：

```python
import os, requests
from config import cookies

# 定义上传函数
def image_upload(file_path, arg):
    # api地址
    api_url = "https://api.vc.bilibili.com/api/v1/drawImage/upload"

    # 打开图片文件
    with open(file_path, "rb") as f:
        img_file = f.read()

    # 设置post参数
    files = {"file_up": (file_path, img_file)}
    data = {
        "biz": "draw",
        "category": "daily",
    }
    headers = {
        "Origin": "https://t.bilibili.com",
        "Referer": "https://t.bilibili.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0",
    }

    # 向api发送post请求
    r = requests.post(
        api_url,
        files=files,
        data=data,
        headers=headers,
        cookies=cookies,
        timeout=300,
    )

    # 解析返回值，得到图片链接
    img_url = r.json()["data"]["image_url"]
    if arg == 0:
        short_url = b23_link(img_url)
        # 输出结果
        print(f"{short_url}")
        return {"url": img_url, "short_url": short_url}
    elif arg == 1:
        return img_url
    elif arg == 2:
        short_url = b23_link(img_url)
        return short_url


# 定义b23短链函数
def b23_link(url):
    # api地址
    api_url = "https://api.bilibili.com/x/share/click"

    # 设置post参数
    data = {
        "build": 10000,
        "buvid": "archlinux",
        "platform": "archlinux",
        "share_channel": "COPY",
        "share_id": "public.webview.0.0.pv",
        "share_mode": 1,
        "oid": url,
    }

    # 请求api得到短链接
    r = requests.post(api_url, data=data)
    return r.json()["data"]["content"]


if __name__ == "__main__":
    if len(os.sys.argv) == 2:
        file_name = os.sys.argv[1]
        file_path = os.path.abspath(file_name)
#        print("图片上传中...")
        os.system('notify-send -u normal "上传成功" -u low "文件正在上传请稍候片刻" -i markdown-editor-zzy-ac  -a bilibili-picpool')
    else:
        print("格式有误！上传示例图片example.png...")
        file_path = os.path.join(os.sys.path[0], "example.png")
    image_upload(file_path, 0)
```



# 二、实现要求1：kde右键上传

首先看效果：

![upload](https://b23.tv/QRw86JM)

## 创建.desktop文件

```bash
mkdir -p $HOME/.local/share/kservices5/
touch $HOME/.local/share/kservices5/picuploader.desktop
```

## 填上这段内容

```bash
[Desktop Entry]
Actions=bilibili-picpool;
MimeType=image/jpeg;image/png;image/gif;
Type=Service
X-KDE-Priority=TopLevel
X-KDE-ServiceTypes=KonqPopupMenu/Plugin
Icon=markdown-editor-zzy-ac

[Desktop Action bilibili-picpool]
Name=Upload with bilibili-picpool
Name[zh_CN]=使用bilibili-picpool上传
Icon=markdown-editor-zzy-ac
Exec=cd /path/to/bilibili-picpool;python3 uploader-url.py %F | scopy
```

**注: 这里的 scopy 是[竹林子](https://blog.zhullyb.top/)创建的脚本，用以同时满足x11和wayland下的使用，如果你仅使用x11的话直接改成`xclip -selection clipboard`即可。**

MimeType指的是文件类型。在这份desktop中，我仅指定了png和jpg文件在右键时会弹出picuploader的上传菜单，如果你需要更多文件类型的MimeType，你可以参考下gwenview的desktop都写了哪些文件类型。

> MimeType=inode/directory;image/avif;image/gif;image/jpeg;image/png;image/bmp;image/x-eps;image/x-icns;image/x-ico;image/x-portable-bitmap;image/x-portable-graymap;image/x-portable-pixmap;image/x-xbitmap;image/x-xpixmap;image/tiff;image/x-psd;image/x-webp;image/webp;image/x-tga;application/x-krita;image/x-kde-raw;image/x-canon-cr2;image/x-canon-crw;image/x-kodak-dcr;image/x-adobe-dng;image/x-kodak-k25;image/x-kodak-kdc;image/x-minolta-mrw;image/x-nikon-nef;image/x-olympus-orf;image/x-pentax-pef;image/x-fuji-raf;image/x-panasonic-rw;image/x-sony-sr2;image/x-sony-srf;image/x-sigma-x3f;image/x-sony-arw;image/x-panasonic-rw2;

## 安装所需组件

### 通知提示

弹出系统提示的功能依赖于`libnotify`

```bash
sudo pacman -S libnotify --needed
```

### 复制到粘贴板

复制到粘贴版的功能在X11下依赖于`xclip` 而wayland下则 依赖于`wl-clipboard`因此我在此同时安装这两个工具并采用了上文所述的由竹林撰写的脚本

```bash
sudo pacman -S xclip wl-clipboard --needed
```

该脚本用于判断当前桌面环境使用X11还是wayland并自动选择对应的工具：

```bash
/usr/bin/scopy
---
#!/bin/bash

if [ "$XDG_SESSION_TYPE" = "wayland" ]; then
  wl-copy
elif [ "$XDG_SESSION_TYPE" = "x11" ]; then
  xclip -selection clipboard
else
  echo "ERROR! You are using $XDG_SESSION_TYPE"
fi
```

为`/usr/bin/scopy`授予运行权限

```bash
sudo chmod 755 /usr/bin/scopy
```

## 启用该动作菜单

```bash
kbuildsycoca5
```

# 三、实现要求2：在typora中支持从剪贴板粘贴进编辑器自动使用图床

## 先看效果：

![Upload-From-Typora](https://img.xiebruce.top/2020/04/06/daad5bbc462d3ada6abb3e240f7ba75b.gif)

## 具体操作：

如下图，在Typora的`偏好设置`→`图象`→`上传服务设定`里：
![image-20211127135023950](https://b23.tv/zP2FJ8b)
上传服务选`Custom Command`，自定义命令请填入：

```bash
cd /path/to/bilibili-picpool;python3 uploader-url.py 
```

其中`/path/to/bilibili-picpool`是脚本所在路径，如果你的路径不是这个，请修改成你自己的路径(即刚刚clone的仓库的为位置)。



# 绕过B站防盗链

由于某些缘故，B站的的外链做了防盗链的措施，如果直接引用到自己网站上面就会出现无法成功加载的现象。

B站的防盗链，利用的是HTTP的Referer属性做判断。如果Referer是他白名单之外的网站，就会返回403。

这时候我们只需要在想办法在页面的`<head>`标签下添加一行

```html
<meta name="referrer" content="no-referrer">
```

就可以绕过B站的防盗链措施了。

# 最终结果

>  至此我们就实现了最开始的设想——
>
> 1. 可以右键上传图片到图床并获得链接到剪贴板
> 2. 可以在typora中复制图片自动上传图床并填入markdown文件。
