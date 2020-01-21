import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL 인코딩한다.
values = {'stnId': '109'}

# k=v ==> query
params = urllib.parse.urlencode(values)

# 요청 전용 URL 을 생성합니다.
url = API + "?" + params
print('url='+url)

# 다운로드
data = urllib.request.urlopen(url).read()
# 읽어온 데이터 한글처리
text = data.decode("UTF-8")
# print(text)
soup = BeautifulSoup(text, 'html.parser')
title = soup.find('title').string
locations = soup.find_all('location')
# print(locations)
for a in locations:
    print("도시 : ", a.city.string, '---------------')
    data = a.find_all('data')
    for b in data:
        print("일시 :", b.tmef.string)
        print("날씨 :", b.wf.string)
        print("최저온도 :", b.tmn.string)
        print("최고온도 :", b.tmx.string)

