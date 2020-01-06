# 자판기 거스름돈 프로그램 ver1.0
# 메뉴 리스트 생성
# 메뉴에 대한 가격 생성
# 주문 개수 리스트
# 메뉴 리스트 프린트하기
# 메뉴에 대한 주문 개수 입력
# 메뉴와 가격을 곱해서 주문 금액 생성
# 거스름돈 구하기
# 주문금액이 투입금액보다 클 때 if문으로 생성

menu = ['커피', '콜라', '사이다']
price = [300, 600, 500]
order = []

for k in range(len(menu)):
    print(menu[k],':',price[k])
    
insert_money = int(input('투입금액 : '))

for item in menu:
    order.append(int(input(item+'개수 입력 : ')))
order_money = 0   
for k in range(len(menu)):
    order_money = order_money + (order[k] * price[k])

money_back = insert_money - order_money

if insert_money>=order_money :
    print('주문금액 : ',order_money)
    print('거스름돈 : ',money_back)
    coin500 = money_back // 500
    back = money_back % 500
    coin100 = back // 100
    print('500원 동전 : ',coin500,'개','100원 동전 : ',coin100,'개')
else:
    print('주문금액이 부족합니다.')
