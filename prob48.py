import math

x = 0
for i in range(1, 1001):
	x = x + i**i

print(x) 
y = str(x)
print(y[-10:])