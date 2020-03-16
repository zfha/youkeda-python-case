import requests
import re
weapons = []

# 请补充代码，填充weapons
response = requests.get('http://news.4399.com/gonglue/wzlm/daoju/')
response.encoding = 'gb2312'

obj = re.search(r'<ul\s+class="cf"\s+id="hreo_list">([\s\S]*?)<\/ul>',
                response.text)
sections = obj.group(1).split('</li>')  # 根据</li>分割
sections.pop()
for item in sections:

  # 注意这里提取的正则和之前的正则是有区别的
  url = re.search(r'<img.*?src="(.*?)"', item)
  name = re.search(r'<img.*?>(.*?)</a>', item)
  weapons.append({
    'name': name.group(1),
    'url': url.group(1)
  })
print(weapons)
