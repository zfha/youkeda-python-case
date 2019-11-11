# -*- coding: UTF-8 -*-
import http.client
import urllib.parse
import json

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest

appKey = 'LTAIe1jCeoKG202P'
appSecret = 'YaFu3MRSpHmCDbwKPOYaZSz2MUAQMR'
# 创建AcsClient实例
client = AcsClient(
    appKey,
    appSecret,
    "cn-shanghai"
)
# 创建request，并设置参数
request = CommonRequest()
request.set_method('POST')
request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
request.set_version('2019-02-28')
request.set_action_name('CreateToken')
response = client.do_action_with_exception(request)
token = json.loads(response.decode())['Token']['Id']

sampleRate = 16000
format = 'mp3'
audioSaveFile = 'test.mp3'

speechAppKey = 'DrmRWP5s54SAD26t'


def speechRequest(text, voice, volume, speechRate, pitchRate):
    host = 'nls-gateway.cn-shanghai.aliyuncs.com'
    url = 'https://' + host + '/stream/v1/tts'
    # 设置URL请求参数
    url = url + '?appkey=' + speechAppKey
    url = url + '&token=' + token
    url = url + '&text=' + text
    url = url + '&format=' + format
    url = url + '&sample_rate=' + str(sampleRate)
    # voice 发音人，可选，默认是xiaoyun
    url = url + '&voice=' + voice
    # volume 音量，范围是0~100，可选，默认50
    url = url + '&volume=' + str(volume)
    # speech_rate 语速，范围是-500~500，可选，默认是0
    url = url + '&speech_rate=' + str(speechRate)
    # pitch_rate 语调，范围是-500~500，可选，默认是0
    url = url + '&pitch_rate=' + str(pitchRate)
    print(url)
    conn = http.client.HTTPSConnection(host)
    conn.request(method='GET', url=url)
    # 处理服务端返回的响应
    response = conn.getresponse()
    print('Response status and response reason:')
    print(response.status, response.reason)
    contentType = response.getheader('Content-Type')
    print(contentType)
    body = response.read()
    if 'audio/mpeg' == contentType:
        with open(audioSaveFile, mode='wb') as f:
            f.write(body)
        print('The GET request succeed!')
    else:
        print('The GET request failed: ' + str(body))
    conn.close()


def urlEncode(text):
    temp = text

    # 特殊符号替换
    temp = urllib.parse.quote_plus(temp)
    temp = temp.replace("+", "%20")
    temp = temp.replace("*", "%2A")
    temp = temp.replace("%7E", "~")
    return temp


# 需要转换的文本
text = '今天是周一，天气挺好的。'
# 采用RFC 3986规范进行urlEncode编码
textUrlEncode = urlEncode(text)

# voice 发音人，可选，默认是xiaoyun
voice = 'xiaoyun'
# volume 音量，范围是0~100，可选，默认50
volume = 50
# speech_rate 语速，范围是-500~500，可选，默认是0
speechRate = 0
# pitch_rate 语调，范围是-500~500，可选，默认是0
pitchRate = 0

# GET 请求方式
speechRequest(textUrlEncode, voice, volume, speechRate, pitchRate)
