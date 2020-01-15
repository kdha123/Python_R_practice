set1 = {1, 2, 3, 3, 3, 4}
# 중복된 키는 하나만 남음
print(set1, type(set1))

# list -> set
salesList = ['삼김', '바나나', '도시락', '삼김', '도시락', '바나나']
print(salesList)
# print(set(salesList))
# print(list(set(salesList)))

# 판매된 상품과 수량을 출력 중복이 되면 안된다.
# print("삼김 : ", salesList.count('삼김'))
product = list(set(salesList))
print(product)
for k in product:
    print(k, ":", salesList.count(k))

mySet1 = {1, 2, 3, 4, 5}
mySet2 = {4, 5, 6, 7}
# 교집합, 합집합, 차집합, 대칭 차집합(합집합 - 교집합)
print(mySet1 & mySet2)
print(mySet1 | mySet2)
print(mySet1 - mySet2)
print(mySet2 - mySet1)
print(mySet1 ^ mySet2)

# 1 ~ 100까지의 데이터로 list 를 만들어보세요.
# 1번
num = [1, 2, 3, 4, 5]
print(num)

# 2번
num1 = []
for i in range(1, 101):
    num1.append(i)
print("num1 : ", num1)

# 3번 컴프리헨션
num2 = [num for num in range(1, 6)]
print(num2)
# 1 ~ 10사이 3의 배수로 리스트 만들기 -> [3,6,9]
# for i in range(1, 10 + 1):
#     if i % 3 == 0:
#         num3.append(i)
# 밑의 한줄로 만들 수 있다.
num3 = [num for num in range(1, 11) if num % 3 == 0]
print(num3)

# 1 ~ 5 사이의 데이터를 제곱을 구해서 리스트 만들기
num4 = [num * num for num in range(1, 6)]
print(num4)

foods = ['떡볶이', '짜장면', '라면', '피자']
sides = ['오뎅', '단무지', '김치']

# zip() 으로 묶는다.
# for food, side in zip(foods, sides):
#     print(food, '-->', side)
'''
if len(foods) > len(sides):
    cnt = len(sides)
else:
    cnt = len(foods)

for k in range(cnt):
    print(foods[k], '-->', sides[k])
'''
for k in range(len(foods)):
    print(foods[k], '-->', sides[k])
    # k는 인덱스이고 len 은 길이라서 -1해줘야함.
    if k >= len(sides) - 1:
        break

# zip 함수를 이용해서 튜플 리스트, 딕셔너리 만들기
tupList = list(zip(foods, sides))
print(tupList)

dic = dict(zip(foods, sides))
print(dic)
