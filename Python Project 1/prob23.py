# Project Euler Prob 23
# https://projecteuler.net/problem=1
# 
# Find the sum of all the positive integers which 
# cannot be written as the sum of two abundant numbers.
# 

import math
def isperfect(n):
    x = 0
    p = math.ceil(n/2)
    for i in range (1, p + 1 ):
        if n % i == 0:
            x = x + i
            print(i)
    print(x)


isperfect(12)