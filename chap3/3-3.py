import requests

url = 'http://www.baidu.com/s'
try:
    kv = {'wd':'python'}
    r = requests.get(url, params=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.request.url)
    print(len(r.text))
except:
    print('爬虫失败')