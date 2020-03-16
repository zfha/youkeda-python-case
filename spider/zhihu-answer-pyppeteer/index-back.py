import requests
from bs4 import BeautifulSoup
import re
import xlsxwriter
from pyppeteer import launch
import asyncio

user_agent='Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
# result = requests.get(url='https://www.zhihu.com/question/341554416', headers={'User-Agent': user_agent})


def patch_pyppeteer():
    import pyppeteer.connection
    original_method = pyppeteer.connection.websockets.client.connect

    def new_method(*args, **kwargs):
        kwargs['ping_interval'] = None
        kwargs['ping_timeout'] = None
        return original_method(*args, **kwargs)

    pyppeteer.connection.websockets.client.connect = new_method


async def spider():
    browser = await launch()
    page = await browser.newPage()
    await page.goto('https://www.zhihu.com/question/341554416')
    answers = await page.querySelectorAll('.List-item')
    lastNum = len(answers)
    # while True:
    #     height = await page.evaluate("() => document.body.scrollHeight")
    #     cur_dist = 0
    #     while True:
    #         if cur_dist < height:
    #             print(cur_dist)
    #             await page.evaluate("window.scrollBy(0, 2000);")
    #             await asyncio.sleep(0.1)
    #             cur_dist += 2000
    #         else:
    #             break

    #     await asyncio.sleep(2)
    #     answers = await page.querySelectorAll('.List-item')
    #     print('lastNum' + str(lastNum) + '---- now' + str(len(answers)))
    #     if lastNum == len(answers):
    #         break
    #     else:
    #         lastNum = len(answers)


    # for answer in answers:
    #     nameDom = await answer.querySelector('.AuthorInfo-name a')
    #     contentDom = await answer.querySelector('.RichText')
    #     name = await page.evaluate('(element) => element.textContent', nameDom)
    #     content = await page.evaluate('(element) => element.innerHTML',contentDom)
    #     print(name + ':' + content)

patch_pyppeteer()
asyncio.get_event_loop().run_until_complete(spider())


# soup = BeautifulSoup(result.text, "html.parser")
# totalDom = soup.find(class_='List-headerText')
# totalText = totalDom.select('span')[0].text
# total = int(re.split('\s', totalText)[0].replace(',', ''))
#
# workbook = xlsxwriter.Workbook('answer.xlsx')
# worksheet = workbook.add_worksheet()
#
# for offset in range(0, total, 20):
#     print('------------offset: ' + str(offset))
#     result = requests.get(url='https://www.zhihu.com/api/v4/questions/341554416/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%2Cis_recognized%2Cpaid_info%2Cpaid_info_content%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%2A%5D.topics&limit={}&offset={}&platform=desktop&sort_by=default'.format(20, offset), headers={'User-Agent': user_agent})
#     data = result.json()['data']
#     index = offset
#     for answer in data:
#         print('index: ' + str(index))
#         text = answer['content']
#         author = answer['author']['name']
#         worksheet.write(index, 0, author)
#         worksheet.write(index, 1, text)
#         index += 1
#
# workbook.close()


