aa = [10, 20, 30, 40, 50]

# list aa의 값의 순서르 거꾸로 정렬하여 출력하시오.
print(aa[::-1])
print(aa)

# 일부 데이터의 변경
# aa 리스트 데이터 중 3번째 30을 300으로
aa[2] = 300
print(aa)

# 1번째 500으로, 2번재는 400으로 변경
aa[0:2] = [500, 400]
print(aa)

# aa list 에서 1~2 데이터를 700하나로 변경
aa[1:3] = [700]
print(aa)

aa[1] = [1000, 2000]
print(aa)
print(type(aa[0]))
print(type(aa[1]))

# list 의 데이터 삭제
# 바꿔치기
aa[2:] = []
print(aa)
