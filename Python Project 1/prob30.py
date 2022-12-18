# Project Euler Prob 30
"""
 there are only three numbers that can be written as the sum of fourth powers of their digits:

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers 
of their digits.

"""
def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num % n == 0:
            return False
    return True

def topower5(num):
    x = str(num)
    l = len(x)
    y = 0
    for i in range(0, l):
        xi = int(x[i])
        y = xi**5 + y
    if y == num:
        #print(num)
        return True

ans = 0
for i in range(2, 9999999):
    if topower5(i) == True:
        ans = ans + i
print(ans)
