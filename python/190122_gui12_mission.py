from tkinter import *
from tkinter import messagebox

photos = ['c1.gif','p1.gif','c2.gif']
idx = 0 # 그림 리스트의 인덱스 번호
# 이전버튼 버전
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
        

win = Tk() 
win.title('동물사진') 
win.geometry('400x400')

photo1 = PhotoImage(file = 'img/'+photos[0])

lbl = Label(win, image = photo1)


btn1 = Button(win, text = 'NEXT', command = next_botton)
btn2 = Button(win, text = 'PREV', command = prev_botton)

lbl.pack()
btn1.pack(side =RIGHT, ipadx = 80)
btn2.pack(side = LEFT, ipadx = 80)

win.mainloop()
