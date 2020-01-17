# 전역 변수 선언
coffee = 0


# 함수 선언 부분
def coffee_machine(button):
    print()
    # 물, 컵을 준비한다. -> 선택 불가능, 자동으로 한다.
    print("#1. (자동으로) 뜨거운 물을 준비한다.")
    print("#2. (자동으로) 종이컵을 준비한다.")
    print()

    # 버튼에 따라서 커피를 탄다.
    if button == 1:
        print("#3. (자동으로)보통커피를 탄다.")
    elif button == 2:
        print("#3. (자동으로) 설탕커피를 탄다.")
    elif button == 3:
        print("#3. (자동으로) 블랙커피를 탄다.")
    else:
        print("#3. (자동으로) 아무거나 탄다.")

    print()


# 메인 부분
# 사용자가 커피 선택
coffee = int(input("어떤 커피 드릴까요?(1.보통, 2.설탕, 3.블랙) : "))
# 기계가 커피를 탄다.
coffee_machine(coffee)
# coffee_machine() -> 요구되어지는 매개변수의 값이 없다.
# coffee_machine(coffee, coffee) -> 2번째 매개값이 없어서 오류
# 함수 이름이 같은 경우 뒤에 것을 호출하기 때문에 오류가 난다.
print('커피나옴')
