import random #random 모듈을 불러온다.


rps = ['가위', '바위' , '보'] #가위바위보 리스트만들기

computer = random.choice(rps)#random으로 컴퓨터 변수 만들기
player = input('가위/바위/보 중 입력 : ') #input으로 플레이어 입력값 받기

print("컴퓨터 : ",computer) 
print("플레이어 : ",player)

#if rps != player: # 리스트와 문자열 비교 따라서 항상 True
    #print('잘못 입력된 값 : 플레이어 패')

if player not in rps: # if를 통해서 플레이어가 잘못된 값을 입력했을 때 
    print('잘못 입력된 값 : 플레이어 패')
elif computer == player: #if가 참이면 elif는 실행하지 않는다.
    print('비겼습니다!')
elif computer == rps[0] and player == rps[1]: # 컴퓨터 : 가위 / 플레이어 : 바위
   print('플레이어 승!')
elif computer == rps[0] and player == rps[2]: # 컴퓨터 : 가위 / 플레이어 : 보
   print('컴퓨터 승!')
elif computer == rps[1] and player == rps[0]: # 컴퓨터 : 바위 / 플레이어 : 가위
   print('컴퓨터  승!')
elif computer == rps[1] and player == rps[2]: # 컴퓨터 : 바위 / 플레이어 : 보
   print('플레이어  승!')
elif computer == rps[2] and player == rps[0]: # 컴퓨터 : 보 / 플레이어 : 가위
   print('플레이어 승!')
elif computer == rps[2] and player == rps[1]: # 컴퓨터 : 보 / 플레이어 : 바위
   print('컴퓨터 승!')



