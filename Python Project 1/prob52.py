# Euler problem 52

import time

time_start = time.time()

for i in range(1000, 1000000):
	x2 = sorted([int(a) for a in str(2*i)])
	x3 = sorted([int(a) for a in str(3*i)])
	x4 = sorted([int(a) for a in str(4*i)])
	x5 = sorted([int(a) for a in str(5*i)])
	x6 = sorted([int(a) for a in str(6*i)])
#	x2.sort(key=int)
#	x3.sort(key=int)
#	x4.sort(key=int)
#	x5.sort(key=int)
#	x6.sort(key=int)
	if x2 == x3 == x4 == x5 == x6:
		print(i, x2)
		break

print("Time taken: ", str(time.time() - time_start))

# Answer was correct

'''
x = 891*30
z = 27630


y = [int(i) for i in str(x)]
y2 = [int(i) for i in str(z)]

y.sort(key=int)
y2.sort(key=int)
if y == y2:
    	print(y)

'''

