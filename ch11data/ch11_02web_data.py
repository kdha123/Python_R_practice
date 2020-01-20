# IP 확인 API 로 접근해서 결과 출력하기
# 모듈 읽어들이기
import urllib.request

# 데이터 읽어들이기
url = "http://api.aoikujira.com/ip/ini"
res = urllib.request.urlopen(url)
data = res.read()

# 바이너리 문자열로 변환하기
text = data.decode("utf-8")
print(text)
