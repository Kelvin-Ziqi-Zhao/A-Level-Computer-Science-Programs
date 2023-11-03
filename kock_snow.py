from turtle import *
n=3

def snow(Level,Length):

    if Level > 1:
        snow(Level-1,Length)
        left(60)
        snow(Level-1,Length)
        right(120)
        snow(Level-1,Length)
        left(60)
        snow(Level-1,Length)
    else:
        forward(Length/3)
    

speed(0)
penup()
goto(-100,50)
pendown()
for i in range(3):
    snow(n,200/n)
    right(120)
mainloop()

