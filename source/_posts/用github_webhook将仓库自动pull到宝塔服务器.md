---
title: 用github_webhook将仓库自动pull到宝塔服务器
date: 2021-07-06 20:29:49
tags: github
categories: 网页部署
---

# 宝塔webhook同步github仓库

  Git仓库有很多代码托管平台，Github、Gitee、Gitlab等等，本文使用Github配置webhook，将github资源同步推送至宝塔，其他git仓库操作大致相同。



## 宝塔配置

### webhook配置

宝塔面板安装webhook插件后，点击设置-添加hook，添加下面的脚本，只需要修改git地址，其他的不用改。
[![img](https://pic.nanbowan.top/picturebed/63ba779432948.png)](https://pic.nanbowan.top/picturebed/63ba779432948.png)

```
#!/bin/bash
echo ""
#输出当前时间
date --date='0 days ago' "+%Y-%m-%d %H:%M:%S"
echo "Start"
#判断宝塔WebHook参数是否存在
if [ ! -n "$1" ]; then
                echo "param参数错误"
        echo "End"
        exit
fi
#git项目路径
gitPath="/www/wwwroot/$1"
#git 网址
gitHttp="https://github.com/xxxxx.git" #只需要修改成仓库的git地址，其他地方默认不修改

echo "Web站点路径：$gitPath"

#判断项目路径是否存在
if [ -d "$gitPath" ]; then
        cd $gitPath
        #判断是否存在git目录
        if [ ! -d ".git" ]; then
                echo "在该目录下克隆 git"
                sudo git clone $gitHttp gittemp
                sudo mv gittemp/.git .
                sudo rm -rf gittemp
        fi
        echo "拉取最新的项目文件"
        sudo git reset --hard origin/master
        sudo git pull
        echo "设置目录权限"
        sudo chown -R www:www $gitPath
        echo "End"
        exit
else
        echo "该项目路径不存在"
                echo "新建项目目录"
        mkdir $gitPath
        cd $gitPath
        #判断是否存在git目录
        if [ ! -d ".git" ]; then
                echo "在该目录下克隆 git"
                sudo git clone $gitHttp gittemp
                sudo mv gittemp/.git .
                sudo rm -rf gittemp
        fi
        echo "拉取最新的项目文件"
        sudo git reset --hard origin/master
        sudo git pull
        echo "设置目录权限"
        sudo chown -R www:www $gitPath
        echo "End"
        exit
fi
```

保存后，点击查看密钥，如下：

```
宝塔WebHook使用方法:
GET/POST:
http://服务器ip:端口/hook?access_key=HOOK密钥&param=aaa
@param access_key string HOOK密钥
@param param string 自定义参数（在hook脚本中使用$1接收）
```

### 初始化git库

在宝塔中创建文件夹，在终端中打开路径并执行初始化如

```
cd www/wwwroot/blog
git init
```

### SSH公钥

如拉取的为私有库，则需配置密钥依次执行，复制生成的公钥（公开库可跳过）

```
cd ~
ssh-keygen -t rsa        #一直回车
cat ~/.ssh/id_rsa.pub
```

## GitHub配置

### webhook填入

点击宝塔webhook查看密钥，将相关信息粘贴至Github中，注意粘贴前把网址最后的aaa换成你的宝塔对应仓库的目录名
例如网站路径 wwwroot/blog，就把aaa替换成blog
如果不替换的话，会在你的服务器根目录创建一个aaa目录，你把站点目录修改为aaa目录，也可以。

[![img](https://pic.nanbowan.top/picturebed/63ba78035f5da.png)](https://pic.nanbowan.top/picturebed/63ba78035f5da.png)

PayloadURl是http://服务器ip:端口/hook?access_key=HOOK密钥&param=aaa内容类型选择json，secret就是webhook的一串密钥，复制过去粘贴，其他默认，保存提交。

### 添加公钥

https://github.com/settings/keys 打开设置ssh页面，点击New SSH key添加标题和刚刚在宝塔生成并复制的公钥
[![img](https://pic.nanbowan.top/picturebed/63bd7ea4c86d1.png)](https://pic.nanbowan.top/picturebed/63bd7ea4c86d1.png)

## 测试

提交git仓库更新，再看Webhook的日志，再检查目录下有没有文件就能看到是否同步成功了。
