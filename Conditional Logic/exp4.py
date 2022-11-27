#nested if

a = int(input())
if a < 10:
    if(a%2)==0:
        print('les,yes')
    else:
        print('les,no')

else:
    if (a%3)==0:
        print('greater,yes')
    else:
        print('greater,no')