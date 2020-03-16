import requests
from bs4 import BeautifulSoup

user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
result = requests.get(url='https://www.zhihu.com/topic/19555033/hot', headers={'User-Agent': user_agent})
print(result.text)

