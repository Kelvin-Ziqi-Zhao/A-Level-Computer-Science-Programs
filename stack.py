

def InitialiseStack(Size):
    global Stack,StackMaxSize,StackTopPointer,Null
    Stack = []
    Null = -1
    StackTopPointer = Null
    StackMaxSize = Size
    for i in range(Size):
        Stack.append("")

def Push(NewItem):
    global StackMaxSize, StackTopPointer
    if StackTopPointer < StackMaxSize:
        StackTopPointer += 1
        Stack[StackTopPointer] = NewItem
        return True
    else:
        return False
    
def Pop():
    global StackTopPointer
    Item = Stack[StackTopPointer]
    if StackTopPointer > Null:
        Stack[StackTopPointer] = ""
        StackTopPointer -= 1
        return(Item)
        
    else:
        return(False)


InitialiseStack(10)
Push("A")
Push("B")
print(Stack)
print(Pop(),StackTopPointer)
print(Stack)
print(Pop(),StackTopPointer)
print(Stack)