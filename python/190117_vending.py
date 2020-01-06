# 자판기 거스름돈 프로그램 ver0.1
# 커피 : 300원, 콜라 : 600원, 생수 : 400원
# 투입금액 : 2000
# 1) 콜라 개수 입력 : 1
# 2) 커피 개수 입력 : 2
# 3) 생수 개수 입력 : 0
# 주문 금액 : 1200원 
# 거스름 돈 : 800원
# 500원 동전 1개 , 100원 동전 3개
print('자판기 프로그램')
print('커피 : 300원, 콜라 : 600원, 생수 : 400원, 게토레이 : 900원')

insert_money = int(input('투입금액 : '))

menu = ['콜라','커피','생수']
order = 
for pd in product:
    product.append(int(input))



coke =int(input('콜라개수 입력:'))
coffee = int(input('커피개수 입력 : '))
water = int(input('생수개수 입력 :'))

money_order = (coke * 600) + (coffee * 300) + (water * 400)
money_remainder = insert_money - money_order

if money_order<=insert_money :
    print('주문금액 : ',money_order)
    print('거스름돈 : ',money_remainder)
    coin500 = money_remainder // 500 
    remainder = money_remainder % 500
    coin100 = remainder // 100
    print('500원 동전 : ',coin500,'개','100원 동전 : ',coin100,'개')
else:
    print('주문금액이 부족합니다.')
