import requests
from bs4 import BeautifulSoup
weapons = []

# 请补充代码，填充weapons
response = requests.get('http://news.4399.com/gonglue/wzlm/daoju/')
response.encoding = 'gb2312'

result = BeautifulSoup(response.text, 'html.parser')

liList = result.select('ul.cf#hreo_list > li')
for item in liList:
  name = item.a.get_text()[1:]
  url = item.img['lz_src']
  weapons.append({'name': name, 'url': url})

print(weapons)
