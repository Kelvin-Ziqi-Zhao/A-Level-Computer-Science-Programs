#Author: Kelvin Zhao 

#Data Structure
class TreeNode:
    def __init__ (self,LeftPointer,Data,RightPointer):
            self.LeftPointer = LeftPointer
            self.Data = Data
            self.RgihtPointer = RightPointer    

#Check Functions

#Initialise Function
def Initialise(Length):
    #Define Variables
    global Null
    Null = -1
    global RootPointer
    RootPointer = Null
    global FreePointer
    FreePointer = 0
    global Tree
    Tree = []
    #Fill in the list
    for i in range(0,Length-1):
        Tree.append(TreeNode(i+1,"",Null))
    if Length > 0:
        Tree.append(TreeNode(Null,"",Null))
#Method Function

#Main Thread
