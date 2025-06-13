---
abbrlink: ''
categories:
- - 图床建设
date: '2024-05-03T13:23:21.494193+08:00'
keywords: null
tags:
- 网页部署
title: Qexo使用Lsky-Pro兰空图床api
updated: '2024-08-12T16:44:51.784+08:00'
---
> 最近才终于整明白了在qexo使用lsky的api的方法，在此简单记录一下

# 获取token

搭建好lsky后在控制面板里可以看到接口页面，里面包含了api的各种使用方法。和最为关键的接口URL——`https://example.com/api/v1`

那么用curl命令获取token，命令如下：

```bash
curl -X POST https://example.com/api/v1/tokens \
-H "Content-Type: application/json" \
-d '{
  "email": "your_email@example.com",
  "password": "your_password"
}'
```

使用后获得输出如下：

```bash
{"status":true,"message":"success","data":{"token":"1|1bJbwlqBfnggmOMEZqXT5XusaIwqiZjCDs7r1Ob5"}}
```

当前版本的lsky-pro接口采用 「HTTP 基本验证」的方式验证授权，获取到 token 后，通过设置请求 header 标头来验证请求(Bearer Token)，例如：

`"Authorization": "Bearer 1|1bJbwlqBfnggmOMEZqXT5XusaIwqiZjCDs7r1Ob5"`

（填你自己获取到的token,我这只是放的官方的示例）

# 编辑qexo图床配置

如图，将lsky接口文档中的各项信息依次填入即可。

![https://img.dmnb.cf/2024-08-12-66b9affb8093f.webp](https://img.dmnb.cf/2024-08-12-66b9affb8093f.webp)

需注意，自定义请求头和自定义请求主体中的空格，复制粘贴的可能存在错误，会变成非普通空格的空白符号。这里建议手打。


![https://img.dmnb.cf/2024-08-12-66b9acf93b703.webp](https://img.dmnb.cf/2024-08-12-66b9acf93b703.webp)

在自定义请求主题处填入你想使用的储存桶的id（如果只有一个可以不用管）

自定义请求头只需要token一项就可以了，即内容为：`{"Authorization":"Bearer Bearer 1|1bJbwlqBfnggmOMEZqXT5XusaIwqiZjCDs7r1Ob5"}`（填你自己获取到的token,我这只是放的官方的示例）

# 完成

填写完成后提交，就完成了qexo中兰空图床的配置。可自行去图片页面进行测试。

![https://img.dmnb.cf/2024-08-12-66b9ad2f8e9dd.webp](https://img.dmnb.cf/2024-08-12-66b9ad2f8e9dd.webp)

如图显示上传成功出现预览图和链接，则表明配置无误，直接开始快乐的写文章插图片去吧！
