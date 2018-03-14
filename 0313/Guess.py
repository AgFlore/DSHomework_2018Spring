import random
while True:
    answer = random.randint(1,100)
    inputnumber = int(input('请输入一个正整数……'))
    if inputnumber==100:
        print('好不陪我玩就不陪我玩吧告辞')
        break
    elif inputnumber < answer:
        print('猜小啦！')
        continue
    elif inputnumber > answer:
        print('猜大啦！')
        continue
    elif inputnumber == answer:
        print('猜中啦！')
        continue
    else:
        print('?????')
        continue
    pass
