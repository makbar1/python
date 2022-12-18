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

def con_p(n):
	x = 2
	sum = 3
	for d in range(3, n + 1):
		if is_prime_v3(d) == False:
			#print(n, x, sum)
			return
		x = x + 1
		sum = sum + d
		print(n, d, x, sum)

# ==== Test Function ====

primes = []
x = 0
y = 0
for n in range(1, 42):
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



x = int(0)
k = int(0)
for i in range(3, len(primes)):
	x = int(0)
	k = int(0)
	y = primes[i]
	z = int(0)
	for t in range(1, i):
		k = k + 1
		for j in range(k, i):
			x = primes[j] + x
			z = z + 1
			#if x == y:
			print(x, z, i)
	
	
	#print(x)


"""
t0 = time.time()
for n in range(1, 42):
	#print(n, is_prime_v2(n))
	con_p(n)
t1 = time.time()
print("Time Required = ", t1 - t0) """