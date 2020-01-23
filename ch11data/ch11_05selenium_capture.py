from selenium.webdriver import Firefox, FirefoxOptions

url = "http://www.naver.com"

# 파이어폭스를 헤드리스 모드로 설정하는 옵션
options = FirefoxOptions()
options.add_argument('-headless')

# 파이어폭스 드라이버 추출
browser = Firefox(options=options)

# URL 읽어들이기
browser.get(url)

# 화면을 캡처해서 저장
browser.save_screenshot("Website.png")

# 브라우저 종료
browser.quit()
