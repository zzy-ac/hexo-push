---
title: 利用github api实现免费图床的python脚本
date: 2022-03-09 21:01:06
tags: 网页部署
keywords:
categories: 图床建设
---

> 本文目标：之前曾经写过一篇[白嫖bilibili图床](https://blog.zzy-ac.top/2021/11/27/bai-piao-bilibi-tu-chuang/)用于白嫖B站的图片外链作为图床使用，然而很可惜，逼站的图床如今已经失效了（逼站修复了这一bug）故而只能重新找寻其他图床了。
>
> 在上一篇文章中我们提到用github action将仓库同步到coding的方法，故而本文的图床也将用到前文内容，利用coding作为图床的空间，来实现免费图床。
>
> 目标：一如之前的bilibili一文，依然是需要在typora中支持从剪贴板粘贴进编辑器自动上传到图床。

# 一、直接上脚本

在本文中，博主将脚本命名为pic2gh.py,各位可以自凭喜好随意命名

```python
import requests
import base64
import json
import uuid
import datetime
import os
import sys

ext = ""
os.system('cp "%s" /path/pic2gh_cache' % sys.argv[1])
# 从文件夹下 读取文件
def read_dir():
    global extp y t h o n
    path = "/path/pic2gh_cache"  # 指定的文件夹目录(自己随意) todo
    files = os.listdir(path)# 得到文件夹下的所有文件名称

    for file in files:  # 遍历文件夹
        if not os.path.isdir(file):  # 判断是否是文件夹，不是文件夹才打开
            ext = os.path.splitext(file)[1]
            with open(path + "/" + file, 'rb') as f: # rb 二进制 读取
                fdata_tmp = file_base64(f.read())
                f.close()
                return fdata_tmp # 只取第一个 文件，太懒了，就默认第一个



# 将文件转换为base64编码，github上传文件必须将文件以base64格式上传
def file_base64(data):
    data_b64 = base64.b64encode(data).decode()
    return data_b64


# 上传文件
def upload_file(file_data):
    global ext
    file_name = sys.argv[1].split('/')[-1]  # 文件名 随机生成
    # token = "[token]" todo
    # url = "https://api.github.com/repos/[user]/[repo]/contents/[path]/"+file_name  # 用户名、库名、路径
    # headers = {"Authorization": "token " + token}
    token = "ghp_ydDXXXXXXXXXXXXXXXXXRW2" ## 自行去github生成token，不懂得文章最好会写
    curr_time = datetime.datetime.now()
    path = curr_time.strftime("/path_at_github") #这里的路径为git仓库中文件所在路径
    url = "https://api.github.com/repos/[user]/[repo]/contents/" + path + "/" + file_name  # 用户名、库名、路径
    headers = {"Authorization": "token " + token} # github token 的规则 在2021-9-29 变调了，注意官方文档的说明哦
    content = file_data
    data = {
        "message": "tc upload pictures",
        "content": content
    }
    data = json.dumps(data)
    req = requests.put(url=url, data=data, headers=headers)
    req.encoding = "utf-8"
    re_data = json.loads(req.text)
    print("https://[user_name].coding.net/t/[user]/p/[project]/d/[repo]/git/raw/main/" + path + "/" + file_name)
    # ！======= 千万注意路径，别写错了  #这里的路径采用了coding仓库的对应目录，请先参照前文配置github与coding的实时同步。


if __name__ == '__main__':
    # 从文件夹 读取文件
    fdata = read_dir()
    
    upload_file(fdata)
os.system('rm -rf /path/pic2gh_cache/*')
```

# 目标实现：

## 脚本的直接使用

在终端使用`python 3 /path/to/pic2gh.py /path/to/picture/whitch/need/upload`即可将所需上传的图片上传到github，并自动同步到coding,获取到coding的图片外链了（由于github actions执行需要时间，这个外链可能将在1～2分钟之后才能生效）。

##  typora中启用脚本

将`python3 /path/to/pic2gh.py`复制到Typora的`偏好设置`→`图象`→`上传服务设定`的`Custom Command`选项的命令一行中去。

# 成果检验

![typora上传效果](https://zzy-ac1.coding.net/t/zzy-ac1/p/zzy-ac/d/My-Selves-Cloud/git/raw/main/images/2022/03/09/Peek_2022-03-09_21-40.gif)
