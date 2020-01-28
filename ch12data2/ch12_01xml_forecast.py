from bs4 import BeautifulSoup as bs
import urllib.request as req
import os.path

# XML 다운로드 -> 기상청에서 제공하고 있는 날시 예보 데이터
url = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108"
# 저장 파일명
savename = 'forecast.xml'
# 파일명이 존재하지 않는 경우 다운로드
if not os.path.exists(savename):
    req.urlretrieve(url, savename)

# BeautifulSoup 로 분석하기
# 다운로드 받은 파일을 읽기 전용으로 읽어온다. -> 문자열
xml = open(savename, "r", encoding="utf-8").read()
# 구조를 가진 오브젝트로 만든다.
soup = bs(xml, 'html.parser')

# 각 지역 확인하기
# 표시할 정보가 들어있는 딕셔너리 데이터
info = {}
# 모든 지역의 데이터 찾기
for location in soup.find_all("location"):
    name = location.find('city').string
    weather = location.find('wf').string
    if not (weather in info):
        info[weather] = []
    info[weather].append(name)

# 각 지역의 날시를 구분해서 출력하기
for weather in info.keys():
    print("+", weather)
    for name in info[weather]:
        print("| - ", name)
