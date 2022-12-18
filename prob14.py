import math

def chain(n):
	x = n
	chain = 1
	while x != 1:
		if x % 2 == 0:
			x = int(x/2)
			chain = chain + 1
		else:
			x = int((3 * x) + 1)
			chain = chain + 1
	return(chain)

for a in range(3, 1000001):
	b = chain(a)
	if b > 500:
		print(a, b)
		
	