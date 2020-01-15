from tkinter import *

win = Tk() # 윈도우 생성
win.title('라벨') # 제목표시줄에 출력할 내용
win.geometry('300x300')

# 3 라벨을 생성
# 옵션을 여러 형태로 지정
lbl1 = Label(win, text ='파이썬을',bg = 'yellow')
lbl2 = Label(win, text = '열심히', font = ('궁서체',30), fg = 'blue')
lbl3 = Label(win, text = '공부중 입니다.', anchor = CENTER,width = 20, height = 5,bg = 'violet',fg = 'white')

lbl1.pack()
lbl2.pack()
lbl3.pack()

win.mainloop()
