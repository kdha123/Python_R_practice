# input() - 사용자에게 문자열로 데이터를 입력받는다.
a = int(input("첫 번째 숫자를 입력해주세요 : "))
b = int(input("두 번째 숫자를 입력해주세요 : "))
# input으로 문자열을 받기 때문에 연산을 할 수 없어서 int()를 이용해서 정수로 변환한다.

result = a + b
print(a, '+', b, '=', result)
result = a - b
print(a, '-', b, '=', result)
result = a * b
print(a, '*', b, '=', result)
result = a / b
print(a, '/', b, '=', result)
