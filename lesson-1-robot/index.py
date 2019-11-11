import json
import requests

city = '杭州'
province = '浙江'
street = '文一西路'
text = '今天天气如何？'

url = "http://openapi.tuling123.com/openapi/api/v2"
values = {
    "reqType": 0,
    "perception": {
        "inputText": {
            "text": text
        },
        "inputImage": {
            "url": "imageUrl"
        },
        "selfInfo": {
            "location": {
                "city": city,
                "province": province,
                "street": street
            }
        }
    },
    "userInfo": {
        "apiKey": "854c4abd263c4154b15daa257861f84e",
        "userId": "youkeda"
    }
}

response = requests.post(url, data=json.dumps(values))
response.encoding = 'utf-8'
result = response.json()
answer = result['results'][0]['values']['text']
print(answer)

