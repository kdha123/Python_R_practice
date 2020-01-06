from tkinter import *


win = Tk() # 윈도우 생성
win.title('라벨&이미지') # 제목표시줄에 출력할 내용

# 포토이미지 로딩 (폴더경로/파일명.gif)

for n in range(1,4):
    btn = Button(win, text = ('버튼',n))
    #btn.pack(side=BOTTOM)
    btn.pack(fill=X, ipadx=10, ipady=50, padx =10, pady=10)
    # 그냥 pad는 버튼과 버튼사이 여백, ipad는 버튼 안의 여백
win.mainloop()
