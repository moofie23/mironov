import tkinter as tk

from PIL import Image, ImageTk

root = tk.Tk()

root.title("Мое приложение")
from tkinter import PhotoImage
import os

#Функция для определения чемпиона

def get_res():
    res1 = float((int(entry1.get())+int(entry2.get())+int(entry3.get())) / 3)
    res2 = float((int(entry5.get())+int(entry6.get())+int(entry7.get())) / 3)
    res3 = float((int(entry9.get())+int(entry10.get())+int(entry11.get())) / 3)
    max = 0
    if res1 > res2 and res1 > res3:
            max = "Андрей"
    else:
            if res2 > res1 and res2 > res3:
                max = "Егор"
            else:
                if res3 > res1 and res3 > res2:
                    max = "Миша"
    label11 = tk.Label(root, font='Aharoni 15')
    label11.place(x = 396, y = 70)
    label11.config(text = max) 

#Окно приложения

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 900
window_height = 550

res1 = 0
res2 = 0
res3 = 0

#пикча

canvas = tk.Canvas(root, height=800, width=1000)
image = Image.open("C:/Mironov/Block_ME_Drive.png")
photo = ImageTk.PhotoImage(image)
image = canvas.create_image(650,285, anchor='nw',image=photo)
canvas.grid(row=2,column=1)


x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

root.geometry(f"{window_width}x{window_height}+{x}+{y}")

#Надписи + лейблы для общего времени

label1 = tk.Label(root, text="Андрей", font='Aharoni')
label1.place(x = 30, y = 192)

label2 = tk.Label(root, text="Егор", font='Aharoni')
label2.place(x = 30, y = 232)

label3 = tk.Label(root, text="Миша", font='Aharoni')
label3.place(x = 30, y = 272)

label4 = tk.Label(root, text="Плавает (м/мин)", font='Aharoni 10')
label4.place(x = 115, y = 170)

label5 = tk.Label(root, text="Велосипед (км/ч)", font='Aharoni 10')
label5.place(x = 285, y = 170)

label6 = tk.Label(root, text="Бег (км/ч)", font='Aharoni 10')
label6.place(x = 480, y = 170)

label7 = tk.Label(root, text="Общее время(м)", font='Aharoni 10')
label7.place(x = 625, y = 170)

label8 = tk.Label(root)
label8.place(x=620, y=200)

label9 = tk.Label(root)
label9.place(x=620, y=240)

label10 = tk.Label(root)
label10.place(x=620, y=280)

label11 = tk.Label(root)
label11.place(x=370, y = 50) 



#Кнопка для определения чемпиона

button1 = tk.Button(root, text="Чемпион", bg='blue', fg='white', font='Aharoni 15', command= get_res)
button1.place(x=380, y = 100)

#Расчет общего времени

def button_click_input1():

    res1 = float((int(entry1.get())+int(entry2.get())+int(entry3.get())) / 3)
    res2 = float((int(entry5.get())+int(entry6.get())+int(entry7.get())) / 3)
    res3 = float((int(entry9.get())+int(entry10.get())+int(entry11.get())) / 3)


    label8 = tk.Label(root)
    label8.place(x=620, y=200)
    label8.config(text = res1)

    label9 = tk.Label(root)
    label9.place(x=620, y=240)
    label9.config(text = res2)

    label10 = tk.Label(root)
    label10.place(x=620, y=280)
    label10.config(text = res3) 


#Кнопка для расчета времени

button3 = tk.Button(root, text="Время", command=button_click_input1, font = "Aharoni 15", bg='blue', fg='white')
button3.place(x=380, y=330)

#Поля для ввода результатов участников

entry1 = tk.Entry(root)
entry1.place(x=110, y=200)


entry2 = tk.Entry(root)
entry2.place(x=280, y=200)

entry3 = tk.Entry(root)
entry3.place(x=450, y=200)


entry5 = tk.Entry(root)
entry5.place(x=110, y=240)

entry6 = tk.Entry(root)
entry6.place(x=280, y=240)

entry7 = tk.Entry(root)
entry7.place(x=450, y=240)


entry9 = tk.Entry(root)
entry9.place(x=110, y=280)

entry10 = tk.Entry(root)
entry10.place(x=280, y=280)

entry11 = tk.Entry(root)
entry11.place(x=450, y=280)


root.mainloop()