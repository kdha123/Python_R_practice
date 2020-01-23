# 실습 전에 한빛미디어 사이트에 회원가입을 해주세요.
import requests
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin

# 아이디 와 비밀번호
USER = "kdha123"
PASS = "*********"

# 세션 시작하기
session = requests.session()

# 로그인 하기
# form tag 안에 입력되는 input tag 의 name 을 확인해서 작성한다.
login_info = {
    "m_id": USER,
    "m_passwd": PASS
}
# post 방식으로 전달하고 form tag -> action 속성값
# 아이디와 비밀번호를 받아서 로그인 처리를 해주는 프로그램
url_login = "http://www.hanbit.co.kr/member/login_proc.php"

# 서버와 post 통신을 이용한 데이터 전송
res = session.post(url_login, data=login_info)
# 오류가 발생되면 예외가 발생
# status 확인 -> 200:정상, 그외 비정상 : 404, 500 등
res.raise_for_status()

# 마이페이지에 접근하기
url_mypage = "http://www.hanbit.co.kr/myhanbit/myhanbit.html"
res = session.get(url_mypage)
res.raise_for_status()

# 마일리지와 코인 가져오기
soup = bs(res.text, "html.parser")
mileage = soup.select_one(".mileage_section1 span").get_text()
ecoin = soup.select_one(".mileage_section2 span").get_text()
print("마일리지 : "+mileage, type(mileage))
print("이코인 : "+ecoin)
