'''
Euler Prob 80 - 
if the square root of a natural number is not an integer, then it is irrational.

'''
import math
import time
from decimal import *
getcontext().prec = 100

time_start = time.time()

for i in range (1, 5):
    num = i ** 0.5
    if (num ** 2) != i:
        print("Square root of",i,"is irrational")
        print(Decimal(num))
'''
    if isinstance(num, int) != True:
        print("Square root of",i,"is irrational")
'''
