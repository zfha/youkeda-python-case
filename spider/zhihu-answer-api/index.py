import requests
from bs4 import BeautifulSoup
import re

user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'


def getTotal(id):
  result = requests.get(
      url='https://www.zhihu.com/question/{}'.format(id),
      headers={'User-Agent': user_agent})
  soup = BeautifulSoup(result.text, "html.parser")
  totalDom = soup.find(class_='List-headerText')
  totalText = totalDom.select('span')[0].text
  print(totalText)
  # 解析获取这个数字，并转换成int类型
  total = int(re.split('\s', totalText)[0].replace(',', ''))
  return total


def start(id, offset=0, limit=20):
  print('--------------' + str(offset))
  result = requests.get(
      url='https://www.zhihu.com/api/v4/questions/{}/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit={}&offset={}&platform=desktop&sort_by=default'
      .format(id, 20, offset),
      headers={'User-Agent': user_agent})
  data = result.json()['data']
  for answer in data:
    # 通过字典获取到需要的字段
    text = answer['content']
    author = answer['author']['name']
    print(author)


id = '341554416'
total = getTotal(id)
for offset in range(0, total, 20):
  start(id, offset, 20)