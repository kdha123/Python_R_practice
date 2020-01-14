# list 는 데이터 변경이 가능 [], tuple 은 데이터 변경이 불가능 ()
tt = (10, 20, 30)

print(tt, type(tt))

# 값을 할당할 수 없다.
print(tt[2])
# tt[2] = 300
# tt.append(40)

print(tt[0:2])
# tt1 = tt.copy()
tt1 = tt
print(tt1)
print(tt1 + tt)
print(tt * 3)

# tuple -> list -> tuple
aa = list(tt)
aa[1] = 200
print(aa)
tt = tuple(aa)
print(tt)
