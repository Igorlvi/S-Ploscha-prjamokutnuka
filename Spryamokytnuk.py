# Автор Ігор Хруневич
# Цю міні-програму створено, щоб зацікавити дітей програмуванням
# Користуйтесь, вивчайте, досліджуйте, змінюйте - експериментуйте

import turtle
import matplotlib.pyplot as plt
import matplotlib.patches as patches

print("Розрахуйте S площу прямокутника")
print("Введіть розміри сторін прямокутника см :")
a = float(input("a довжина ? = "))
b = float(input("b ширина ? = "))
print ("S=a*b")
print("Площа = %.2f" % (a * b))
print ("Поки Ви звіряєте свій розв'язок із розв'язком даної програми, черепашка та matplotlib накреслили Вам ваш прямокутник . Знайдіть їх у себе на моніторі.")
turtle.forward(a*37)
turtle.left(90)
turtle.forward(b*37)
turtle.left(90)
turtle.forward(a*37)
turtle.left(90)
turtle.forward(b*37)
turtle.hideturtle()
#Smatplotlib
fig, ax = plt.subplots()
square = patches.Rectangle((0, 0), a, b, edgecolor='grey', facecolor='none')
ax.add_patch(square)
plt.xlim(-1, a+2)
plt.ylim(-1, b+2)
plt.gca().set_aspect('equal', adjustable='box')
plt.title('Ваш прямокутник накреслений на координатній сітці')
plt.show()
    
    

  
