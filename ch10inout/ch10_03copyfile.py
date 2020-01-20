import os
# 파일 객체 선언
inFp, outFp = None, None

# 복사할 파일이름 입력
inFn = input("복사할 파일명 : ")
outFn = input("복사될 파일명 : ")

# 한줄 단위로 읽은 데이터 저장 변수
inStr = ""

# 한줄 단위로 읽어와서 화면에 표시한다.
if os.path.exists(inFn):
    inFp = open(inFn, "r")
    outFp = open(outFn, "w")
    while True:
        # 한 줄 단위로 읽기
        inStr = inFp.readline()
        if not inStr:
            break
        outFp.writelines(inStr)
else:
    print("파일이 존재하지 않습니다.")
inFp.close()
outFp.close()
