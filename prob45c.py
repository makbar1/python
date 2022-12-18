import math

"""
Triangle Tn=n(n+1)/2
Pentagonal Pn=n(3n-1)/2
Hexagonal Hn=n(2n-10
"""


def is_pentagonal(p):
    """function to check if the
    given number is pentagonal"""
    if (1+(24*p+1)**0.5) % 6 == 0:
        return True
    return False


def is_hexagonal(h):
    """function to check if the
    given number is hexagonal"""
    if (1+(8*h+1)**0.5) % 4 == 0:
        return True
    return False


def tph(n):
	t = int((n*(n + 1))/2)
	p = int(n*(3*n -1)/2)
	h = int(((2 * n) -1))
	print(t, p , h)

# iterator start after 100
i = 100

"""
The following loop 1) calculates the Triangle then 2) checks to see if that number is pent AND Hex
"""

while True:
    triangle = i*(i+1)/2
    if is_pentagonal(triangle) and is_hexagonal(triangle):
        print(triangle)
        #break
    i += 1
