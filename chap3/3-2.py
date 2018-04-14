import requests

url = 'https://www.amazon.cn/dp/B07896QS5D/ref=cngwdyfloorv2_recs_0?pf_rd_p=7149a3bb-2ee6-4f99-92eb-d87852365f8c&pf_rd_s=desktop-2&pf_rd_t=36701&pf_rd_i=desktop&pf_rd_m=A1AJ19PSB66TGU&pf_rd_r=CP5129Q8E30K90CDZNY6&pf_rd_r=CP5129Q8E30K90CDZNY6&pf_rd_p=7149a3bb-2ee6-4f99-92eb-d87852365f8c'
try:
    kv = {'user-agent':'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print('爬虫失败')