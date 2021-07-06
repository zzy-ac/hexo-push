---
uuid: c4c5665b-90a3-9a4f-d231-870230614178
title: SDDM汉化
date: 2020-12-18 17:29:07
tags: linux
categories: archlinux
---
用文本编辑器打开/usr/lib/systemd/system/sddm.service
在[Service]下添加Environment=LANG=zh_CN.UTF-8
