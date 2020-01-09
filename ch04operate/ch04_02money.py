# 변수 선언
c, c500, c100, c50, c10 = 0, 0, 0, 0, 0


# 함수 선언
def change_money(money):
    cc500 = money // 500
    money = money % 500
    cc100 = money // 100
    money = money % 100
    cc50 = money // 50
    money = money % 50
    cc10 = money // 10
    cc = money % 10
    return cc500, cc100, cc50, cc10, cc


# 메인 코드
my_money = int(input("교환할 돈을 입력하세요 : "))
c500, c100, c50, c10, c = change_money(my_money)
print(c500)
print(c100)
print(c50)
print(c10)
print(c)
