from tkinter import *
from tkinter import messagebox

def my_func():
    if var.get() == 1:
        lbl1.configure(image = photo1) # configure함수는 라벨의 구성을
    elif var.get() ==2:                          # 바꾸라는 것
        lbl1.configure(image = photo2)
    else:
        lbl1.configure(image = photo3)
        
        
win = Tk() # 윈도우 생성
win.title('동물선택하기') # 제목표시줄에 출력할 내용
win.geometry('400x400')

lbl_text = Label(win, text = '좋아하는 동물은',fg = 'blue',font= ('궁서체',20))

var = IntVar() # IntVar함수는 정수형 형식의 변수를 생성
rb1 = Radiobutton(win, text = '고양이1', variable=var, value=1)
rb2 = Radiobutton(win, text ='강아지1', variable=var, value=2)
rb3 = Radiobutton(win, text ='고양이2', variable=var, value=3)

btn_ok = Button(win, text='사진보기',command = my_func)

photo1 = PhotoImage(file = 'img/c1.gif')
photo2 = PhotoImage(file = 'img/p1.gif')
photo3 = PhotoImage(file = 'img/c2.gif')
lbl1 = Label(win, width=200, height=200, bg='yellow', image = None)

lbl_text.pack()
rb1.pack()
rb2.pack()
rb3.pack()
btn_ok.pack()
lbl1.pack()
win.mainloop()
