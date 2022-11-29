#variable length argument

def add(*args):
    tmp = 0
    for number in args:
        tmp = tmp + number
    return tmp
temp = add(1,2,22,12,17,21,98,3)
print(temp)