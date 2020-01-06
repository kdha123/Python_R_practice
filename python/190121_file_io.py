# hoseo.txt 파일을 쓰기('w') 모드로 오픈
# 쓰기모드로 만들 파일의 주소를 fp가 받는다.
fp = open('hoseo.txt','w')
# fp = open('hoseo.txt','a') <- 추가모드

# fp의 주로를 찾아가서 '파이썬 재미있어요!' 문자열을 hoseo.txt파일에 쓴다.
print('파이썬 재미있어요!',file = fp)

# fp가 가지고 있는 주소를 메모리 해제한다.
fp.close()
