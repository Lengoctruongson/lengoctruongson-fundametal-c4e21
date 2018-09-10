def print_hello():
    for i in range (3):
        print("Hello world")

def sum_2(a,b):
    print(a, '+', b, '=', a+b)

def draw_square(length, square_color):
    color(square_color)
    for i in range (4):
        forward(length)
        left(90)

from turtle import *
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
