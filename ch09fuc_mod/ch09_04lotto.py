import random


# 함수 선언 부분
def get_number():
    return random.randrange(1, 46)


# 전역 변수
lotto = []

# 메인코드
print("로또 추첨을 시작")

while len(lotto) < 6:
    lotto.append(get_number())
    setLotto = list(set(lotto))

'''
while True:
    lotto.append(get_number())
    setLotto = list(set(lotto))
    if len(setLotto) >= 6:
        break
'''

print("추첨된 로또번호 -- > ", sorted(setLotto))

