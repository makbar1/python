import math
import time

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
for n in range(997, 1000):
    if is_prime_v3(n) == True:
        x=[int(a) for a in str(n)]
        for a in range(0, len(x)-1):
            del x[a]
            #convert list to a single number
            #num = int(''.join(map(str,numList)))
            y = int(''.join(map(str,x)))
            print(y)