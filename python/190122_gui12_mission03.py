# 버튼들 밑에 라벨 추가
# 라벨에는 페이지 번호 표시
# 첫 번 째 이미지 일때는 1/3
# 두 번 째 이미지 일때는 2/3
# 마지막은 3/3

from tkinter import *
from tkinter import messagebox

photos = ['c1.gif','p1.gif','c2.gif']
idx = 0 # 그림 리스트의 인덱스 번호
# page up, page down 키보드를 이용

def next_botton():
    #messagebox.showinfo('잘되나','굳')
    global idx # 전역변수 idx 사용
    idx = idx + 1

    if idx == len(photos):
        idx = 0

    if idx < len(photos):
        photo = PhotoImage(file = 'img/'+photos[idx])
        lbl.configure(image = photo)
        lbl.image_names = photo
        lbl_page_n.configure(text = str(idx+1)+'/'+str(len(photos)))

def prev_botton():
    #messagebox.showinfo('잘되나','굳')
    global idx # 전역변수 idx 사용
    idx = idx - 1

    if idx < 0:
        idx = len(photos)-1

    if idx < len(photos):
        photo = PhotoImage(file = 'img/'+photos[idx])
        lbl.configure(image = photo)
        lbl.image_names = photo
        lbl_page_n.configure(text = str(idx+1)+'/'+str(len(photos)))

def page_up(e): # 이전으로 가기
    prev_botton()
def page_down(e): # 다음으로 가기
    next_botton()





win = Tk() 
win.title('동물사진') 
win.geometry('400x400')

photo1 = PhotoImage(file = 'img/'+photos[0])

lbl = Label(win, image = photo1)


btn1 = Button(win, text = 'NEXT', command = next_botton)
btn2 = Button(win, text = 'PREV', command = prev_botton)

lbl_page_n = Label(win, text = str(idx)+'/3')
# Prior(키보드의 page up 키 )는 page_up 함수와 바인딩
# Next(키보듸의 page down 키)는 page_down 함수와 바인딩
win.bind('<Prior>',page_up)
win.bind('<Next>',page_down)

lbl.pack()
lbl_page_n.pack()
btn1.pack(side =RIGHT, ipadx = 80)
btn2.pack(side = LEFT, ipadx = 80)

win.mainloop()
