import math
import time
from functools import lru_cache

@lru_cache(maxsize=1000)

def is_prime(n):
    """ Return True if n is a prime number. False of not"""
    if n == 1:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def is_prime_v2(n):
    """ Return True if n is a prime number. False of not"""
    if n == 1:
        return False

    max_divisor = math.floor(math.sqrt(n))

    for d in range(2, 1 + max_divisor):
        if n % d == 0:
            return False
    return True

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

#Start_Time = time.time()    

#print(prime_fac(16))

num = 600851475143


#print(is_prime(9))

# Fine the Prime Factors of a Number
for i in range(1, num, 2):
    if num % i == 0:
        if is_prime_v3(i) != False:
            print(i)
    




#End_Time = time.time()
#
# print(End_Time - Start_Time)
