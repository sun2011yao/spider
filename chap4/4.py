import requests
from bs4 import BeautifulSoup
url = 'https://python123.io/ws/demo.html'
r = requests.get(url)
demo = r.text
soup = BeautifulSoup(demo)
print(soup.prettify())
