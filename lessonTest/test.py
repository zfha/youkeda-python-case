# 定义一个combat的方法
def combat(aex, arthur):
    while arthur > 0 and aex > 0:
        if arthur > 650:
            arthur -= 450
            print('斧王对亚瑟造成了' + str(450) + '点伤害，亚瑟剩余生命值为' + str(arthur) + '点')
        else:
            arthur -= 650
            print('斧王对亚瑟造成了' + str(arthur + 650) + '点伤害，亚瑟被击败')
            break

        harm = int(aex * 0.2) + 300
        aex -= harm
        if aex > 0:
            print('亚瑟对斧王造成了' + str(harm) + '点伤害，斧王剩余生命值为' + str(aex) + '点')
        else:
            print('亚瑟对斧王造成了' + str(harm + aex) + '点伤害，斧王被击败')
            break


print('第一场战斗---------------')
combat(5000, 5000)
print('第二场战斗---------------')
combat(5000, 3000)
