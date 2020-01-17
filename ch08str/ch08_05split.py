ss = '파이썬을 열심히 공부하는 중'
print(ss)
print(ss.split(), type(ss.split()))

ss = '하나:둘:셋'
print(ss.split(':'))

# 전화번호 3개 -> 010-1111-2222
# 각각의 위치에 따른 데이터 출력
# 010, 1111, 2222
# 분리되어 있는 데이터를 중간에 '-'를 이용해서 완성된 전화번호를 출력한다.
phone = '010-1111-2222'
ph = phone.split('-')
for i in ph:
    print(i)
print('-'.join(ph))

# 정렬 : 가운데, 왼쪽, 오른쪽, 채우기
ss = '파이썬'
# 가운데 정렬
print(ss.center(10))
# 가운데로 정렬하고 빈공간에 '-'
print(ss.center(10, '-'))
# 왼쪽 정렬
print(ss.ljust(10))
# 오른쪽 정렬
print(ss.rjust(10, '-'))
# 빈공간에 0채워넣기
print(ss.zfill(10))
print(ss.isdigit())
