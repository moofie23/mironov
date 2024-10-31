import tkinter as tk


import math
from PIL import Image, ImageTk

root = tk.Tk()

root.title("Мое приложение")
from tkinter import PhotoImage
import os

#Функция для определения вида треугольника и его площади


def vid():
    a = float(entry1.get())
    b = float(entry2.get())
    c = float(entry3.get())
    x = "\nПлощадь треугольника = "
    Type = "Не определен"
    if a == b and b == c:
         Type = "Равносторонний"
         S = (pow(a,2)*math.sqrt(b))/4
    elif (a==b and b!=c and a!= c) or (b==c and b!=a) or (a==c and a!=c):
         Type = "Равнобедренный"
         S = (a*b)/2
    else:
         Type = "Разносторонний"
         p = (a+b+c)/2
         S = math.sqrt(p)*(p-a)*(p-b)*(p-c)
    if a<=0 or b<=0 or c<=0:
        Type = "Введены неверные значения"
        x = " "
        S = " "
    if (a+b)<c or (b+c)<a or (a+c)<b:
         Type = "Введены неверные значения"
         x = " "
         S = " "
    label1.config(text = str(Type) + str(x) + str(S))

#Окно приложения

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 900
window_height = 550

res1 = 0
res2 = 0
res3 = 0


x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg='#00c4ff')


#Кнопка для определения вида треуг и его площади

button1 = tk.Button(root, text="Определить вид треугольника и его площадь", bg='blue', fg='white', font='Aharoni 15', width = 60, command= vid)
button1.place(x=100, y = 350)

#Поля для ввода значений треугольника

entry1 = tk.Entry(root, width = 30,borderwidth = 3, )
entry1.place(x=130, y=250, height=40)


entry2 = tk.Entry(root, width = 30,borderwidth = 3)
entry2.place(x=330, y=250, height=40)

entry3 = tk.Entry(root, width = 30,borderwidth = 3)
entry3.place(x=530, y=250, height=40)


label1 = tk.Label(root,font='Aharoni 15', bg='#00c4ff', fg='white', text = "Не определено")
label1.place(x=180, y=100, width= 500, height= 130)


root.mainloop()
