Stack = [NewItem]
StackTopPointer = len(Stack)

def Push(NewItem):
    if StackTopPointer < len(Stack):
        StackTopPointer += StackTopPointer
        StackTopPointer = NewItem
        return True
    else:
        return False