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
	return True


# ==== Test Function ====

t0 = time.time()
maxprime = 1
for n in range(1, 10000000):
        #print(n, is_prime_v3(n))
    if is_prime_v3(n) == True:
        maxprime=n
t1 = time.time()
print("Time Required = ", t1 - t0)
print(maxprime)