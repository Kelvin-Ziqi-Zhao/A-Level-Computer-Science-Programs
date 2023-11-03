from turtle import *

def BinaryTreeDraw(Level,Length):
    if Level == 1:
        fd(Length)
        fd(-Length)
    else:
        fd(Length)  
        right(30)
        BinaryTreeDraw(Level-1,Length/3)
        left(60)
        BinaryTreeDraw(Level-1,Length/3)
        right(30)
        fd(-Length)  


        

BinaryTreeDraw(2,100)


mainloop()
