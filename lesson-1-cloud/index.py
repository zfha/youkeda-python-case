import jieba
import jieba.analyse
import urllib.request
import re
from wordcloud import WordCloud
from os import path

# 希望生成图云的网页地址
url = 'https://www.zhihu.com/question/291869104/answer/824514120'

font_path = path.join('SimHei.ttf')


def getHTMLContent():
    page = urllib.request.urlopen(url)
    html = page.read().decode('utf-8')
    reg = re.compile('<[^>]*>')
    html = reg.sub('', html)
    return html


def analyseContent(sentence):
    # https://gist.github.com/luw2007/6016931
    keywords = jieba.analyse.extract_tags(
        sentence, topK=100, withWeight=True, allowPOS=('n', 'nr', 'ns'))
    return keywords


def makeImage(text):
    wc = WordCloud(scale=4, font_path=font_path,
                   background_color="white", max_words=500)
    wc.generate_from_frequencies(text)
    # plt.imshow(wc, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()
    wc.to_file(path.join('result.jpg'))

sentence = getHTMLContent()
keywords = analyseContent(sentence)

print(keywords)

dict = {}
for item in keywords:
    dict[item[0]] = item[1]

makeImage(dict)
