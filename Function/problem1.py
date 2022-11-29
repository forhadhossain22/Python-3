print('please input three integers')
a,b,c = map(int, input().split())

if a >= b and c >= c:
    greatest = a
elif b >= a and b >= c:
    greatest = b
else: greatest = c

print(greatest)