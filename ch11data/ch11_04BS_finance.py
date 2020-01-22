from bs4 import BeautifulSoup
import urllib.request as req

# HTML 가져오기
url = "https://finance.naver.com/marketindex/"
# euc-kr 엔코딩해서 불러온다.
res = req.urlopen(url).read()

# HTML 분석하기
soup = BeautifulSoup(res, 'html.parser', from_encoding="euc-kr")

# 데이터 추출
data_li = soup.select('.data > .data_lst > li')
# print(data_li) 
for d in data_li:
    nation = d.select_one('.h_lst > .blind')
    price = d.select_one('.head_info > .value')
    print("%s의 환율은 %s" % (nation.string, price.string))
