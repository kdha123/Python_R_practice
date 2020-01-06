#이전 버튼 버전

from tkinter import *
from tkinter import messagebox

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
        
def type_key(event):
    #messagebox.showinfo('키보드 이벤트','눌린 키 : '+str(event.keycode))
    messagebox.showinfo('키보드 이벤트','눌린 키 : '+chr(event.keycode))
    
    
win = Tk() # 윈도우 생성
win.title('마우스 좌표처리') # 제목표시줄에 출력할 내용
win.geometry('400x400')


lbl = Label(win, text = '이곳이 바뀝니다')

win.bind('<Button>',click_mouse)
win.bind("<Key>",type_key)

lbl.pack(expand = 1, anchor = CENTER)

win.mainloop()
