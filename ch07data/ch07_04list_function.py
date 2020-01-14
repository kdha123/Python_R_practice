aa = [85, 100, 90, 70, 95, 90]


# 1. 리스트의 개수를 출력
print(len(aa))

# 2. 리스트의 데이터 바꾸지 않으면서 정렬해서 출력
print(sorted(aa))

# 3. 90 데이터의 위치를 출력
# 값이 여러개면 첫번째값을 반환함.
print(aa.index(90))

# 4. 마지막를 데이터를 꺼내면서 제거
aa.pop()
print(aa)

# 5. bb 라는 리스트에 동일한 데이터를 가지도록 처리
bb = aa.copy()
print(bb)

# 6. aa 리스트에서 값이 100인 것을 지운다.
aa.remove(100)
print(aa)

# 7. aa 리스트의 내용 지운다.
aa.clear()
print(aa)
