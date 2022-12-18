import time

time_start = time.time()

m=0
maxa =0
maxb =0
for a in range(1,4):
    for b in range(1,4):
        #m=max(m,sum([int(x) for x in str(a**b)]))
        m=max(m,a**b)

    
print(m)
print(10**10)
print("Time taken: ", str(time.time() - time_start))

