from bs4 import BeautifulSoup

html = """
<html>
  <head>
    <title>优课达</title>
  </head>
  <body>
    <a href="https://www.youkeda.com" alt="学得比别人好一点">优课达</a>
    <ul>
      <li><a href="https://www.youkeda.com">问吧</a></li>
      <li class="info"><a href="https://www.youkeda.com/academy/java">研发学院</a></li>
      <li class="info"><a href="https://www.youkeda.com/academy/python/P2">Python学院</a></li>
      <li class="info"><a class="download" href="https://www.youkeda.com/app">APP下载</a></li>
    </ul>
  </body>
</html>
"""
result = BeautifulSoup(html, 'html.parser')

# # 查询所有的a标签
# aList1 = result.find_all('a')
# print(aList1)
# print('-------------')

# # 查询所有class为info的li标签
# liList = result.find_all('li', 'info')
# print(liList)
# print('-------------')

# # 查询所有的href为https://www.youkeda.com的a标签
# aList2 = result.find_all('a', href='https://www.youkeda.com')
# print(aList2)
# print('-------------')


# # 来一个复杂的查询，查询所有的class为info的li标签，并且查询li标签内部class为download的a元素的文字内容
# liList2 = result.find_all('li', "info")
# for li in liList2:
#   temp = li.find_all('a', 'download')
#   if len(temp) > 0:
#     print(temp[0].get_text())
#     print('-------------')


# liList = result.find_all('li', "info")
# for li in liList:
#   print('{}-{}'.format(li.a.get_text(), li.a['href']))

aList = result.select('ul > li.info > a')
for item in aList:
  print('{}-{}'.format(item.get_text(), item['href']))