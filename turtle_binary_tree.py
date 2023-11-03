from turtle import *

def BinaryTreeDraw(Level,Length):
    if Level == 1:
        fd(Length)
        fd(-Length)
    else:
        fd(Length)  
        right(30)
        BinaryTreeDraw(Level-1,Length/1.5)
        left(60)
        BinaryTreeDraw(Level-1,Length/1.5)
        right(30)
        fd(-Length)  


        

BinaryTreeDraw(3,100)


mainloop()
