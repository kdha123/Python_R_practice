def multi_return():
    return 100, 200


# main
a, b = 10, 20
print(a, b)
print(multi_return())

# 2개의 리턴값 2개의 변수에 각각 넣을 수 있다.
a, b = multi_return()
print(a, b)
