#Author: Kelvin Zhao 

#Data Source
DataSource = ["F","C","S","B","E","R","D"]
#Data Structure
class TreeNode:
    def __init__ (self,LeftPointer,Data,RightPointer):
            self.LeftPointer = LeftPointer
            self.Data = Data
            self.RightPointer = RightPointer    

#Check Functions
def CheckTree():
    print("Tree Information:")
    for Index in range(0,len(Tree)):
         print(Tree[Index].LeftPointer,Tree[Index].Data,Tree[Index].RightPointer)

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
def InsertNode(DataInsert):
    global FreePointer
    #Prepare Node
    ThisNodePointer = FreePointer
    Tree[FreePointer].Data = DataInsert
    Tree[ThisNodePointer].LeftPointer = Null
    Tree[ThisNodePointer].RgihtPointer = Null
    FreePointer = Tree[ThisNodePointer].LeftPointer
    #Insert
    ThisNodePointer = RootPointer
    while ThisNodePointer != Null:
        PreviousNodePointer = ThisNodePointer
        if Tree[ThisNodePointer].Data > DataInsert:
            TurnLeft = True
            ThisNodePointer = Tree[ThisNodePointer].LeftPointer
        else:
            TurnLeft = False
            ThisNodePointer = Tree[ThisNodePointer].LeftPointer   

#Main Thread
Initialise(6)
CheckTree()
InsertNode("A")
CheckTree()