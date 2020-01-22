# 빅데이터 수집
from bs4 import BeautifulSoup as bs
import urllib.request as req
# 1. 데이터가 포함이된 웹페이지를 찾으세요.
url = "https://auto.naver.com/car/mainList.nhn?isMnfcoAll=Y"
# 2. 웹페이지에 포함이되어 있는 데이터를 가져와서 리스트로 만들고 출력하세요.
# HTML 분석
res = req.urlopen(url)
soup = bs(res, 'html.parser')

car_list = soup.select('.model_lst > li')
# print(car_list)
for car in car_list:
    name = car.select_one('.box > strong').string
    price = car.select_one('.cont').string
    print(name, price)
