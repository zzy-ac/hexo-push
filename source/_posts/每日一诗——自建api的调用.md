---
title: 每日一诗——自建api的调用
date: 2021-04-04 12:16:04
uuid: a7c6abd6-a65b-dced-5369-09f53e2ffbb7
tags: api
keywords:
categories: api
---
---
一言——是一个在全网范围获得广泛应用的api,可以为我们提供一句随机的直戳心灵的话语。
而有时我们会需要创建一个类似一言这种形式的完全自定义内容的api该怎么办呢？
这样其实不难，我们可以很轻松的通过php实现我们想要的目的。
首先在网站根目录下创建一个文件夹文件名就是你希望访问的地址的路径名，在这里我使用<code>/poem</code>来表示
之后在文件夹内创建一个<code>index.php</code>文件，在其中写入如下内容
```php
<?php
// 获取句子文件的绝对路径
// 如果你介意别人可能会拖走这个文本，可以把文件名自定义一下，或者通过Nginx禁止拉取也行。
$path = dirname(__FILE__);
$file = file($path."/poem.txt");
 
# 随机读取一行
$arr  = mt_rand( 0, count( $file ) - 1 );
$content  = trim($file[$arr]);
 
# 编码判断，用于输出相应的响应头部编码
if (isset($_GET['charset']) && !empty($_GET['charset'])) {
    $charset = $_GET['charset'];
    if (strcasecmp($charset,"gbk") == 0 ) {
        $content = mb_convert_encoding($content,'gbk', 'utf-8');
    }
} else {
    $charset = 'utf-8';
}
header("Content-Type: text/html; charset=$charset");
 
# 格式化判断，输出js或纯文本
if ($_GET['format'] === 'js') {
    echo "function poem(){document.write('" . $content ."');}";
} else {
    echo $content;
}
```
（其中的<code>poem</code>字样可以替换为你需要的名称，只需将对应的文件名称修改即可）
接着，在index.php同一目录下创建一个名为poem.txt的文本文件（如上文所述，可以替换为其他文件名，只需修改相应的参数即可）并将需要展示的语句逐行放进这个txt
例如：
```code
爆竹声中一岁除，春风送暖入屠苏。
小楼一夜听春雨，深巷明朝卖杏花。
惆怅东栏一株雪，人生看得几清明。
更深月夜半人家，北斗阑干南斗斜
春水碧于天，画船听雨眠。
春风又绿江南岸，明月何时照我还。
等闲识得东风面，万紫千红总是春。

..........

```
之后访问<http://你的域名/poem/>就可以查看api效果了

那么该如何将api调用到你需要的网站中呢？
只需在网站文件中你需要的地方添加如下代码，即可
```html
<script type="text/javascript" src="http://你的域名/poem/?format=js&charset=utf-8"></script>
<div id="poem"><script>poem()</script></div>
```

以上就是完整的自建类一言api并调用之的完整教程
欢迎使用博主的古诗词api
```
 <script type="text/javascript" src="https://api.zzy-ac.top/poem/?format=js&charset=utf-8"></script>
 <div id="poem"><script>poem()</script></div>
```
<h3>效果如下：</h3>
    <h4><font color="blue"><script type="text/javascript" src="https://api.zzy-ac.top/poem/?format=js&charset=utf-8"></script><div id="poem"><script>poem()</script></div></font></h4>


