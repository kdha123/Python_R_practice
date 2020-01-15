# 1) 2x+1계산 , 2) 절대값, 3) 팩토리얼 : 3엔터
# 정수를 입력하세요 : 5
# 5팩토리얼의 결과 값은 120 입니다.
# 1) 2x+1계산 , 2) 절대값, 3) 팩토리얼 : 2엔터
# -90의 절대값은 90 입니다.
# 1) 2x+1계산 , 2) 절대값, 3) 팩토리얼 : 4엔터
# 안녕~

def absolute(n):
    r = 0
    if n < 0:
       r = n * -1
    else:
        r = n
    return r

def f(x):
    result = (2 * x) + 1
    return result

def fac(x):
    result = 1
    for h in range(1,x+1):
        result = result * h
    return result

def plus_minus(x, y):
    return [x + y, x - y]

def gubun():
    print('==============================================================')

while True:
    gubun()
    select = input('1) 2x+1계산  2) 절대값 3) 팩토리얼  4) 합과 차 5)끝 : ')
    if select == '5':
        print('안녕~')
        break
    elif select == '1':
        x = int(input('2x+1 계산) x를 입력하세요 : '))
        print('x값이',x,'일 때, 2x+1의 결과는',f(x), '입니다')
    elif select == '2':
        n = int(input('절대값  계산) x를 입력하세요 : '))
        print('x값이',n,'일 때, 절대값의 결과는',absolute(n),'입니다')
    elif select == '3':
        x = int(input('팩토리얼  계산) x를 입력하세요 : '))
        print('x값이',x,'일 때, 팩토리얼의 결과는',fac(x),'입니다')
    elif select == '4':
        n1 = int(input('첫 번째 x를 입력하세요 : '))
        n2 = int(input('두 번째 y를 입력하세요 : '))
        print('두 수의 합은',plus_minus(n1,n2)[0],' / 두 수의 차는',plus_minus(n1,n2)[1],'입니다.')        
    else:
        print('메뉴에서 골라주세요')
            
    
