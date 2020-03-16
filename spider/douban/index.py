import requests
from bs4 import BeautifulSoup

user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
result = requests.get(url='https://movie.douban.com/', headers={'User-Agent': user_agent})
soup = BeautifulSoup(result.text, "html.parser")
movies = screenMove.select('#content > div > div.article > div.gaia.gaia-lite.gaia-movie.slide-mode > div.list-wp > div > div.slide-container a')
print(len(movies))
# for move in movies:
#     posterDomList = move.select('li.poster img')
#     titleDomList = move.select('li.title a')
#     if posterDomList and len(posterDomList) > 0:
#         poster = posterDomList[0].attrs['src']
#         title = titleDomList[0].text
#         print(title, end="")
#         print(poster)
#         imgResult = requests.get(poster)
#         with open('imgs/{}.jpg'.format(title), 'wb') as file:
#             print(title + ' download complete！')
#             file.write(imgResult.content)

