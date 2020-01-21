import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

API = "http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

# 매개변수를 URL 인코딩한다.
values = {'stnId': '108'}

# k=v ==> query
params = urllib.parse.urlencode(values)

# 요청 전용 URL 을 생성합니다.
url = API + "?" + params
print('url='+url)

# 다운로드
data = urllib.request.urlopen(url).read()
# 읽어온 데이터 한글처리
text = data.decode("UTF-8")
print(text)
soup = BeautifulSoup(text, 'html.parser')
wf = soup.find('wf')
print(wf.string)
