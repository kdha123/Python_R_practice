from tkinter import *
from tkinter import messagebox

def my_fuc():
    if chk.get() == 0:
        messagebox.showinfo('체크박스','체크 OFF')
    else:
        messagebox.showwarning('체크박스','체크 ON')
        
win = Tk() # 윈도우 생성
win.title('체크박스') # 제목표시줄에 출력할 내용

chk = IntVar() # IntVar함수는 정수형 형식의 변수를 생성
cb1 = Checkbutton(win, text ='클릭하세요', variable=chk, command = my_fuc)


cb1.pack()
win.mainloop()
