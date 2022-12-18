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
					


def diviso(m,n):
	x = int(math.sqrt(n))
	sum = 0
	for i in range(1, x + 1):
		if n % i == 0:
			#sum = sum + 1
			if n/i == i:
			#	#print(i)
				sum = sum + 1
			else:
				#print(i, n/i)
				sum = sum + 2
	if sum > 490:
		print(m, n, sum)


def triangular(n):
	if n == 1:
		return 1
	elif n >= 2:
		x = 0	
		for i in range(1, n + 1):
			x = x + i
		return x

#divisors(28)
a = int(input("Enter range start: "))
b = int(input("Enter range end: "))
for y in range(a, b):
	#print(triangular(y))
	z = triangular(y)
	#divisors(z)
	#print(y, z, diviso(z))
	diviso(y,z)