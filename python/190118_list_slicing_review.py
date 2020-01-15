# 딕셔너리
foods = {'맥주':'치킨', '소주':'골뱅이소면', '고량주':'양장피', '와인':'치즈'}

# 딕셔너리에 아이템 추가
foods['아무거나'] = '진짜아무거나'

# 딕셔너리의 키를 리스트로 변환
foods_key = list(foods.keys())

# 딕셔너리의 벨류를 리스트로 변환
foods_value = list(food.values())

# 딕셔너리의 값 중 맨 마지막 값 제거(슬라이싱)
#foods_value = foods_value[:-1]

# 딕셔너리의 값 중 맨 마지막 값 제거(pop())
# foods_value.pop()

# 딕셔너리의 값 중 맨 마지막 값 제거(remove)
#foods_value.remove('진짜아무거나')

# 딕셔너리의 값 중 맨 마지막 값 제거(del)
del foods_value[-1]

print(foods_key)
print(foods_value)
