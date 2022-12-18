# Project Euler Prob 66
"""
 Consider quadratic Diophantine equations of the form:

 x^2 - Dy^2 = 1
 Find the value of D ≤ 1000 in minimal solutions of x for which 
 the largest value of x is obtained.

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
xmax = 0
for D in range(1, 1000):
    for x in range(1, 1000):
        for y in range(1, 1000):
            E = x**2 - (D*y**2)
            if E == 1:
                if x > xmax:
                    xmax = x
                #print("x=",x,"y=",y, "is a solution for D=", D)
print(xmax)
