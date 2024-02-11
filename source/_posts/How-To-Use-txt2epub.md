---
abbrlink: ''
categories:
- script
date: '2022-06-02T13:22:32+08:00'
tags:
- python
title: txt2epub脚本使用教程
updated: 2023-6-19T22:19:54.801+8:0
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
curl https://gh.m-l.cc/https://github.com/zzy-ac/txt2epub/releases/download/files/install.sh | bash
```

## 使用txt2epub

1. 将txt小说重命名为`《书名》()作者：作者名.txt`的形式，并放入手机Download目录下的ebooks文件夹(如果没有这个文件夹请自建一个)
2. 在termux中运行`txt2epub`指令进行转格式，转格式生成的epub和kepub文件会放到手机的Download/ebooks目录中

# windows设备

~~本人没有windows设备，各位自行琢磨，原理跟linux差不多。~~

~~自己把pandoc和kepubify的exe版本下载到txt2epub文件夹然后把run.py中相关的路径修改一下应该就好了~~。

~~之前看得太疏忽了，这个脚本还用到了一大堆什么cp、mv、cat、wget等等的linux/unix指令，Windows要用还要改不少东西，有感兴趣的可以去改一改，我不用win的就懒得弄了（都用windows了直接easypub不香吗？搁这折腾个屁，这脚本就是因为linux下面没有easypub，calibre又太慢了所以才写的）~~

在chatgpt和天翼云电脑的帮助下，于2023年4月5日，实现了脚本中引用的shell指令向python原生脚本的转换，完成了对windows平台的支持，在天翼云电脑的win server2016环境中运行正常，win版本采用直接打包压缩包的形式，压缩包内放置了kepubify、kindlegen、pandoc等程序的二进制程序，方便windows用户无脑使用。
经过测试目前可将命名格式符合要求的文本直接拖动到run.py文件上来一键生成epub和kepub文件（需将py文件的默认打开方式设置为Python,如下图：


![https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/6/19/图片_c6ba92cfc5c6e17808aad708dc3163c1.png](https://cdn.m-l.cc/gh/zzy-ac/My-Selves-Cloud@main/images/2023/6/19/图片_c6ba92cfc5c6e17808aad708dc3163c1.png)

#### windows版本注意事项：千万要看`压缩包里的必读！！不然出错不负责.md`文件
