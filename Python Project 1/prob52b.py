import time
time_start = time.time()

def f(n):
    return sorted([int(n) for n in str(n)])

for n in range(1000, 1000000):
    if f(n*2)==f(n*3)==f(n*4)==f(n*5)==f(n*6):
        print(n)
        break

'''
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
'''

print("Time taken: ", str(time.time() - time_start))