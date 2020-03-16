import requests
import os

result = requests.get('https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js')
data = result.json()

for hero in data['hero']:
    name = hero['name']
    print('处理英雄：' + name)
    avatar = 'https://game.gtimg.cn/images/lol/act/img/champion/{}.png'.format(hero['alias'])
    folder = 'imgs/{}'.format(name)
    os.makedirs(folder)

    avatarResult = requests.get(avatar)
    with open('{}/{}.png'.format(folder, name), 'wb') as file:
        print(name + ' avatar download complete！')
        file.write(avatarResult.content)

    selectAudioResult = requests.get(hero['selectAudio'])
    with open('{}/{}.ogg'.format(folder, 'select'), 'wb') as file:
        print(name + ' selectAudio download complete！')
        file.write(avatarResult.content)

    banAudioResult = requests.get(hero['banAudio'])
    with open('{}/{}.ogg'.format(folder, 'ban'), 'wb') as file:
        print(name + ' banAudio download complete！')
        file.write(avatarResult.content)
