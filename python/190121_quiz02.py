#힌트시스템 추가
#힌트는 답안의 맨 첫글자와 마지막 글자를 제공한다.
#힌트는 2번의 추측기회를 제공한 후 3번째 질문 추측기회 전에
#'힌트를 드릴까요? 라는 질문을 하고 네 입력 시 힌트 제공
import random

wonderland = ['앨리스', '체셔고양이', '시계토끼', '공작부인', '하트여왕', '하트병정', '도로시']
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
        print('정답입니다!')
        break
    else:
        chance = chance - 1
        if chance != 0:
            print('틀렸습니다.',chance,'번 남았습니다.')
        else :
            print('정답은',answer,'입니다')
