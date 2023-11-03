from turtle import *

def snow(Level,Length):
    
    forward(Length/3)
    left(60)
    forward(Length/3)
    right(120)
    forward(Length/3)
    left(60)
    forward(Length/3)
    home()


snow(1,100)
mainloop()

