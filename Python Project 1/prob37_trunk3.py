
import math
import time
from functools import lru_cache

@lru_cache(maxsize=1000)

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
primes = []   
for n in range(11, 37989, 2):
    if is_prime_v3(n) == True:
        primes.append(n)

print(primes)
print(len(primes), type(primes))
'''
        #x=[int(a) for a in str(n)]
        x=str(n)
        sum = 0
        for a in range(0, len(x)):
            y=int(x[0:len(x)-a])
            yr=int(x[-len(x)+a:])
            if is_prime_v3(y) == False or is_prime_v3(yr) == False:
                break
            else:
                sum = sum + 1
        if sum == len(x):
            print(n)
'''

End_Time = time.time()
print(End_Time - Start_Time)