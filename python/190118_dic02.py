import random
foods = {'맥주':'치킨', '소주':'골뱅이소면', '고량주':'양장피', '와인':'치즈'}
foods['아무거나'] = '아무거나' # 키/벨류 추가
foods['고량주'] = '짬뽕' #양장피를 짬뽕으로 수정(따로 메뉴를 새로 생성하지 않음.)

while True :
    drink = input(str(list(foods.keys()))+'에서 고르세요.(아무거나 포함,끝 입력시 종료)) : ')
    if drink == '끝':
        break
    elif drink == '아무거나': #랜덤 픽
        temp = list(foods.keys())
        temp1 = list(foods.values())
        rd = random.choice(temp[0:-1])
        rf = random.choice(temp1[0:-1])
        print(rd+'와',rf+'을  드리겠습니다')
    elif drink in foods.keys(): #입력 값이 foods 딕셔너리 키 중에 있으면
        print(drink + '에 어울리는 안주는',foods[drink]+'입니다')
    else:
        print(drink+'은 판매하지 않습니다. 메뉴에서 골라주세요.')

