---
abbrlink: ''
categories:
- bitwarden
date: '2023-11-09T19:18:55+08:00'
tags:
- 网页部署
title: 定时备份mysql/mariadb数据库并上传至tgbot
updated: 2023-11-21T10:29:2.502+8:0
---
# 前情提要：

前文[利用koyeb免费自建bitwarden服务端](https://blog.m-l.cc/2023/03/21/li-yong-koyeb-mian-fei-zi-jian-bitwarden-fu-wu-duan/)可知博主之前已经将bitwarden自建的vaultwarden服务端部署在koyeb,并利用db4free提供的免费数据库实现了数据的永久存储。虽说这样基本不会有什么问题了，但db4free毕竟是别人提供的在线数据库，为了以防万一其跑路或者删数据库，今天特地花时间构思了数据库备份的方法。
本文分为两节：

* 基本构思
* 定时推送

## 基本构思

### 备份数据库

想要备份mysql/mariadb的数据库，最方便的莫过于mariadb或mysql自带的mysqldump命令了，只需简单一行就可以将数据库备份到指定的文件。

```bash
mysqldump -h <hostname> -u <username> -p<password> <database_name> > backup_`date '+%F'`.sql
#<hostname>：数据库所在的域名，本地数据库为localhost,此处用的db4free的数据库所以填入db4free.net
#<username>：数据库的用户名
#<password>：显然是密码
#<database_name>：数据库的名称
```

依次填入对应内容后即可备份你的数据库，为了方便记录和存档，这里在生成的备份文件的文件名处添加了`date +%F`来生成带日期的文件名。

### 上传至tgbot

其实这里上传到什么地方都可以，你可以选择部署一个rclone将文件上传到你的onedrive、google drive、webdav等任何网盘去，也可以直接扔到github的releases去，但这里为了图方便（只需要一行就能解决它不香吗？），博主就直接选择了通过curl命令将文件上传给tgbot发送给自己。

```bash
curl -F document=@"./backup_`date +%F`.sql" 'https://api.telegram.org/bot<bot_token>/sendDocument?chat_id=<chat_ID>'

#<bot_token>：从BotFather处获取到的apibot的token
#<chat_ID>：你的telegramID可以从https://t.me/myidbot处使用/getid获取你的id
```

使用上述命令就可以简单的将你的数据库备份文件上传到你的tgbot处，从而实现云端存储。

## 定时推送

### 方案一：vps、机顶盒等

如果你有一台24小时在线的设备，那么你可以选择直接给上面两条命令写一个sh文件并通过crontab实现定时推送，如果你的设备在国内，可能还需要给[https://api.telegram.org](https://api.telegram.org)地址前面加一行反代如`https://r.zzy-ac.top/`从而实现在大陆网络环境下的上传。

### 方案二：github actions

那么如果你就是纯粹的白嫖狗(比如我)，连bitwarden服务端都扔PaaS了，怎么可能还定时服务扔到自己VPS去？给我白嫖！

1. 创建一个github仓库，权限设为私人（Private）

![image-20231109195138845](https://img-blog.csdnimg.cn/fce4c31c34d54b208acc3184582605c8.png)

2. 点击actions创建workflows文件

![image-20231109195419519](https://img-blog.csdnimg.cn/a0df8d40db764398964f9998f49213ab.png)

3. 在yml文件中填入如下内容

```yaml
#自动bitwarden mysql数据库备份
name: Auto Api Task

on: 
  schedule:
    - cron: '12 0 * * *'
  watch:
    types: [started]
   
jobs:
   Task:
    runs-on: ubuntu-latest
    if: github.event.repository.owner.id == github.event.sender.id  # 自己点的 start
    steps:
    - name: Checkout
      uses: actions/checkout@master
    - name: Install MariaDB
      run: |
        sudo apt-get update
        sudo apt-get install -y mariadb-server
    - name: backup and upload to tgbot  #上传到tgbot

      run: | 
        mysqldump -h <hostname> -u <username> -p<password> <database_name> > backup_`date '+%F'`.sql
        curl -F document=@"./backup_`date +%F`.sql" 'https://api.telegram.org/bot<bot_token>/sendDocument?chat_id=<chat_ID>'
    - name: Time #记录上传时间
      run: | 
        echo `date +"%Y-%m-%d %H:%M:%S"` begin > time.log
```

保存之后你就可以白嫖github actions的定时服务自动备份数据库文件了。为了减少服务器压力，建议`- cron: '0 0 * * *'`此处的时间自主设定一个时间，避免大量排队带来的不好体验。

actions运行成功后将会把备份到的数据库文件发送到你的tgbot如下图：

![image-20231109200104152](https://img-blog.csdnimg.cn/1cbffc36466b4b1b997c7f5e0ca57c3d.png)

![image-20231109200125616](https://img-blog.csdnimg.cn/12bfd0c5775747ea846acc3fb553046a.png)

至此，自动定时备份数据库的功能就实现完毕了，在需要还原数据库时可以使用db4free自带的phpMyAdmin将数据库备份文件导入，或通过命令导入。
