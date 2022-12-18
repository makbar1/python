import math
import time
from functools import lru_cache

#@lru_cache(maxsize=100000)

def is_prime_v3(n):
    """ Return True if n is a prime number. False of not"""
    if n == 1:
        return False

    # If it is even and not 2, then it is not prime
    if n == 2:
        return True

    if n > 2 and n % 2 == 0:
        return False
    
    max_divisor = math.floor(math.sqrt(n))
    for d in range(3, 1 + max_divisor, 2):
        if n % d == 0:
            return False
    return True 

Start_Time = time.time()    

nth = 1
# Fine the Prime Factors of a Number
for i in range(1, 1000000):
    if i % 2 != 0:
        if is_prime_v3(i) != False:
            nth = nth + 1
            if nth == 10001:
                print(nth, i)
                break
    




End_Time = time.time()
#
print(End_Time - Start_Time)