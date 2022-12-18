import math

def diviso(n):
	x = int(math.sqrt(n))
	sum = 0
	for i in range(1, x + 1):
		if n % i == 0:
			if n/i == i:
				print(i)
				sum = int(sum + i)
			else:
				print(i, n/i)
				sum = int(sum + i + n/i)
	print(sum)

diviso(10000000)