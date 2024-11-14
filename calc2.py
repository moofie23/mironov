from tkinter import *

window = Tk()
window.title('Кулькулятор')
window.geometry('450x350')
def input(symbol):
    entry.insert(END, symbol)

def clear():
    entry.delete(0,END)

def result():
    chis = entry.get()
    first = 0
    result = 0
    if '+' in chis:
        move = chis.split('+')
        first = float(move[0])
        second = float(move[1])
        result = first + second
    if '-' in chis:
        move = chis.split('-')
        first = float(move[0])
        second = float(move[1])
        result = first - second
    if '/' in chis:
        move = chis.split('/')
        first = float(move[0])
        second = float(move[1])
        result = first / second
    if '*' in chis:
        move = chis.split('*')
        first = float(move[0])
        second = float(move[1])
        result = first * second
    if '^' in chis:
        move = chis.split('^')
        first = float(move[0])
        second = float(move[1])
        result = pow(first, second)
    clear()

    entry.insert(0, result)
        
        
        



entry = Entry(window, width=17, font = ('Arial', 20))
entry.place(x=95, y=50)

btn1 = Button(window, bg='Black', fg='White', text='1', command = lambda:input('1'))
btn1.place(x=100, y=100, width=50,height=50)

btn2 = Button(window, bg='Black', fg='White', text='2', command = lambda:input('2'))
btn2.place(x=150, y=100, width=50,height=50)

btn3 = Button(window, bg='Black', fg='White', text='3', command = lambda:input('3'))
btn3.place(x=200, y=100, width=50,height=50)

btn4 = Button(window, bg='Black', fg='White', text='4', command = lambda:input('4'))
btn4.place(x=100, y=150, width=50,height=50)

btn5 = Button(window, bg='Black', fg='White', text='5', command = lambda:input('5'))
btn5.place(x=150, y=150, width=50,height=50)

btn6 = Button(window, bg='Black', fg='White', text='6', command = lambda:input('6'))
btn6.place(x=200, y=150, width=50,height=50)

btn7 = Button(window, bg='Black', fg='White', text='7', command = lambda:input('7'))
btn7.place(x=100, y=200, width=50,height=50)

btn8 = Button(window, bg='Black', fg='White', text='8', command = lambda:input('8'))
btn8.place(x=150, y=200, width=50,height=50)

btn9 = Button(window, bg='Black', fg='White', text='9', command = lambda:input('9'))
btn9.place(x=200, y=200, width=50,height=50)

btn_plus = Button(window, bg='Black', fg='White', text='+', command = lambda:input('+'))
btn_plus.place(x=250, y=100, width=50, height=50)

btn_minus = Button(window, bg='Black', fg='White', text='-', command = lambda:input('-'))
btn_minus.place(x=250, y=150, width=50, height=50)

btn_divide = Button(window, bg='Black', fg='White', text='/', command = lambda:input('/'))
btn_divide.place(x=250, y=200, width=50, height=50)

btn_multiply = Button(window, bg='Black', fg='White', text='*', command = lambda:input('*'))
btn_multiply.place(x=250, y=250, width=50, height=50)

btn_result = Button(window, bg='Black', fg='White', text='=', command = result)
btn_result.place(x=200, y=250, width=50, height=50)

btn_clear = Button(window, bg='Black', fg='White', text='C', command = clear)
btn_clear.place(x=150, y=250, width=50, height=50)

btn_dot = Button(window, bg='Black', fg='White', text='.', command = lambda:input('.'))
btn_dot.place(x=100, y=250, width=50, height=50)

btn_degree = Button(window, bg='Black', fg='White', text='^', command = lambda:input('^'))
btn_degree.place(x=300, y=100, width=50, height=200)




window.mainloop()