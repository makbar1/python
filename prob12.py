import math

def divisors(n):
	if n == 1:
		return 1
	elif n == 2:
		return 3
	elif n >= 3:
		x = 0
		nh = int(n / 2)
		for i in range(1, n):
			if n % i == 0:
				#print(x)
				x = x + 1
				#print(n, i, x)
				if x > 4:
					print(n, i, x)
					


def triangular(n):
	if n == 1:
		return 1
	elif n >= 2:
		x = 0	
		for i in range(1, n + 1):
			x = x + i
		return x

divisors(76576500)
#for y in range(1, 10):
	#print(triangular(y))
#	z = triangular(y)
#	divisors(z)
	