---
abbrlink: ''
categories:
- - 网页部署
date: '2024-01-22T15:10:40.549685+08:00'
keywords: null
tags:
- 网页部署
title: cf worker反代脚本分享
updated: 2024-1-22T15:19:29.232+8:0
---
反向代理好处多多，既可以帮助中转使得原本无法访问的网站可以直连访问，同时还能实现通过访问自己的自定义域名来访问目标网站从而实现自定义域名的作用。

这里写个一个简短的cf workers可用的反代脚本，在此分享一下，顺便水一篇博客。

```js
addEventListener(
    "fetch",event => {
       let url=new URL(event.request.url);
       url.hostname="example.com";  //你需要反代的域名
       let request=new Request(url,event.request);
       event. respondWith(
         fetch(request)
       )
    }
  )
```

在cf workers中部署好该workers，并将其中的`example.com`修改为你需要反代的域名即可。

利用此脚本可以实现对github、cdn.jsdelivr.net等不能直连访问的域名的访问，同时还可以用于如：glitch、koyeb等不支持/收费自定义域名PaaS平台服务，用于给部署在这些网站上的服务提供自定义的域名。
