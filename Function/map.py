myList = [2,3,4,5,6,7,8]
def square(x):
    return x*x
newList = map(square, myList)
print(newList)
print(list(newList))