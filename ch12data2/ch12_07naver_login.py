from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
import time

# Issue 1 -> 책 예제로 로그인 시 네이버 캡차 시스템에 걸려 로그인 실패
# 편법을 통해 복사붙여 넣기 이용 : 대신 Headless 모드론 불가
# 복사 붙여넣기를 이용하기 위해 pyperclip 설치 -> 터미널에 pip install pyperclip

USER = "012rlaehdgus"
PASS = "wjdals29@"


# 복사붙여넣기를 수행하는 함수
def copy_input(xpath, input):
    # pyperclip 모듈 라이브러리 이용
    pyperclip.copy(input)
    # id가 들어왔을 시 id 칸 클릭 pw 가 들어왔을 시 pw 클릭 (xpath)로
    browser.find_element_by_xpath(xpath).click()
    # ActionChains -> CTR 입력 -> V 입력 -> CTR 업 을 통해 복사 붙여넣기 시행
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
    time.sleep(1)


options = FirefoxOptions()
# headless 옵션 적용 시 로그인 실패
# options.add_argument('-headless')
browser = Firefox(options = options)
browser.implicitly_wait(3)
browser.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
# xpath 를 통해 html input tag (get_element_by_id로 찾아도 됨)선택
copy_input('//*[@id="id"]', USER)
# sleep 없이 수행 시 캡차에 걸릴 수 있어 1초의 텀을 준다.
time.sleep(1)
copy_input('//*[@id="pw"]', PASS)
time.sleep(1)

# xpath를 통해 form 태그 안의 input 태그를 찾고 click 을 통해 submit
browser.find_element_by_xpath('//*[@id="log.login"]').click()

browser.get("https://order.pay.naver.com/main/cart")

# class 가 zzim_add 인 태그를 찾고 그 밑의 a 태그 중 target이 _blank 인 값들을 찾는다.
products = browser.find_elements_by_xpath("//*[@class='zzim_add']/a[@target='_blank']")
print(products)

for product in products:
    print("-", product.text)
