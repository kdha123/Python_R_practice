# 1. 214.png 파일을 test.png 로 다운로드하기
# 라이브러리 읽어 들이기
import urllib.request

# URL 과 저장 경로 지정하기
url = "http://uta.pw/shodou/img/28/214.png"

# 저장할 파일명 - 확장명은 같아야한다.
saveName = "test.png"

# 다운로드
urllib.request.urlretrieve(url, saveName)
print("완료")

saveName = 'test2.png'
# 파일 오픈하는 형식에 의해서 데이터를 읽어서 저장하는 방식
mem = urllib.request.urlopen(url).read()

# with 문으로 선언된 개체는 with 문 밖으로 나가면서 소멸시킨다.
# JAVA -> try{자원선언} try 문 밖으로 나가면서 close() 된다.
with open(saveName, mode="wb") as f:
    f.write(mem)
    print("읽기쓰기로 저장완료")


# 2. 다운로드 받고자하는 이미지 파일을 찾아서 다운로드하기
url1 = "https://i.pinimg.com/originals/4e/21/12/4e2112e57f4299bb549df36b12632531.jpg"
saveName = "test1.png"

urllib.request.urlretrieve(url1, saveName)
print("완료")
