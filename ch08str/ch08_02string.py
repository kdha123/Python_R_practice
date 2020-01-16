ss = "파이썬최고"

print(ss)
print(ss[1:3])

ss = "파이썬 "+'최고'
print(ss)
ss = '파이썬'*3
print(ss)

# 문자열을 입력 받아서 역순으로 나오게하기
inStr, outStr = "", ""
count, i = [0]*2

# inStr = input("문자를 입력하세요 : ")
inStr = "Python is fun. 재미있다."
count = len(inStr)

for i in range(0, count):
    outStr += inStr[count-(i+1)]
print("거꾸로 출력 --> " + outStr)

for i in range(count-1, -1, -1):
    print(inStr[i], end="")
print()
print(inStr[::-1])

# 대문자와 소문자 변환하기
ss = 'Python is very fun. 재미있음'
print(ss.upper())
print(ss.lower())
print(ss.swapcase())
print(ss.title())
