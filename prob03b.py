import time
import math

def is_prime_v1(n):
    """Return true if 'n' is a prime number. False otherwise"""
    if n == 1:
        return False  # 1 is not prime
    if n == 2:
        return True # 2 is a prime
    if n > 2 and n % 2 ==0:
        return False

    max_divisor = int(math.floor(math.sqrt(n)))

    #for d in range(2, n):
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True

t0=time.time()
Largest_p=2
#max = 600851475143
max = 781295
for n in range(1, max + 1):
    #print(n, is_prime_v1(n))
    #is_prime_v1(n)
    if is_prime_v1(n) == True:
        if max % n == 0:
            print(n)
            Largest_p=n
        
print("Largest Prime Factor of ",max, "is :", Largest_p)
t1=time.time()
print("Time taken:",t1-t0)