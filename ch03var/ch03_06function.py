# -- 함수 선언 부분 --
def my_func():
    print("함수를 호출함.")


def main():
    print('메인 함수 부분이 실행됩니다.')
    my_func()
    print('전역 변수 값 : ', gVar)


# -- 전역 변수 선언 부분 --
gVar = 100

# -- 메인 코드 부분 --
# main()만 선언을 한 경우는 시작부분으로 인정하지 않는다.
# 함수 선언 없이 처리문을 만들거나 if __name__ == '__main__'선언해서 main()을 실행한다.
# if __name__ == '__main__':
main()
#     print('메인 함수 부분이 실행됩니다.')
#     my_func()
#     print('전역 변수 값 : ', gVar)
