from tkinter import *
from tkinter import messagebox

def click_left(event):
    messagebox.showinfo('마우스','마우스 왼쪽 버튼 클릭')

def click_right(event):
    messagebox.showinfo('마우스','마우스 오른쪽 버튼 클릭')

def click_center(event):
    messagebox.showwarning('마우스','마우스 중앙 버튼 클릭')
win = Tk() # 윈도우 생성
win.title('마우스 이벤트') # 제목표시줄에 출력할 내용

# 마우스 왼쪽 / 중앙 / 오른쪽 버튼 클릭 이벤트 발생 시
# 각각의 대응되는 함수로 엮여둠
win.bind('<Button-1>',click_left)
win.bind('<Button-2>',click_center)
win.bind('<Button-3>',click_right)

win.mainloop()
