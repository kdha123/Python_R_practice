# 매표소 프로그램 (version 1.0)
# 성인 : 10000원 / 어린이 8세 미만 : 4000원
# 노인(65세 이상): 5000원

people = int(input('사람수  : '))
ages = []
total = 0
for k in range(people):
    ages.append(int(input('나이를 적어주세요')))# 가족 나이 리스트

for age in ages :
    if age < 8: # 어린이 일 때
        total = total + 4000
    elif age >= 65: # 노인 일 때
        total = total + 5000
    else :
        total = total +10000
print(total,'원')
        
