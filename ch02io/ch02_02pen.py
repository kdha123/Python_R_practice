# 필요한 라이브러리 등록
import turtle
import random


# 함수 선언 부분 -2줄 띄세요.
# global 은 전역변수
# 함수, 함수에서의 변수는 소문자로 사용하세요.
# 왼쪽 마우스 버튼 - 선을 그린다.
# 포함관계는 {}를 사용하지 않고 들여쓰기를 하세요.
def screen_left_click(x, y):
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x, y)


# 오른쪽 마우스 버튼 - 이동만 - 그리지 않는다.
def screen_right_click(x, y):
    turtle.penup()
    turtle.goto(x, y)


# 가운데 마우스 버튼 - 색상과 거북이 크기조정
def screen_mid_click(x, y):
    global r, g, b
    t_size = random.randrange(1, 10)
    turtle.shapesize(t_size)
    r = random.random()
    g = random.random()
    b = random.random()


# 전역 변수 선언 부분
pSize = 10
r, g, b = 0.0, 0.0, 0.0


# 메인 코드 부분
# 창의 이름 셋팅
turtle.title('거북이로 그림 그리기')
# 그려질 포인터 형태 셋팅
turtle.shape('turtle')
# 선의 두께 셋팅
turtle.pensize(pSize)

# onscreenclick -  클릭 이벤트 처리
turtle.onscreenclick(screen_left_click, 1)
turtle.onscreenclick(screen_mid_click, 2)
turtle.onscreenclick(screen_right_click, 3)

# 실행된 창을 유지시킨다.
turtle.done()
