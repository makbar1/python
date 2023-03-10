import time
import math

def is_prime_v1(n):
    """Return true if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False  # 1 is not prime
    if n == 2:
        return True # 2 is a prime

    max_divisor = int(math.floor(math.sqrt(n)))

    #for d in range(2, n):
    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

t0=time.time()
Largest_p=2
for n in range(1,10000):
    #print(n, is_prime_v1(n))
    #is_prime_v1(n)
    if is_prime_v1(n) == True:
        Largest_p=n
        
print("Largest Prime of n is :", Largest_p)
t1=time.time()
print("Time taken:",t1-t0)