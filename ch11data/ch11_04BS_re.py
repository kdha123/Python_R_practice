from bs4 import BeautifulSoup as bs
import re

html = """
<ul>
    <li><a href="hoge.html">hoge</li>
    <li><a href="https://example.com/fuga">fuga*</li>
    <li><a href="https://example.com/foo">foo*</li>
    <li><a href="http://example.com/aaa">aaa</li>
</ul>
"""

soup = bs(html, 'html.parser')

li = soup.find_all(href=re.compile(r"^https://|http://"))
for e in li:
    print(e.attrs['href'])
    print(e.string)
