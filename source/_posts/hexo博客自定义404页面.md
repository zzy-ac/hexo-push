---
title: hexo博客自定义404页面
date: 2021-03-28 15:01:48
uuid: a462ea67-4801-eec2-4b6e-2f0e991e58ca
tags: hexo
keywords: 博客
categories: 网页部署
---
我们在部署hexo主题时，有时会希望可以制定属于自己的404页面，那么我们该怎么做才能实现用hexo来自定义404页面呢，下面请看教程：
##### · 首先，<code>hexo new page 404</code>创建404页面文件夹 #####
##### · 之后删除<code>404/index.md</code>文件 #####
##### · 下载你想要的404的模板/写一个自己的404页面 #####
##### · 将404.html放置到hexo根目录下的<code>./source/</code>文件夹下 #####
##### · 将404页面的素材放入<code>./source/404/style</code>文件夹内（没有该文件夹就新建一个） #####
##### · 将<code>404.html</code>内指定资源文件夹的位置修改为<code>./source/404/style/</code> #####
##### · 打开hexo根目录下的<code>_config.yml</code>文件，找到<code>skip_render:</code>这一行添加如下代码 #####
```yaml
skip_render: 
  - "404.html"
```
##### · 执行如下指令将修改好的内容推送到gitee/github #####

```bash
hexo clean && hexo g -d
```
##### · github pages可以等待自动部署生效 | gitee pages则需要手动部署或参考<a href="/2021/02/27/hexo-gitee-pages-zi-dong-bu-shu-zhan-dian/">Hexo Gitee Pages 自动部署站点</a>一文进行自动部署 #####

## 综上，我们就完成了hexo自定义404页面的工作 ##
