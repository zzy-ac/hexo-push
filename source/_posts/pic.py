import os
import re
import requests

file_extension = [
    '.md',
    '.yml',
    '.html'
]

pic_urls = []
_files = []

# 修改后的正则表达式，用于匹配 Markdown 图片链接
pattern = r'!\[.*?\]\((.*?)\)'

def upload(url):
    # API 相关信息
    api_url = 'https://lsky.m-l.cc/api/v1/upload'
    headers = {
        'Authorization': 'Bearer 5|SYLCnLZgsSdXAZQlPQ8mq0nF2vxdyRtOSXbxqlpq',
    }

    # 第一步：下载图片
    response = requests.get(url)
    if response.status_code == 200:
        # 将图片内容保存到内存中
        image_data = response.content

        # 第二步：上传图片
        files = {
            'file': ('image.webp', image_data),  # 使用内存中的图片数据
            'strategy_id': (None, '6'),  # 传递其他表单数据
        }
        upload_response = requests.post(api_url, headers=headers, files=files)

        # 处理上传响应
        if upload_response.status_code == 200:
            upload_result = upload_response.json()
            return upload_result['data']['links']['url']  # 返回链接
        else:
            print(f"上传失败: {upload_response.status_code}, {upload_response.text}")
            return None
    else:
        print(f"下载失败: {response.status_code}, {response.text}")
        return None



for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(tuple(file_extension)):
            file_name = os.path.join(root, file)
            with open(file_name, 'r') as f:
                content = f.read()
            urls = re.findall(pattern, content)
            if urls:
                pic_urls.extend(urls)
                _files.append(file_name)

pic_urls = list(set(pic_urls))
print("共找到图片：", len(pic_urls))

url_dict = {}

for i, u in enumerate(pic_urls, start=1):
    try:
        new_u = upload(u)
    except Exception:
        try:
            new_u = upload(u)
        except Exception:
            try:
                new_u = upload(u)
            except Exception as e:
                new_u = u
                print(f"{u} 无法上传：{e}")
    url_dict[u] = new_u
    print(f"第 {i} 个， 共 {len(pic_urls)} 个")

for file in _files:
    with open(file, 'r') as f:
        content = f.read()
    for k, v in url_dict.items():
        content = content.replace(k, v)
    with open(file, 'w') as f:
        f.write(content)
    print("完成替换：", file)

