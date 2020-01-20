import os

# 입력 파일 변수 선언
infp = None

# 한줄 단위로 텍스트 읽은 데이터 저장 변수
inStr = ""

infn = input("파일명 입력 : ")

# 파일명으로 존재하면 처리
if os.path.exists(infn):
    # 파일 읽기로 연결
    # open(연결파일명, 모드(r, w, a, +, b))
    infp = open(infn, "r")
    # 한줄 단위로 읽어와서 화면에 표시한다.
    while True:
        # 한 줄 단위로 읽기
        inStr = infp.readline()
        # 무한 while 문을 빠져나가는 조건 - 읽어온 데이터가 없다.
        if not inStr:
            break
        print(inStr, end="")
    infp.close()

# 파일이 존재하지 않는 경우 처리
else:
    print("파일이 존재하지않습니다.")

