# 프로그램과 답안지 분리
# 파일 입출력 적용

import random

wd = open('wonderland.txt','r')
wonder = wd.readlines()
wonderland = []
for k in wonder:
    wonderland.append(k.strip('\n'))
wd.close()

answer = random.choice(wonderland)
hint = answer[0] + answer[-1]
print(answer)
print('이상한 나라에 오신 것을 환영합니다!')

chance = 5
hint_check = chance - 2

for s in range(chance): #chance에 저장된 수만큼 반복
    if chance == hint_check :
        ok = input("힌트를 드릴까요? ('네' 입력 시 힌트제공)")
        if ok == '네':
            print('힌트! 앞글자와 맨뒷글자 : '+hint)
    guess = input('등장인물을 맞춰주세요 : ')
    if guess == answer:
        print('정답입니다!',str(chance)+'점 입니다')
        break
    else:
        chance = chance - 1
        if chance != 0:
            print('틀렸습니다.',chance,'번 남았습니다.')
        else :
            print('정답은',answer,'입니다. '+str(chance)+'점 입니다')
