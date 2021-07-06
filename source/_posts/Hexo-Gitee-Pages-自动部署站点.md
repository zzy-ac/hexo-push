---
uuid: 345a9259-6b43-28c1-3cf7-fe34bce9afa3
title: Hexo Gitee Pages 自动部署站点
date: 2021-02-27 22:42:09
tags: hexo
keywords: 博客
categories: 网页部署
---
本站使用hexo同时上传到gitee和github，但是gitee的pages服务是不能自动部署的，只能手动在网页部署，所以有大佬开发了在Github上使用的动作：<code>gitee-pages-action</code>&#xff08;<a href="https://github.com/yanglbme/gitee-pages-action">点击查看</a>&#xff09;。只要在某个仓库配置好这个动作就能在往这个仓库提交任何内容时自动让Gitee部署Gitee里面指定仓库的内容。

我们按照这个仓库的文档往Hexo站点的<code>source</code>目录添加<code>.github\workflows\sync.yml</code>这个文件&#xff0c;并在这个文件里面配置要使用的Gitee站点仓库和用户名。

```yaml
name: Sync

on:
  push:
    branches:
      - master

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Build Gitee Pages
        uses: yanglbme/gitee-pages-action@master
        with:
          # 注意替换为你的 Gitee 用户名
          gitee-username: zzy-ac
          # 注意在 Settings->Secrets 配置 GITEE_PASSWORD
          gitee-password: ${{ secrets.GITEE_PASSWORD }}
          # 注意替换为你的 Gitee 仓库，仓库名严格区分大小写，请准确填写，否则会出错
          gitee-repo: zzy-ac/zzy-ac
          # 要部署的分支，默认是 master，若是其他分支，则需要指定（指定的分支必须存在）
          branch: master
          https: true
```

经过查阅<a href="https://hexo.io/zh-cn/docs/configuration">Hexo文档</a>发现&#xff0c;Hexo默认会忽略隐藏文件和文件夹&#xff08;包括名称以下划线和 <strong><code>.</code>开头的文件和文件夹</strong>&#xff0c;Hexo的<code>_posts</code>和<code>_data</code>等目录除外&#xff09;。因此需要在后台仓库的<code>_config.yml</code>文件添加这样的配置才能把<code>.github</code>的目录也给带进来。可能已经预留了<code>include</code>属性&#xff0c;建议先搜索这个属性&#xff0c;然后直接往这里面添加。并且由于hexo会默认编译这些文件，因此我们还要忽略它的编译，即在<code>skip_render</code>属性中忽略上述文件。

```yaml
include: 
  - ".github/workflows/sync.yml"
  
skip_render: 
  - ".github/workflows/sync.yml"
```

此外还应设置往远程仓库部署时不要跳过隐藏文件，由于git bash会默认将<code>.</code>开头的文件/文件夹视为隐藏文件，所以要继续在hexo根目录的<code>_config.yml</code>文件添加配置将<code>deploy</code>这个属性中的<code>ignore_hidden</code>设置为<code>false</code>。

```yaml
deploy:
  type: git
  ignore_hidden: false # 添加这个属性值为false
  repo: 
    gitee: git@gitee.com:你的Gitee仓库.git,要使用的分支名
    github: git@github.com:你的Github仓库.git,要使用的分支名
    # 可以先提交Gitee然后再提交Github，也就是把这个Gitee的地址放在前面。这样保证Gitee的站点内容能在Github开始动作之前完成提交。
```

最后千万要注意Github的部署仓库后台的Settings里面也要按照最上面那个仓库说明中那样配置Secrets（<code>GITEE_RSA_PRIVATE_KEY</code>和(<code>GITEE_PASSWORD</code>)的两个密钥。其中：<code>GITEE_RSA_PRIVATE_KEY</code>存放<code>id_rsa</code>私钥；<code>GITEE_PASSWORD</code>存放Gitee帐号的密码），这一步不要忘记了。

按照上述流程配置后，就可以通过github仓库中配置好的动作来自动部署gitee pages了。

（如果遇到需要短信验证码校验。可以关注 Gitee 微信公众号，并绑定 Gitee 帐号，就可以用公众号来接收登录提示了。）
（其他详细操作请查看插件作者的<a href="https://github.com/yanglbme/gitee-pages-action/blob/main/README.md">文档</a>）
