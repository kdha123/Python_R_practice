money = int(input("교환할 돈은 얼마? "))
print()
money500 = money // 500
print("500원짜리 ==> ", money500, '개')
money100 = (money - (500 * money500)) // 100
print("100원짜리 ==> ", money100, '개')
money50 = (money - (100 * money100) - (500 * money500)) // 50
print("50원짜리 ==> ", money50, '개')
money10 = (money - (50 * money50) - (100 * money100) - (500 * money500)) // 10
print("10원짜리 ==> ", money10, '개')
last_money = money - (10 * money10) - (50 * money50) - (100 * money100) - (500 * money500)
print("바꾸지 못한 잔돈 ===> ", last_money, '원')
