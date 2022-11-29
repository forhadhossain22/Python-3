myList = [2,3,4,5,6,7]
def isEven(x):
    if(x%2) == 0:
        return True
    else:
        return False
newList = filter(isEven, myList)
print(list(newList))