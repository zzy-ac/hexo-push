---
title: 腾讯云安装archlinux并通过docker运行宝塔面板
date: 2021-11-14 23:18:46
tags: linux
categories: archlinux
---

# 一、archlinux系统安装

> 鉴于日常使用过程中对archlinux的习惯与依赖，一个熟悉的生产环境对于个人服务器就显得日益重要起来。然而大多数国内的主机服务商并不提供archlinux的服务器镜像，也不提供自定义镜像的服务，这无疑给人带来困扰。因此在这里提供一个将服务器转化为archlinux系统的教程。


## 准备
首先，你得有一个linux系统的服务器，如centos/debian/ubuntu等。
其次，你需要一个能访问github的网络（最好）
之后，你的服务器上至少要安装有`curl` 和`wget`两个基础的应用。

## 安装
大概鉴于类似的需求，早已有大佬(肥猫老哥牛批！！！！)在github上上传了[vps2arch](https://github.com/felixonmars/vps2arch)脚本。通过这款脚本我们可以傻瓜式安全的在我们的服务器上安装archlinux系统
![Screenshot_20211114232846.png](https://cloudpic.m-l.cc/images/2021/11/14/Screenshot_20211114232846.png)
你只需要按照肥猫大佬在README.md中写到的那样在你的服务器中输入三行指令：

```
wget https://felixc.at/vps2arch
chmod +x vps2arch
./vps2arch
```
然后静静的等待收获一个archlinux操作系统的服务器就好了。

此时_Arch Linux_已安装，但尚未配置。该脚本将提供一个支持 SSH 的系统，自动配置 grub（或 syslinux）、网络并从原始系统恢复 root 密码（如果没有设置 root 密码，则使用`vps2arch`作为密码）。

## 配置
在安装完archlinux系统之后我们可以对其进行一些简单的配置如修改一下镜像源地址、装一下sudo、nano、vim、curl、wget之类的常用软件。

## 完成
至此我们就顺利收获了一个archlinux系统的vps。

# 二、使用docker配置一个宝塔面板环境。

> 由于本人之前使用服务器时是在debian10的系统环境下借助宝塔面板来操作的。因此出于习惯(偷懒)本人没有尝试直接用ngnix或其他web服务软件来部署网站，而是希望继续使用宝塔面板。

## 需求

* 一个能使用宝塔面板的docker
* 能成功在宝塔面板上部署网页并通过端口映射到宿主机从而实现外部访问。

## 可选的方案
* 直接在docker hub上找一个装好了宝塔面板的镜像来安装就完事了。（方便、省事，不过大多数是centos环境，令本人十分不适，且部署python环境之类的很多时候都需要手动编译，费时费力）
* 老老实实装一个最简安装的debian/ubuntu,然后用宝塔官方提供的脚本一键安装宝塔面板（可能稍微多几个步骤，而且装出来的面板配置一些端口比较麻烦，但是装好后很舒适（毕竟之前服务器就用的debian））

## 准备
ssh 进入已经装好的archlinux服务器
使用指令

```bash
# 第一步 通过pacman安装docker  
sudo pacman -Sy docker --needed --noconfirm
# 第二步 用systemctl将docker服务设置为开机启动  
sudo systemctl enable docker
# 第三步 用systemctl启动docker服务  
sudo systemctl start docker  
# 第三步 将本地用户加入docker用户主  
sudo gpasswd -a ${USER} docker
```

来安装并简单配置好docker的环境。之后使用`docker info`  来测试是否已经成功安装好docker
以下在虚拟机下的输出结果，部分信息隐藏

```bash
Client:
Debug Mode: false



Server:
Containers: 0
Running: 0
Paused: 0
Stopped: 0
Images: 0
Server Version: 19.03.13-ce
Storage Driver: overlay2
Backing Filesystem: extfs
Supports d_type: true
Native Overlay Diff: false
Logging Driver: json-file
Cgroup Driver: cgroupfs
Plugins:
Volume: local
Network: bridge host ipvlan macvlan null overlay
Log: awslogs fluentd gcplogs gelf journald json-file local logentries splunk syslog
Swarm: inactive
Runtimes: runc
Default Runtime: runc
Init Binary: docker-init
containerd version: xxxxxx
runc version: xxxxx
init version: xxxx
Security Options:
seccomp
Profile: default
Kernel Version: 5.9.1-arch1-1
Operating System: Arch Linux
OSType: linux
Architecture: x86_64
CPUs: 4
Total Memory: 3.812GiB
Name: archlinux
ID: xxxxxxxx
Docker Root Dir: /var/lib/docker
Debug Mode: false
Registry: https://index.docker.io/v1/
Labels:
Experimental: false
Insecure Registries:
127.0.0.0/8
Live Restore Enabled: false
```

重新登入來套用新权限，或者你可以用这个指令让现在的使用者阶段套用新群组：  
`newgrp docker`

## 安装docker镜像

### 使用基于centos创建的自带完善的宝塔环境的docker[镜像](https://hub.docker.com/r/pch18/baota)。

具体操作参考该作者的介绍，遇到的问题可以先参考一下issus中给出的解决方案。
![Screenshot_20211115000039.png](https://cloudpic.m-l.cc/images/2021/11/15/Screenshot_20211115000039.png)


### 使用官方的debian最简镜像来手动安装宝塔满版

```bash
docker run -tid --name baota --net=host --privileged=true --shm-size=1g --restart always -v ~/wwwroot:/www/wwwroot debian
```

在这里我们使用docker的HOST模式来运行docker镜像，这样,不需要设置映射端口,自动映射宝塔面板全端口到外网正常的bridge模式可能会造成网站后台不能获取用户真实ip地址。

随后使用宝塔[官网的一键安装脚本](https://www.bt.cn/bbs/thread-19376-1-1.html)来安装面板

![Screenshot_20211115000209.png](https://cloudpic.m-l.cc/images/2021/11/15/Screenshot_20211115000209.png)

### 注意，这样安装的宝塔面板需要在debian的docker中手动配置好ssh服务的端口不然无法在面板中直接使用终端。

# 结语

文至于此，安装一个带有宝塔面板的archlinux服务器的工作就基本完成了，剩下的无非是照常的部署网页、配置定时任务之类的。虽然文章不长，总体的过程看起来也比较简单、清晰，但却实实在在耗费了点墨近一整天的时间（这个点墨就是逊了啦）。最后总结出这篇简单的教程，希望可以帮到看到本文的有缘人（其实就是做个笔记怕自己忘了，万一下回崩掉了也好恢复不是～～～）

