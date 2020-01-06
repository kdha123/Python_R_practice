number1 = input('첫번째 수 입력 : ') # input으로 수를 입력 받는다.
number2 = input('두번째 수 입력 : ') 

print(number1 + number2) # 문자열 결합 연산이 됨
# int함수는 문자를 숫자로 str함수는 숫자를 문자로 바꿔준다.
# 산술 연산
# str로 int함수를 문자로 바꿔서 +하면 공백이 사라진다.
print(number1+'와',number2+'의 곱은',str(int(number1) * int(number2))+'입니다')
print(number1+'와',number2+'의 합은',str(int(number1) + int(number2))+'입니다')
print(number1+'와',number2+'의 차는',str(int(number1) - int(number2))+'입니다')
print(number1+'와',number2+'의 나누기는',str(int(number1) / int(number2))+'입니다')
print(number1+'와',number2+'의 몫은',str(int(number1) // int(number2))+'입니다')
print(number1+'와',number2+'의 나머지는',str(int(number1) % int(number2))+'입니다')
print(number1+'와',number2+'의 거듭제곱은',str(int(number1) ** int(number2))+'입니다')

