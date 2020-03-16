import requests
import re

# from bs4 import BeautifulSoup

response = requests.get('http://news.4399.com/gonglue/wzlm/yingxiong/')
response.encoding = 'gb2312'
# soup = BeautifulSoup(result.text, "html.parser")
# heroList = soup.find(id='hreo_list')
# for hero in heroList:
#     img = hero.find('img')
#     span = hero.find('span')
#     if img == -1:
#         continue
#     imgResult = requests.get(img.attrs['lz_src'])
#     with open('imgs/{}.jpg'.format(span.text), 'wb') as file:
#         print(span.text + ' download complete！')
#         file.write(imgResult.content)

obj = re.search(r'<ul\sclass="rolelist\scf"\sid="hreo_list">([\s\S]*?)<\/ul>',
                response.text)
heros = obj.group(1).split('</li>')  # 根据</li>分割
heros.pop()
for hero in heros:
  banner = re.search(r'\slz_src="(.*?)"\s', hero)
  name = re.search(r'<span>(.*?)</span>', hero)
    # 我们不需要先存储results了，在这里直接下载即可
  imgResult = requests.get(banner.group(1))
  with open('imgs/{}.jpg'.format(name.group(1)), 'wb') as file:
    print(name.group(1) + ' 下载完成！')
    file.write(imgResult.content)

