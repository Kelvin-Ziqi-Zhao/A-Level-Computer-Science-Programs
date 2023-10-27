Stack = []
StackTopPointer = 0

def InitialiseStack(Size):
    for i in range(Size):
        Stack.append(0)
        global StackMaxSize
        StackMaxSize = Size
def Push(NewItem):
    global StackMaxSize, StackTopPointer
    if StackTopPointer < StackMaxSize:
        Stack[StackTopPointer] = NewItem
        StackTopPointer += 1
        return True
    else:
        return False

InitialiseStack(10)
Push("A")
Push("B")
print(Stack)