'''
result = 0

k = int(input('수를 입력해주세요 : '))
for num in range(1,k+1): # num은 1부터 10까지 1씩 증가, 11이 되면 종료
    result = result + num
print(result)
'''    
result = 1
number = int(input('팩토리얼 수를 입력해주세요 : '))

for x in range(1,number+1) :
    result = result * x
print(result)
