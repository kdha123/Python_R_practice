while True:
    ans = input('서울, 런던, 파리 중 영국의 수도는 ? ')
    if ans == '런던' :
        print('정답입니다!')
        break
    elif ans == '서울' :
        print('서울은 대한민국의 수도 입니다.')
    elif ans == '파리' :
        print('파리는 프랑스의 수도 입니다.')
    else :
        print('보기 중 에서 골라주세요.')
