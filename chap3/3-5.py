import requests
url = 'http://m.ip138.com/ip.asp?ip='
ip = input('Please enter your ip address: ')
try:
     r = requests.get(url + ip)
     r.raise_for_status()
     r.encoding = r.apparent_encoding
     print(r.text[-500:])
except:
    print('爬虫失败')