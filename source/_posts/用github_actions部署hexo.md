---
title: 用github_actions部署hexo
date: 2021-07-06 15:30:49
uuid: 35dff528-822f-e875-fd06-7c2741d92b63
tags: hexo
categories: 网页部署
---
今天博主突发奇想决定用github_actions服务在线编辑并部署hexo，从而实现类似动态博客的后台的效果。
那么如何来进行部署呢？
首先，创建一个仓库例如<code>hexo-push</code>，新建文件夹<code>.github/workflows</code>在其中新建文件<code>main.yml</code>
在文件中写入如下内容
```yml
name: Hexo Deploy

on:
  push:
    branches:
      - hexo

jobs:
  build:
    runs-on: ubuntu-18.04
    if: github.event.repository.owner.id == github.event.sender.id

    steps:
      - name: Checkout source
        uses: actions/checkout@v2
        with:
          ref: hexo

      - name: Setup Node.js
        uses: actions/setup-node@v1
        with:
          node-version: '14.x'

      - name: Setup Hexo
        env:
          ACTION_DEPLOY_KEY: ${{ secrets.HEXO_DEPLOY_KEY }}
        run: |
          mkdir -p ~/.ssh/
          echo "$ACTION_DEPLOY_KEY" > ~/.ssh/id_rsa
          chmod 700 ~/.ssh
          chmod 600 ~/.ssh/id_rsa
          ssh-keyscan github.com >> ~/.ssh/known_hosts
          git config --global user.email "xxxxx@xxx.xx"
          git config --global user.name "xxxxxx"
          npm install hexo-cli yarn -g
          yarn
      - name: Deploy
        run: |
          hexo clean
          hexo d
```
接着，在hexo-push库的setting中添加HEXO_DEPLOY_KEY秘钥为你的本地私钥
之后，将hexo-push仓库，clone到你的本地
然后在你的hexo目录执行<code>hexo clean</code>清除不必要的文件
将除<code>.deploy_git、.git</code>之外的其他文件/文件夹复制到hexo-push的本地仓库并上传
然后就可以通过在hexo-push仓库中发布新的md文件来达到更新博客的目的了！
