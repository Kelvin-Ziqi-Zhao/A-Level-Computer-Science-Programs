from turtle import *

def BinaryTreeDraw(Level,Length):

    forward(Length)  
    backward(Length)  
    if Level > 1:
        right(30)
        BinaryTreeDraw(Level-1,Length/3)
        left(60)
        BinaryTreeDraw(Level-1,Length/3)
        

        

BinaryTreeDraw(4,100)


mainloop()
