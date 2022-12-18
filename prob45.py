import math

"""
Triangle Tn=n(n+1)/2
Pentagonal Pn=n(3n-1)/2
Hexagonal Hn=n(2n-10
"""


def tph(n):
	t = int((n*(n + 1))/2)
	p = int(n*(3*n -1)/2)
	h = int(((2 * n) -1))
	print(t, p , h)

def triang(n):
	t = int((n*(n + 1))/2)
	return(t)

def pent(n):
	p = int(n*(3*n -1)/2)
	return(p)

def hexa(n):
	h = int(n*(2*n - 1))
	return(h)


tr = []
pt = []
hx = []

for i in range(0, 300001):
	tr.insert(i, triang(i))
	pt.insert(i, pent(i))
	hx.insert(i, hexa(i))


y = int(0)
x = int(0)
for i in range(1, 300000):
	y = tr[i]
	for j in range(1, 300000):
		if y == int(pt[j]):
			for k in range(1, 300000):
				if y == int(hx[k]): 
					print(i, j, k, y)

#print(hexa(12), tr[275])
