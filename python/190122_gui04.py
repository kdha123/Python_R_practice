from tkinter import *

win = Tk() # 윈도우 생성
win.title('라벨&이미지') # 제목표시줄에 출력할 내용

# 포토이미지 로딩 (폴더경로/파일명.gif)
photo = PhotoImage(file = 'img/p1.gif')
lbl1 = Label(win, image = photo)

lbl1.pack()


win.mainloop()
