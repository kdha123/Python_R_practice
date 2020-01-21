from bs4 import BeautifulSoup

html = """
<html><body>
    <h1 id="title">스크레핑이란?</h1>
    <p id="body">웹 페이지를 분석하는 것</p>
    <p>원하는 부분을 추출하는 것</p>
</body></html>
"""

# HTML 데이터 분석
soup = BeautifulSoup(html, 'html.parser')

# find() 메서드로 원하는 부분 추출하기 id로
title = soup.find(id="title")
body = soup.find(id="body")

print("#title = " + title.string)
print("#%s = %s" % (title["id"], title.string))
print("#body = " + body.string)
print("#%s = %s" % (body["id"], body.string))
# h1의 id
print(title["id"])


