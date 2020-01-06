for k in range(1,10) : 
    print(3, 'x', k, '=' ,3 * k)

'''
print(3, 'x', 1, '=' ,3 * 1)
print(3, 'x', 2, '=' ,3 * 2)
print(3, 'x', 3, '=' ,3 * 3)
print(3, 'x', 4, '=' ,3 * 4)
print(3, 'x', 5, '=' ,3 * 5)
print(3, 'x', 6, '=' ,3 * 6)
print(3, 'x', 7, '=' ,3 * 7)
print(3, 'x', 8, '=' ,3 * 8)
print(3, 'x', 9, '=' ,3 * 9)
'''
# 2에서 9사이에의 수일 때
number = input('단수를 입력 : ')
if 2<= int(number) <=9 :
    for i in range(1,10) : # 1부터 9까지 곱할 때 
        print(number, 'x', i, '=' ,int(number) * i)
else :
    print('2에서 9사이의 수를 입력해주세요!')


'''
# 2에서 9사이에의 수가 아닐 때
if int(number) > 9 or int(number) < 2 : 
    print('2에서 9사이의 수를 입력해주세요!')
else :
    for i in range(1,10) :
        print(number, 'x', i, '=' ,int(number) * i)
'''
