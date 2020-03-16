import requests
from bs4 import BeautifulSoup
import re


def replaceContent(content):
  content = re.sub(r'\s', '', content)
  return content


def startSpider(url):
  user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
  response = requests.get(url, headers={'User-Agent': user_agent})

  # 同样我们可以根据 meta charset 获取到页面的编码方式
  response.encoding = 'utf-8'

  result = BeautifulSoup(response.text, 'html.parser')
  books = result.select('#content > div > div.article > div > table')
  for book in books:
    nameDoms = book.select('tr > td:nth-child(2) > div.pl2 > a')
    name = ''
    if len(nameDoms) > 0:
      name = nameDoms[0].get_text()

    rawNameDoms = book.select('tr > td:nth-child(2) > div.pl2 > span')
    rawName = ''
    if len(rawNameDoms) > 0:
      rawName = rawNameDoms[0].get_text()

    authorDoms = book.select('tr > td:nth-child(2) > p.pl')
    author = ''
    if len(authorDoms) > 0:
      author = authorDoms[0].get_text()
      author = author.split('/')[0]

    print('{} {} {}'.format(
        replaceContent(name), replaceContent(rawName), replaceContent(author)))


for i in range(10):
  startSpider('https://book.douban.com/top250?start={}'.format(i * 25))
