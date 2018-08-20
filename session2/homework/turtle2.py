from turtle import *
for i in range(3,7):
    if i % 2 == 1:
        color("blue")
    else:
        color("red")
    r = 180 - 180 * (i-2) / i
    for j in range (i):
        left(r)
        forward(100)
mainloop()