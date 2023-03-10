import time
import math
"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""
def is_palindrome(num):
    a = str(num)
    reverse = a[::-1]

    if a == reverse:
        return num
    
max = 0  
maxi = 0 
maxj = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        a = str(i * j)
        r = a[::-1]
        if a == r:
            if int(a) > max:
                max = int(a)
                maxi = i
                maxj = j
print(maxi, maxj, max)