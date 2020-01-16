ss = '   파   이   썬   '
print(ss)

# 앞 뒤 공백을 없애서 출력
print(ss.strip())
# 글자 사이의 공백은 하나만 남긴다.
ss1 = ss.strip()
print(ss1.replace("   ", " "))

outStr = ""
for i in range(0, len(ss)):
    if ss[i] != ' ':
        outStr += ss[i] + " "
print(outStr.strip())


# 문자 사이의 공백을 하나로 만드는 함수
def blackwithword(s):
    s = s.strip()
    while s.find("  ") >= 0:
        s = s.replace("  ", " ")
    return s


print(blackwithword(ss))
