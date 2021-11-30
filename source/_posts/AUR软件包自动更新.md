---
title: AUR软件包自动更新
date: 2021-12-01 00:59:19
tags: AUR
categories: archlinux
---


> 作为一名archlinux用户在日常使用中，维护几个自己的aur包是很正常的现象，其中有一些软件上游是在github上更新的，这时候可能会有些作者定期、频繁的更新上游的软件包，导致某些懒惰的aur维护者懒得跟上作者的节奏手动定期更新，于是-git类型的包就应运而生，这种包才用直接git上游仓库、自动更新版本号并编译的方式来达到自动更新软件的目的。


> 然而编译的过程往往耗费大量时间和计算机性能，对于用户来说可能并不是那么美好，于是一些软件的作者就提供了打包好linux版本的包并将其提供在github仓库的releases，但是很多情况下软件作者要么只提供一个Linux的二进制包、要么只提供一个deb/rpm包，那么就需要我们自己将其打包下来上传到aur仓库来维护arch的版本。那么对于这样的软件我们该怎样实现自动更新呢？本文将以koreader-bin这个包为例子进行介绍

# 编写PKGBUILD

```bash
# Maintainer: zaoqi <zaomir@outlook.com>

pkgname=koreader-bin
pkgver=2021.11
pkgrel=1
pkgdesc="An ebook reader application supporting PDF, DjVu, EPUB, FB2 and many more formats, running on Cervantes, Kindle, Kobo, PocketBook and Android devices"
arch=("x86_64")
url="https://github.com/koreader/koreader/"
license=('AGPL3')
depends=('sdl2' 'fonts-noto-hinted' 'fonts-droid-fallback')
source=(
  "https://github.com/koreader/koreader/releases/download/v${pkgver}/koreader-${pkgver}-amd64.deb")
sha512sums=('811adc6a6fb4fef2ed9bb00ceb41b4c4d0cad9e024cb19021c9fad3d1f7dc06e8105fbb0f8410464576b0436e04e3c60e852db32d8c89bc14adf3a36f93223da')

build() {
  mkdir -p "${srcdir}/dpkgdir"
  tar -xvf data.tar.xz -C "${srcdir}/dpkgdir"
}

package() {
  cp -r "${srcdir}/dpkgdir"/* "${pkgdir}"
}
```
## 调整PKGBUILD版本号有关变量

在平常笔者手动打包时通常只是简单的将资源的直链填入`source`，下次更新时自己手动换上新的直链，但既然要自动更新了当然是让这里能够在不需要修改的情况下只需要修改`PKGBUILD`的`pkgver`变量就可以自动变为新的直链这样更好。由于github releases提供的直链规则比较统一，而这个软件包的做的命名方式也比较规范，因此如上面代码块中那样我们只需要将直链中的版本号`2021.11`替换成`${pkgver}`这个`PKGBUILD`中的版本号就行了。这样我们的修改`PKGBUILD`的时候就只需要修改版本号这一个参数就可以正常的更新软件包了。

## 更新哈希值
然后在arch系统中会根据`PKGBUILD`来将文件进行打包时会对比一下文件的哈希值来保证文件的完整性，因此我们还需要在每次修改完`PKGBUILD`的版本号之后运行`updpkgsums`命令来对`PKGBUILD`文件中的`sha512sums`参数进行自动更新。

那么思路就很清晰了，只要我们可以定时自动检测github上对应的版本号并通过脚本自动填入`PKGBUILD`，然后通过脚本运行`updpkgsums`来更新哈希值，这样处理过之后的`PKGBUILD`就可以自动更新到最新版本了。

于是我们有了如下两个选择
1. 将这个脚本扔到服务器上设置个定时任务
2. 建立一个github actions来自动更新`PKGBUILD`并将其`PUSH`到aur
这里我们详细介绍方法二

# 通过github actions自动更新PKGBUILD并push到aur

## 在actions中自动更新PKGBUILD文件的版本号

fork项目[https://github.com/zzy-ac/auto-aur-update](https://github.com/zzy-ac/auto-aur-update)到你的github仓库中，稍微按照自己软件包最新版本号的获取方式编写一段更新`PKGBUILD`的脚本将其内容写入仓库中`/build-aur-action/entrypoint.sh`脚本中函数`ver`的内容。由于`updpkgsums`会下载一个source包来对比哈希值，但这个包我们是不需要将其push到aur中去的，因此在脚本最后我们应该用`rm`将其删除。

```bash
#!/bin/bash

useradd builder -m
echo "builder ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
chmod -R a+rw .

pacman-key --init
pacman -Sy --noconfirm &&

cd ${INPUT_PKGNAME}

ver=$(curl -s https://api.github.com/repos/koreader/koreader/releases/latest | jq '.tag_name'|tr -d 'v"')
sed -i "s/pkgver=.*/pkgver=$ver/" PKGBUILD
sudo -u builder  updpkgsums

rm koreader-$ver-amd64.deb

echo OK
```

![image-20211201005340911](https://b23.tv/ypbdBxA)

## 用action将上述修改好的PKGBUILD文件push到aur仓库中去

在这里我们使用了[KSXGitHub/github-actions-deploy-aur](https://github.com/KSXGitHub/github-actions-deploy-aur)这一现成的action来完成这一步骤。

![image-20211201005539998](https://b23.tv/mVsLctT)

我们只用参照其编写的README.md中的介绍将对应的参数填入你的`main.yml`中的对应位置就可以了。

![image-20211201005614409](https://b23.tv/8SqJj6o)

![image-20211201005640741](https://b23.tv/WWQ1x8n)

接下来我们只要在仓库中建立一个/数个你要打包的包名命名的文件夹，并将对应的PKGBUILD放入文件夹中就可以了。

![image-20211201005712531](https://b23.tv/jjIIt39)

![image-20211201005737295](https://b23.tv/X9dn6dj)

## 定时运行

最后设置好每天定时更新的时间也就是yml中的`-cron`值就可以实现定时检查并更新aur仓库的软件包了。