#Title: Josephus problem in CS class
#Ref: https://en.wikipedia.org/wiki/Josephus_problem
#Author: Kelvin Zhao

#Data Source
DataSource = ["A","B","C","D","E","F","G","H","I","J"]
#DataSource = ["Kelly","Lucas","Paul","Clara","Justin","Jaxton","Ivan","Kelvin","Jack","Kalie"]
#Data Structure
class ListNode:
    def __init__(self,data,pointer):
        self.Data = data
        self.Pointer = pointer

#Check Functions
def CheckList():
    print("Check of List")
    print("StartPointer = ",StartPointer)
    print("FreePointer = ",FreePointer)
    print("Index   ","Data     ","Pointer")
    print("------   -------   -------")
    for Index in range(0,len(List)):
        print("{:<9}{:<10}{:<10}".format(Index,List[Index].Data,List[Index].Pointer))
def CheckRela():
    print("Check of List relationship")
    Pointer = StartPointer
    print("StartPointer ",end="")
    while Pointer != Null:
        print("=> {}:{}".format(List[Pointer].Data,List[Pointer].Pointer),end=" ")
        Pointer = List[Pointer].Pointer
    print("")
#Initialise Function
def Initialise():
    global Null
    Null = -1
    global StartPointer
    StartPointer = Null
    global FreePointer
    FreePointer = 0
    global List
    List = []
def InitialiseList(Length):
    global StartPointer
    for i in range(0,Length-1):
        List.append(ListNode("",i+1))
    if Length > 0:
        List.append(ListNode("",Null))
#Method Function
def InsertNode(PreviousNodePointer,NewData):
    global FreePointer, StartPointer
    NextNodePointer = List[PreviousNodePointer].Pointer
    #Prepare the node ready to insert, change FreePointer
    NewNodePointer = FreePointer
    List[NewNodePointer].Data = NewData
    FreePointer = List[NewNodePointer].Pointer
    #Check if the node will insert to the start of list
    if NextNodePointer == StartPointer:
        #Connect all node after that node
        List[NewNodePointer].Pointer = StartPointer
        StartPointer = NewNodePointer
    List[PreviousNodePointer].Pointer = NewNodePointer
    List[NewNodePointer].Pointer = NextNodePointer
    return NewNodePointer
def DeleteNode(PreviousNodePointer):
    global StartPointer,FreePointer
    TargetPointer = List[PreviousNodePointer].Pointer
    if PreviousNodePointer == Null:
        StartPointer = List[TargetPointer].Pointer
    List[PreviousNodePointer].Pointer = List[TargetPointer].Pointer
    #release node to FreePointer
    List[TargetPointer].Data = ""
    List[TargetPointer].Pointer = FreePointer
    FreePointer = TargetPointer

#Load Data
def SortLoad():
    global StartPointer, FreePointer
    Pointer = InsertNode(Null,DataSource[0])
    for Index in range(len(DataSource)-1):
        Pointer = StartPointer
        PreviousNodePointer = Null
        while List[Pointer].Data < DataSource[Index+1] and Pointer != Null:
            PreviousNodePointer = Pointer
            Pointer = List[Pointer].Pointer
        InsertNode(PreviousNodePointer,DataSource[Index+1])


Initialise()
InitialiseList(11)
CheckList()
SortLoad()

CheckList()
CheckRela()