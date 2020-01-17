# 파라메터 값이 2개 또는 3개 등을 전달 받을 수 있는 함수
def para_func(v1, v2, v3=0):
    return v1 + v2 + v3


print(para_func(10, 20))
print(para_func(10, 20, 30))