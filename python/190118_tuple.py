# tuple : 읽기 전용 자료구조!!!
# 원소의 값을 수정할 수 없다.

l = [1, 2, 3]
t = (1, 2, 3)

print(type(l))
print(type(t))

l[-1] = 55
print(l)

#t[-1] = 55 # 에러 : 원소값 수정 불가
print(t[-1])

#del t # 튜플 전체 삭제는 가능

temp = list(t) # 튜플을 리스트로 변환
temp[1] = 7
t = tuple(temp) # 리스트를 튜플로 변환
print(t[1])
print(t)
