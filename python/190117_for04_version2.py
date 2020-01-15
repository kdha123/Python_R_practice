# 매표소 프로그램 (version 1.2)
# 성인 : 10000원 / 어린이 8세 미만 : 4000원
# 노인(65세 이상): 5000원

people = int(input('사람수  : '))
ages = []
total = 0

# 인원수
no_kid = 0
no_adult = 0
no_old = 0

for k in range(people):
    ages.append(int(input('나이를 적어주세요')))# 가족 나이 리스트

for age in ages :
    if age < 8: # 어린이 일 때
        total = total + 4000
        no_kid = no_kid + 1
    
    elif age >= 65: # 노인 일 때
        total = total + 5000
        no_old = no_old + 1
    else :
        total = total +10000
        no_adult = no_adult + 1
       
print('어린이',no_kid,'명',no_kid * 4000,'원')
print('성인',no_adult,'명', no_adult * 10000,'원')
print('노인',no_old,'명',no_old * 5000,'원')
print('총 금액 : ',total,'원')
        
