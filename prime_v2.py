import time
import math
          
def is_prime_v2(n):
    """Return true if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True


# ==== Test Function ====

t0 = time.time()
for n in range(1, 100000):
	#print(n, is_prime_v2(n))
	is_prime_v2(n)
t1 = time.time()
print("Time Required = ", t1 - t0)