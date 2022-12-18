import math
import time
from prob_prime2 import isprime

primes=[]
for i in range(1, 10001):
    if isprime(i) == True:
        primes.append(i)

print(len(primes))

x = 0
x10 = []
for j in range(0, len(primes)-1):
    x = x + primes[j]
    if x == 10:
        x10.append(j)
        
