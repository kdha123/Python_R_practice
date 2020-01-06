from tkinter import *

win = Tk() # 윈도우 생성
win.title('라벨&이미지') # 제목표시줄에 출력할 내용

# 포토이미지 로딩 (폴더경로/파일명.gif)

for n in range(1,11):
    btn = Button(win, text = ('버튼',n))
    btn.pack(side=LEFT)
    



win.mainloop()
