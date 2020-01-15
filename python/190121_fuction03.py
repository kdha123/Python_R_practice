# 하나의 함수로 더하기/빼기 연산 해결
def plus_minus(x, y): #매개변수가 2개
    #return (x + y, x - y)
    return [x + y, x - y]


n1 = int(input('첫 번째 수를 입력하세요 : '))
n2 = int(input('두 번째 수를 입력하세요 : '))

print('두 수의 합은',plus_minus(n1,n2)[0],' / 두 수의 차는',plus_minus(n1,n2)[-1],'입니다.')

