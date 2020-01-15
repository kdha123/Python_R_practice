from tkinter import *
from tkinter import messagebox

def my_fuction():
    #messagebox.showinfo('강아지','예뻐요')
    #messagebox.showwarning('강아지','예뻐요')
    messagebox.showerror('강아지','예뻐요')
win = Tk() # 윈도우 생성
win.title('알림창') # 제목표시줄에 출력할 내용

photo1 = PhotoImage(file = 'img/p1.gif')

btn1 = Button(win, image = photo1, command = my_fuction)

btn1.pack()

win.mainloop()
