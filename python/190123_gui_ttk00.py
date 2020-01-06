from tkinter import *
from tkinter import ttk

# 윈도우 객체 생성
w =Tk()
w.title('텍스트 상자')
w.geometry('100x100')

# 텍스트 상자 생성
text_in = ttk.Entry(w, width = 20)

# 버튼 생성
btn1 = ttk.Button(w, text = '입력버튼')

# 윈도우에 배치(격자 방식)
# columnspan은 열 확장
text_in.grid(row = 0,columnspan=1)
# 1행 0열에 버튼 배치
btn1.grid(row = 1, column = 0)

# grid 방식으로 컴포넌트들을 배치 할 예정이므로
# pack을 통한 배치는 에러가 발생한다.
# btn = Button(w, text ='버튼')
# btn.pack()

w.mainloop()
