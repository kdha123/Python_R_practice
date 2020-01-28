from urllib.parse import urljoin

base = "http://example.com/html/a.html"

# file 명 -> 같은 위치
print(urljoin(base, "b.html"))
# 하부 위치 sub 밑에
print(urljoin(base, "sub/c.html"))
# .. 상위 -> "http://example.com/"
print(urljoin(base, "../index.html"))
print(urljoin(base, "../img/hoge.png"))
print(urljoin(base, "../css/hoge.css"))

# / -> root 위치 -> http://서버명 위치
print(urljoin(base, "../css/hoge.html"))
# http:// or // -> 외부 url
print(urljoin(base, "http://otherExample.com/wiki"))
print(urljoin(base, "//anotherExample.org/test"))

