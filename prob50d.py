import time
import math
          
def is_prime_v3(n):
	"""Return true if 'n' is a prime number. False otherwise"""
	if n == 1:
		return False
	if n == 2:
		return True
	if n > 2 and n % 2 == 0:
		return False

	max_divisor = math.floor(math.sqrt(n))
	for d in range(3, 1 + max_divisor, 2):
		if n % d == 0:
			return False
		#return True
	return(n)


# ==== Test Function ====

primes = []
x = 0
y = 0
for n in range(1, 10000):
	if is_prime_v3(n) != False:
		#print(is_prime_v3(n))
		#y = y + n
		primes.insert(x, n)
		x = x + 1
	#if y == n:
		#print(n, x, primes)
	#print(n, x, primes)

print(primes)
print(len(primes))

#print(primes[161])
for t in range(0, len(primes)):
	x = 0
	for i in range(t, len(primes)):
		x = primes[i] + x
#		print(t, x)
		#if x == primes[161]:
		if x == primes[999]:
			print(x, t, i - 2)
	t = t + 1

u = 0
for b in range(3, 24):
	u = u + primes[b]
	print(b, u)
	
