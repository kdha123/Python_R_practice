import turtle
import random


# 전역 변수 선언------------
# swidth , sheight 는 윈도창의 폭과 높이, pSize 는 펜의 두께 준비
# exitCount 는 윈도창 밖으로 빠져나간 횟수를 위해서 준비.
# r, g, b 는 색상, angle 과 dist 는 임의로 이동할 거리와 각도,
# curX dhk curY 는 현재 거북이의 위치

swidth, sheight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0] * 7

# 메인 코드------------
# 창의 제목, 거북이 모양, 펜 두께, 윈도창 크기, 안쪽 화면 크기 지정
turtle.title('거북이가 맘대로 다니기')
turtle.shape("turtle")
turtle.pensize(pSize)
turtle.setup(width=swidth + 30, height=sheight + 30)
turtle.screensize(swidth, sheight)

# while True: <- 무한 반복
while True:
    r, g, b = random.random(), random.random(), random.random()
    turtle.pencolor((r, g, b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    # screen 밖으로 빠져 나갔는지 알기 위해서 거북이의 위치구하기
    curX = turtle.xcor()
    curY = turtle.ycor()
# 임의의 색상 설정하고 각도는 360도 범위, 거리는 1~100 범위
# 거북이의 각도 설정 후 거리만큼 이동
# 거북이의 현재 위치 구함
    # 스크린 밖으로 빠져 나갔는지 확인
    # 스크린 안에 있는 조건
    if((-swidth / 2 <= curX) and (curX <= swidth / 2)) and ((-sheight / 2 <= curY) and (curY <= sheight / 2)):
        pass
# pass 실행해서 if 문을 그냥 종료하고 다시 while 문 수행이 범위를 벗어난다면
# 중앙으로 이동해서 다시 펜사용
    else:
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitCount += 1
        if exitCount >= 5:
            break
# 거북이가 바깥으로 나간 횟수를 하나 증가
# 5회 이상 밖으로 나갔다면 break 문으로 while 문을 빠져나감
turtle.done()
