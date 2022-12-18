'''
Euler Problem 21
Amicable Pairs.
'''
import math
import time

time_start = time.time()

def divisors(n):
    ni = int(n/2)
    sum = 0
    for i in range(1, ni + 1):
        if n % i == 0:
            sum = sum + i
    #print(sum)
    return sum

suma = 0
for i in range(1, 10001):
    x = divisors(i)
    if divisors(x) == i:
        suma = suma + x + i
print(i, x, suma)


