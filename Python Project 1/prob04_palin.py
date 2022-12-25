import time
import math

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

x = str(10 * 12)
print(x,x[::-1])


