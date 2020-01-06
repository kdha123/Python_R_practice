from tkinter import *


def click_mouse(event):
    txt = ''
    if event.num == 1:
        txt = txt + '마우스 왼쪽 버튼이 ('
    elif event.num == 3:
        txt = txt + '마우스 오른쪽  버튼이 ('
    else:
        txt = txt + '마우스 중앙  버튼이 ('

    txt = txt + str(event.x) + ',' + str(event.y) + ')에서 클릭됨'
    lbl.configure(text = txt)
        
        
   


win = Tk() # 윈도우 생성
win.title('마우스 좌표처리') # 제목표시줄에 출력할 내용
win.geometry('400x400')


lbl = Label(win, text = '이곳이 바뀝니다')

# 윈도우에서 마우스 클릭관련 이벤트가 발생하면
# click_mouse 함수 호출
win.bind('<Button>',click_mouse)
lbl.pack(expand = 1, anchor = CENTER)

win.mainloop()
