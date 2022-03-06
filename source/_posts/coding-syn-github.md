---
title: Coding同步Github仓库
date: 2022-03-06 08:36:31
tags: github
keywords:
categories: github
---

> 很多时候当我们访问github仓库时会感到十分显著的延迟问题，由于很多原因，原本可以直接引用到网页中的github直链无法正常使用，仓库的克隆和使用也非常困难。为此大家尝试过各种各样的方法来对github进行提速，有人通过cloudflare搭建反代，有人通过cdn搭建镜像站，也有人通过gitee来同步仓仓库。而今天主要介绍用户coding对github仓库进行实时同步的方法。

# 为什么选择Coding

Coding作为与Gitee齐名的两大国内git服务商，相比于小家子气的码云显得要大气得多。

在Gitee的使用中总存在着各种各样的严苛限制，仓库的大小、对实名认证的需要、pages的手动部署，但最为让人无语的还是它对于超过1M的文件都需要登陆后才能下载的限制，这直接导致了无法在不登陆的情况下引用Gitee仓库的图片直链到自己的网站中来。

![image-20220306085214473](https://zzy-ac1.coding.net/t/zzy-ac1/p/import-p2i9/d/My-Selves-Cloud/git/raw/main/images/2022/03/06/image-20220306085214473.png)

因此，几番辗转之下，博主了解到了Coding这样一个更加开放的国内git平台，在同样提供git服务的前提下，Coding比Gitee减少了许多的限制，其中最重要的就是它和Github一样可以直接提供仓库文件的直链，而不需要所谓的超过1M就得登陆。这让Coding的可实用性得到了巨大的保障。

![image-20220306085718811](https://zzy-ac1.coding.net/t/zzy-ac1/p/import-p2i9/d/My-Selves-Cloud/git/raw/main/images/2022/03/06/image-20220306085718811.png)

# 从Github同步仓库到Coding

既然决定了使用Coding来对Github仓库进行同步那么接下来就介绍一下步骤：

## 简单的定时同步Github仓库

如题，只是简单的同步Github仓库，每天可以定时自动拉去Github的更新，从而实现自动同步的效果。

* 登陆Coding进入`项目`版块

![image-20220306090630641](https://zzy-ac1.coding.net/t/zzy-ac1/p/import-p2i9/d/My-Selves-Cloud/git/raw/main/images/2022/03/06/image-20220306090630641.png)

* 点击右上角创建项目旁的···

  ![image-20220306091422419](https://zzy-ac1.coding.net/t/zzy-ac1/p/import-p2i9/d/My-Selves-Cloud/git/raw/main/images/2022/03/06/image-20220306091422419.png)并选择导入项目，在导入页面选中Github旁的开始导入按钮。

  ![image-20220306091657284](https://zzy-ac1.coding.net/t/zzy-ac1/p/import-p2i9/d/My-Selves-Cloud/git/raw/main/images/2022/03/06/image-20220306091657284.png)

* 在这里你可以选择输入Github用户名来获取想要导入的仓库或者直接输入Github仓库的git地址来进行导入。任选其一开始导入你所需要的仓库。

  ![image-20220306091837496](https://zzy-ac1.coding.net/t/zzy-ac1/p/import-p2i9/d/My-Selves-Cloud/git/raw/main/images/2022/03/06/image-20220306091837496.png)

* 稍等一会儿后我们可以看到仓库已经成功的导入Coding了，进入导入的项目中打开我们导入的这一仓库。

  ![image-20220306092153675](https://zzy-ac1.coding.net/t/zzy-ac1/p/import-p2i9/d/My-Selves-Cloud/git/raw/main/images/2022/03/06/image-20220306092153675.png)

![image-20220306092208117](https://zzy-ac1.coding.net/t/zzy-ac1/p/import-p2i9/d/My-Selves-Cloud/git/raw/main/images/2022/03/06/image-20220306092208117.png)

* 在仓库的设置中选择`同步信息`标签，并勾选开启自动同步并设置同步时间。



至此，最基本的简单同步就已经完成了，每天固定时间，Coding会自动为我们拉取最新的Cithub仓库。



## 利用Github Actions实现实时同步Github的每一次push

在某些情况下，我们可能不想等到一天之后再同步Github的仓库，而是希望可以将Github的每一次改动都及时的同步过来，这时候我们可以利用Github Actions服务来实现这一功能。

这里我们使用[serverlesslife-cn/sync-repo-to-coding](https://github.com/serverlesslife-cn/sync-repo-to-coding)项目来实现。

### SSH 密钥配置

创建一个 [SSH key](https://help.github.com/en/github/authenticating-to-github/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) ， 将公钥`id_rsa.pub`保存到 [Github SSH keys](https://github.com/settings/keys)和 「CODING 个人账户——> SSH公钥」， 将私钥 `id_rsa` 在 GitHub 项目的 Settings -> Secrets 路径下配置好 CODING_PRIVATE_KEY

![add-secret](https://gh.zzy-ac.workers.dev/https://raw.githubusercontent.com/serverlesslife-cn/sync-repo-to-coding/master/img/add-secret.png)

### 创建workflow

在仓库的.github/workflows目录下创建一个yml文件，并填入如下内容：

```yml
name: Sync Repo to CODING
on:
  push:
  schedule:
    # 每天北京时间0点同步
    - cron:  '0 16 * * *'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Sync Repo to CODING
      uses: serverlesslife-cn/sync-repo-to-coding@master
      env:
          # 在 GitHub Settings->Secrets 配置 CODING_PRIVATE_KEY
          SSH_PRIVATE_KEY: ${{ secrets.CODING_PRIVATE_KEY }}
      with:
          # 注意替换为你的 GitHub 源仓库地址
          github-repo: "git@github.com:serverlesslife-cn/sync-repo-to-coding.git"
          # 注意替换为你的 CODING 目标仓库地址
          coding-repo: "git@e.coding.net:donghui1/serverlesslife/sync-repo-to-coding.git"
```

至此我们基本上完成了，自动实时同步Github的目标，但是我们可以发现，在上述的yml中我们还加入了crontab定时启动的条件，这会让我们每天定时同步Github仓库到Coding——是不是很眼熟？这一功能明明之前在Coding里面就通过自带的同步功能实现了，因此为了避免没必要的浪费行为，我们可以将这一行抹去，改为只有push行为才能触发actions的同步如下：

```yml
name: Sync Repo to CODING
on:
  push:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Sync Repo to CODING
      uses: serverlesslife-cn/sync-repo-to-coding@master
      env:
          # 在 GitHub Settings->Secrets 配置 CODING_PRIVATE_KEY
          SSH_PRIVATE_KEY: ${{ secrets.CODING_PRIVATE_KEY }}
      with:
          # 注意替换为你的 GitHub 源仓库地址
          github-repo: "git@github.com:serverlesslife-cn/sync-repo-to-coding.git"
          # 注意替换为你的 CODING 目标仓库地址
          coding-repo: "git@e.coding.net:donghui1/serverlesslife/sync-repo-to-coding.git"
```



# 结束

到这里我们就全部完成了从Github仓库同步到Coding仓库的目的了，这样的操作当然是有着各种的用途，例如当你想要使用别人的一个仓库但你网不好用不了Github,那你就可以这样操作来把仓库更快的clong下来；同时如果你用Github当图床觉得太慢了的话，你也可以尝试用这种方法，将上传到Github的图床实时同步到Coding，从而实现多点备份保存，并且提高图片的访问速度。

本文结束，欢迎留言^ v ^ !
