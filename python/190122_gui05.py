from tkinter import *

win = Tk() # 윈도우 생성
win.title('라벨&이미지') # 제목표시줄에 출력할 내용

# 포토이미지 로딩 (폴더경로/파일명.gif)
photo1 = PhotoImage(file = 'img/p1.gif')
photo2 = PhotoImage(file = 'img/p2.gif')
photo3 = PhotoImage(file = 'img/p3.gif')

lbl1 = Label(win, image = photo1)
lbl2 = Label(win, image = photo2)
lbl3 = Label(win, image = photo3)

lbl1.pack(side = LEFT)
lbl2.pack(side = LEFT)
lbl3.pack()


win.mainloop()
