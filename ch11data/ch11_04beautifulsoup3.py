from bs4 import BeautifulSoup

html = """
<html><body>
    <ul>
        <li><a href="http://www.naver.com">naver</a></li>
        <li><a href="http://www.daum.net">daum</a></li>
    </ul>
</body></html>
"""

linklist = []

# html 구조
soup = BeautifulSoup(html, 'html.parser')
# a 태그의 데이터가 여러개 이므로 find_all()을 사용해서 모두 찾기한다.
links = soup.find_all('a')
print(links)

# 링크 목록 출력하기
for a in links:
    # 데이터 한개를 가져오면({site:값}, url:값)
    data = {}
    href = a.attrs['href']
    text = a.string
    print(text, ">", href)
    # 딕셔너리에 데이터 추가
    data["site"] = text
    data["url"] = href
    linklist.append(data)

print(linklist)
