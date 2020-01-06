import random

wonderland = ['앨리스', '체셔고양이', '시계토끼', '공작부인', '하트여왕', '하트병정', '도로시']
answer = random.choice(wonderland)
print(answer)
print('이상한 나라에 오신 것을 환영합니다!')

chance = 5


for s in range(chance):
    guess = input('등장인물을 맞춰주세요 : ')
    if guess == answer:
        print('정답입니다!')
        break
    else:
        chance = chance - 1
        if chance != 0:
            print('틀렸습니다.',chance,'번 남았습니다.')
            if chance == 3 :
                    print('힌트! 앞글자와 맨뒷글자 : '+answer[0]+answer[-1])  
        else :
            print('정답은',answer,'입니다')
