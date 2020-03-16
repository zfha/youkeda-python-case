import requests
from bs4 import BeautifulSoup

user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
result = requests.get(url='https://movie.douban.com/subject/30176393/comments?start=40&limit=20&sort=new_score&status=P', headers={'User-Agent': user_agent})
print(result.text)
# soup = BeautifulSoup(result.text, "html.parser")
# screenMove = soup.find(class_='screening-bd')
