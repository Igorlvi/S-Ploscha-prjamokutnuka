# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

import turtle
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from tkinter import *
import tkinter as tk

print("Розрахуйте S площу прямокутника")
print("Введіть розміри сторін прямокутника см :")
a = float(input("a довжина ? = "))
b = float(input("b ширина ? = "))
print ("S=a*b")
print("Площа = %.2f" % (a * b))
print ("Поки Ви звіряєте свій розв'язок, дана програма побудує Вам Ваш прямокутник ")
print("У графічному сервісі\n1-Turtle\n2-Matplotlib\n3-Tkinter")
figure = input("Оберіть графічний сервіс : ")
if figure == '1':
    turtle.forward(a*37)
    turtle.left(90)
    turtle.forward(b*37)
    turtle.left(90)
    turtle.forward(a*37)
    turtle.left(90)
    turtle.forward(b*37)
    turtle.hideturtle()
    style = ('Courier', 15, 'italic')
    turtle.write(" Turtle накреслила\n Вам ваш прямокутник", font=style, align='right')
    turtle.title('Ваш прямокутник')

elif figure == '2':
    fig, ax = plt.subplots()
    square = patches.Rectangle((0, 0), a, b, edgecolor='grey', facecolor='none')
    ax.add_patch(square)
    plt.xlim(-1, a+2)
    plt.ylim(-1, b+2)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.title('Ваш прямокутник накреслений на координатній сітці в Matplotlib')
    plt.show()

elif figure == '3':
    win = tk.Tk()
    win.title("Ваш прямокутник накреслений в Tkinter")
    canvas = Canvas(width=a*50+50, height=b*50+50, bg='white')  
    canvas.pack(expand=YES, fill=BOTH)                
    canvas.create_rectangle(50, 50, a*50, b*50)
    mainloop()

else:
    print("Помилка введення ???")    
    

  
