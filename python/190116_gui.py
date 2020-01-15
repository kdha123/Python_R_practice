from tkinter import *

win = Tk() # 윈도우 생성
win.title('첫번째 그래픽 프로그램') # 제목표시줄에 출력할 내용

btn = Button(win, text = '종료', command = quit
             ) # 버튼 생성
btn.pack() # 버튼을 윈도우에 부착


win.mainloop()
