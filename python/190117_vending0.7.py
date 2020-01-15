# 자판기 거스름돈 프로그램 ver0.7
# 메뉴 리스트 생성
# 메뉴에 대한 가격 생성
# 주문 개수 리스트
# 메뉴 리스트 프린트하기
# 메뉴에 대한 주문 개수 입력
# 메뉴와 가격을 곱해서 주문 금액 생성
# 거스름돈 구하기
# 주문금액이 투입금액보다 클 때 if문으로 생성
menu = ['콜라','커피','생수','게토레이','포카리'] # 메뉴와 가격은 추가할 수 밖에 없음.
prices = [600, 300, 400, 900, 800]
order = []

print('자판기 프로그램')

for k in range(len(menu)): 
    print(menu[k],':', prices[k])

insert_money = int(input('투입금액 : '))

money_order = 0
for item in menu:
    order.append(int(input(item+' 개수 입력 : ')))
    
for k in range(len(menu)): # menu의 개수에 따라 반복 획수가 가변처리됨
    money_order = money_order + (order[k] * prices[k])
    
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
