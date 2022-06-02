---
title: txt2epub脚本使用教程
date: 2022-06-02 13:22:32
tags: python
categories: script
---


> 项目地址：
> [https://github.com/zzy-ac/txt2epub](https://github.com/zzy-ac/txt2epub)
# linux设备

```bash
#安装
git clone https://github.com/zzy-ac/txt2epub.git
cd txt2epub
wget https://raw.githubusercontent.com/zzy-ac/txt2epub/termux/requirements.txt
pip3 install -r requirements.txt
#运行
python3 run.py </path/of/novel>
```



# Android设备

## 安装txt2epub

1、安装termux

2、切换清华镜像源：

```bash
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main@' $PREFIX/etc/apt/sources.list
apt update&&apt upgrade
```

3、运行如下指令：

```bash
curl https://gh.dmnb.cf/https://github.com/zzy-ac/txt2epub/releases/download/files/install.sh | bash
```



## 使用txt2epub

1. 将txt小说重命名为`《书名》()作者：作者名.txt`的形式，并放入手机Download目录下的ebooks文件夹(如果没有这个文件夹请自建一个)
2. 在termux中运行`txt2epub`指令进行转格式，转格式生成的epub和kepub文件会放到手机的Download/ebooks目录中



# windows设备

本人没有windows设备，各位自行琢磨，原理跟linux差不多。

自己把pandoc和kepubify的exe版本下载到txt2epub文件夹然后把run.py中相关的路径修改一下应该就好了。
