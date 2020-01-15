# LOG파일 남기기 - log.txt
import my_math

# log.txt 파일을 추가모드로 오픈
fp = open('log.txt','a')

while True:
    my_math.gubun()
    select = input('1) 2x+1계산  2) 절대값 3) 팩토리얼  4) 합과 차 5)끝 : ')
    if select == '5':
        print('프로그램을 종료')
        print('프로그램을 종료',file = fp)
        break
    elif select == '1':
        x = int(input('2x+1 계산) x를 입력하세요 : '))
        print('x값이',x,'일 때, 2x+1의 결과는',my_math.f(x), '입니다')
        print('x값이',x,'일 때, 2x+1의 결과는',my_math.f(x), '입니다',file = fp)
    elif select == '2':
        n = int(input('절대값  계산) x를 입력하세요 : '))
        print('x값이',n,'일 때, 절대값의 결과는',my_math.absolute(n),'입니다')
        print('x값이',n,'일 때, 절대값의 결과는',my_math.absolute(n),'입니다',file = fp)
    elif select == '3':
        x = int(input('팩토리얼  계산) x를 입력하세요 : '))
        print('x값이',x,'일 때, 팩토리얼의 결과는',my_math.fac(x),'입니다')
        print('x값이',x,'일 때, 팩토리얼의 결과는',my_math.fac(x),'입니다',file = fp)
    elif select == '4':
        n1 = int(input('첫 번째 x를 입력하세요 : '))
        n2 = int(input('두 번째 y를 입력하세요 : '))
        print('두 수의 합은',my_math.plus_minus(n1,n2)[0],' / 두 수의 차는',my_math.plus_minus(n1,n2)[1],'입니다.')
        print('두 수의 합은',my_math.plus_minus(n1,n2)[0],' / 두 수의 차는',my_math.plus_minus(n1,n2)[1],'입니다.',file = fp)        
    else:
        print('메뉴에서 골라주세요')
        print('메뉴에서 골라주세요',file = fp)

fp.close()
