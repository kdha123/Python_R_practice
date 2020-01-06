from tkinter import *
from tkinter import ttk

def btn_pressed(v):
    # 텍스트 입력창에 삽입
    text_in.insert("end",v)
    # 콘솔창에 출력
    # print(v, "눌림")


w =Tk()
w.title('텍스트 상자')
w.geometry('400x400')

# 텍스트입력 창의 값 저장할 변수 선언
value_in = StringVar(w, value='')

# 컴포넌트 생성
text_in = ttk.Entry(w, width = 30, textvariable = value_in)
btn7 = ttk.Button(w, text = '7',command = lambda:btn_pressed('7'))
btn8 = ttk.Button(w, text = '8',command = lambda:btn_pressed('8'))
btn9 = ttk.Button(w, text = '9',command = lambda:btn_pressed('9'))
btn_div = ttk.Button(w, text = '/',command = lambda:btn_pressed('/'))

btn4 = ttk.Button(w, text = '4',command = lambda:btn_pressed('4'))
btn5 = ttk.Button(w, text = '5',command = lambda:btn_pressed('5'))
btn6 = ttk.Button(w, text = '6',command = lambda:btn_pressed('6'))
btn_mul = ttk.Button(w, text = '*',command = lambda:btn_pressed('*'))

btn1 = ttk.Button(w, text = '1',command = lambda:btn_pressed('1'))
btn2 = ttk.Button(w, text = '2',command = lambda:btn_pressed('2'))
btn3 = ttk.Button(w, text = '3',command = lambda:btn_pressed('3'))
btnminus = ttk.Button(w, text = '-',command = lambda:btn_pressed('-'))

btnC = ttk.Button(w, text = 'CE',command = lambda:btn_pressed('CE'))
btn0 = ttk.Button(w, text = '0',command = lambda:btn_pressed('0'))
btn_eq = ttk.Button(w, text = '=',command = lambda:btn_pressed('='))
btnplus = ttk.Button(w, text = '+',command = lambda:btn_pressed('+'))




# 배치
text_in.grid(row = 0,columnspan=4)
btn7.grid(row = 1, column = 0)
btn8.grid(row = 1, column = 1)
btn9.grid(row = 1, column = 2)
btn_div.grid(row = 1, column = 3)

btn4.grid(row = 2, column = 0)
btn5.grid(row = 2, column = 1)
btn6.grid(row = 2, column = 2)
btn_mul.grid(row = 2, column = 3)

btn1.grid(row = 3, column = 0)
btn2.grid(row = 3, column = 1)
btn3.grid(row = 3, column = 2)
btnminus.grid(row = 3, column = 3)

btnC.grid(row = 4, column = 0)
btn0.grid(row = 4, column = 1)
btn_eq.grid(row = 4, column = 2)
btnplus.grid(row = 4, column = 3)


w.mainloop()
