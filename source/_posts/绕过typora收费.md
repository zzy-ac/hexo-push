---
title: 绕过typora收费
date: 2021-12-10 17:47:07
tags:
keywords:
categories:
---



> 近日，知名markdown所见即所得式编辑工具typora告别了测试阶段进入1.0正式版本，开启了收费使用的新征程。对于高达$14.99美元(￥89)的价格，博主只能表示敬而远之，毕竟typora虽然强大，但并不是博主的唯一选择，使用其他的markdown编辑器无非也就是多进行一两个步骤而已，故而一直使用的没有进行付费。

那么想要继续免费使用typora有什么办法呢？

1. 使用0.11.18的旧版本。
2. 如果你使用的是各大linux发行版的话，typora支持无限期的免费试用，但会不定期的弹出付费窗口。
3. 作为一款electron程序，当然是把它解码自行破解激活。

前两种显而易见没有太多好介绍的，在这里略微介绍一下第三种方案。

# 解压处理typora的app.asar文件

`app.asar`文件是一众electron程序默认的主程序文件，通常情况下我们可以正常的用electron来启动这一文件，但是typora可能是处于软件安全考虑对这一文件进行了加密处理。

但是在某[Mas0nShi](https://github.com/Mas0nShi)大佬的努力下，这一加密已经得到了破解，我们可以通过大佬的这一[项目](https://github.com/Mas0nShi/typoraCracker)方便的对`app.asar`文件进行修改。

## 1.克隆typoraCracker项目

```bash
git clone https://github.com/Mas0nShi/typoraCracker.git
```

## 2.在克隆下来的仓库打开终端

按照项目readme.md文件的介绍对typora的app.asar文件进行处理。

## 3.将处理好的app.asar文件替换掉原文件

输入邮箱和获得的序列号。

![image-20211210181218925](https://b23.tv/nsRNyY5)

至此就可以成功绕过typora的付费过程了
