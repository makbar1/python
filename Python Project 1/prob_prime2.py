import math
import time

def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num % n == 0:
            return False
    return True

for i in range(1, 1000):
    print(i, isprime(i))

