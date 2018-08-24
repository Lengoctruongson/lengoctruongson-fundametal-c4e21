colors = ['red', 'blue', 'brown', 'yellow', 'grey']

from turtle import *

for i in colors:

    color(i)

    begin_fill()
    left(90)
    forward(100)
    right(90)
    forward(50)
    right(90)
    forward(100)
    left(90)
    end_fill()

mainloop()