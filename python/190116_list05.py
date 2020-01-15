from random import * # *로 import를 하는 것은 random에 있는 모든 메소드 값을 쓰겠다는 의미
coin = ['head','tail']
dice = [1,2,3,4,5,6]

print(choice(coin)) # 코인 리스트의 원소 중 랜덤
print(choice(dice)) # 다이스 리스트의 원소 중 랜덤

print(randint(1,6)) # 1에서 6사이의 랜덤

import math
print(math.sqrt(25))

