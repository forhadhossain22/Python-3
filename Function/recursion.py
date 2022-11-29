
def abc(n):
	if (n == 0):
		return 1
	return n * abc(n-1)
print(abc(3))
