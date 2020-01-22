from bs4 import BeautifulSoup

# HTML 분석 데이터
html = """
<html><body>
    <div id="meigen">
        <h1>위키북스 도서</h1>
        <ul class="items">
            <li>유니티 게임 이펙트 입문</li>
            <li>스위프트로 시작하는 아이폰 앱 개발 교과서</li>
            <li>모던 웹사이트 디자인의 정석</li>
        </ul>
    </div>
</body></html>
"""

# HTML 분석
soup = BeautifulSoup(html, 'html.parser')

# css 쿼리로 필요한 부분 추출하기
# div#meigen > h1 : div#meigen 바로 아래의 h1 tag
h1 = soup.select_one('div#meigen > h1').string
print("h1 = ", h1)
# print(soup.select('div#meigen > ul.items'))
# div#meigen > ul.items : div#meigen 바로 아래의 class 가 items 인 ul tag
li_list = soup.select('div#meigen > ul.items > li')

for li in li_list:
    print("li = ",li.string)
