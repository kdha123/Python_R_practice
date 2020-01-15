from tkinter import *
from tkinter import messagebox

def my_fuc():
    if var.get() == 1:
        lbl1.configure(text ='파이썬',fg ='blue') # configure함수는 라벨의 구성을
    elif var.get() ==2:                          # 바꾸라는 것
        lbl1.configure(text ='R', fg = 'blue')
    else:
        lbl1.configure(text = 'JAVA', fg = 'blue')
        
        
win = Tk() # 윈도우 생성
win.title('라디오버튼') # 제목표시줄에 출력할 내용

var = IntVar() # IntVar함수는 정수형 형식의 변수를 생성
rb1 = Radiobutton(win, text ='파이썬', variable=var, value=1, command = my_fuc)
rb2 = Radiobutton(win, text ='R', variable=var, value=2, command = my_fuc)
rb3 = Radiobutton(win, text ='JAVA', variable=var, value=3, command = my_fuc)

lbl1 = Label(win, text = '수강신청한 언어 : ',fg = 'red')


rb1.pack()
rb2.pack()
rb3.pack()
lbl1.pack()
win.mainloop()
