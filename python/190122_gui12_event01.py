from tkinter import *
from tkinter import messagebox

def click_image(event):
    messagebox.showinfo('마우스','강아지그림에서 마우스 클릭됨')


win = Tk() # 윈도우 생성
win.title('마우스 이벤트') # 제목표시줄에 출력할 내용
win.geometry('400x400')

photo = PhotoImage(file = 'img/p1.gif')
lbl = Label(win, image = photo)

lbl.bind('<Button>',click_image)

lbl.pack(expand = 1, anchor = CENTER)

win.mainloop()
