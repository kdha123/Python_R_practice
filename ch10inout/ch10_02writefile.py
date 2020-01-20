# 출력 파일 객체 선언
outFp = None

# 출력할 파일명 입력
outFn = input("출력할 파일명 입력 : ")
outStr = ""

# 파일 객체를 쓰기로 열기
outFp = open(outFn, "w")

# 글자를 입력한대로 출력하기를 한다.
while True:
    outStr = input("텍스트 입력 : ")
    # 빠져나갈 조건 -> 입력을 안하고 엔터를 누른다.
    if not outStr:
        break
    outFp.writelines(outStr + "\n")

outFp.close()

