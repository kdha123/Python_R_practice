# 라이브러리 읽어 들이기
# html 구조화 시켜주는 라이브러리
from bs4 import BeautifulSoup

# 분석하고 싶은 HTML
html = """
<html><body>
    <h1>스크레핑이란?</h1>
    <p>웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# HTML 데이터 분석하기 BeautifulSoup(데이터, 작업모드) 파라메터로 넘긴다.
soup = BeautifulSoup(html, 'html.parser')

# 원하는 부분 추출하기
# soup 에서 object 가져오기
# 위에서 하단으로 모든 단계를 다 선언해서 찾기
h1 = soup.html.body.h1
# 구조와 상관없이 h1찾기
h2 = soup.h1
p1 = soup.html.body.p
p2 = p1.next_sibling.next_sibling

# 요소의 글자 출력하기
print("h1(구조) = " + h1.string)
print("h2(단독) = " + h2.string)
print("p1 = " + p1.string)
print("p2 = " + p2.string)
