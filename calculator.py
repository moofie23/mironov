import tkinter as tk

from PIL import Image, ImageTk

root = tk.Tk()

root.title("Мое приложение")
from tkinter import PhotoImage
import os

#Функция для вычисления макс значения

def max():
    res1 = float(entry1.get())
    res2 = float(entry2.get())
    res3 = float(entry3.get())
    res4 = float(entry4.get())
    if  res1 > res2 and res1 > res3 and res1 > res4:
            max = res1
    else:
            if res2 > res1 and res2 > res3 and res2 > res4:
                max = res2
            else:
                if res3 > res1 and res3 > res2 and res3 > res4:
                    max = res3
                else:
                    max = res4
    label1.config(text = max)

#Функция для вычисления мин значения

def min():
    res1 = float(entry1.get())
    res2 = float(entry2.get())
    res3 = float(entry3.get())
    res4 = float(entry4.get())
    if  res1 < res2 and res1 < res3 and res1 < res4:
            max = res1
    else:
            if res2 < res1 and res2 < res3 and res2 < res4:
                max = res2
            else:
                if res3 < res1 and res3 < res2 and res3 < res4:
                    max = res3
                else:
                    max = res4
    label1.config(text = max)

#Функция для рассчета суммы

def sum():
    res1 = float(entry1.get())
    res2 = float(entry2.get())
    res3 = float(entry3.get())
    res4 = float(entry4.get())
    max = float(int(entry1.get())+int(entry2.get())+int(entry3.get())+int(entry4.get()))
    label1.config(text = max)

#Функция для расчета произведений

def cn():
    res1 = float(entry1.get())
    res2 = float(entry2.get())
    res3 = float(entry3.get())
    res4 = float(entry4.get())
    max = float(int(entry1.get())*int(entry2.get())*int(entry3.get())*int(entry4.get()))
    # label1 = tk.Label(root, text = max, font='Aharoni 15')
    # label1.place(x=250, y=100, width = 150)
    label1.config(text = max)

#Окно приложения

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 900
window_height = 550

res1 = 0
res2 = 0
res3 = 0

canvas = tk.Canvas(root, height=800, width=1000, bg='#00c4ff')
image = Image.open("C:/Mironov/Block_ME_Drive.png")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(550,130, anchor='nw',image=photo)
canvas.grid(row=2,column=1)


x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")
root.configure(bg='#00c4ff')


#Кнопки для вычислений

button1 = tk.Button(root, text="Сумма", bg='blue', fg='white', font='Aharoni 15',command=sum , width = 14)
button1.place(x=100, y = 150)

button2 = tk.Button(root, text="Произведение", bg='blue', fg='white', font='Aharoni 15',command=cn , width = 14)
button2.place(x=100, y = 200)

button3 = tk.Button(root, text="Максимум", bg='blue', fg='white', font='Aharoni 15', command=max , width = 14)
button3.place(x=100, y = 250)

button4 = tk.Button(root, text="Минимум", bg='blue', fg='white', font='Aharoni 15', command=min , width = 14)
button4.place(x=100, y = 300)

#Поля для ввода и вывода значения

entry1 = tk.Entry(root, width = 30,borderwidth = 3, )
entry1.place(x=280, y=150, height=40)


entry2 = tk.Entry(root, width = 30,borderwidth = 3)
entry2.place(x=280, y=200, height=40)

entry3 = tk.Entry(root, width = 30,borderwidth = 3)
entry3.place(x=280, y=250, height=40)


entry4 = tk.Entry(root, width = 30,borderwidth = 3)
entry4.place(x=280, y=300, height=40)

label1 = tk.Label(root,font='Aharoni 15', bg='#00c4ff', fg='white')
label1.place(x=250, y=100)


root.mainloop()