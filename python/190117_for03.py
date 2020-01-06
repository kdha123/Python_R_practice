# 2에서 9사이에의 수일 때
number = int(input('단수를 입력 : ')) #입력 받을 때 숫자로 바꿔주면 개선된다.

'''
if 2<= number <=9 :
    for i in range(1,10) :
        print(number, 'x', i, '=' ,number * i)
else :
    print('2에서 9사이의 수를 입력해주세요!')
'''


# 2에서 9사이에의 수가 아닐 때
if number > 9 or number < 2 : 
    print('2에서 9사이의 수를 입력해주세요!')
else :
    for i in range(1,10) :
        print(number, 'x', i, '=' ,number * i)

