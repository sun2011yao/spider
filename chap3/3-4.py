import requests
import os
url = 'http://image.ngchina.com.cn/2018/0307/20180307050221166.jpg'
root = 'D://pics//'
path = root + url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        r.raise_for_status()
        with open(path, 'wb') as f:
            f.write(r.content)
            print('文件保存成功')
    else:
        print('文件已存在！！！')
except:
    print('爬虫失败')