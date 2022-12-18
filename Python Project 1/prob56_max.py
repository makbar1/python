# Euler Prob 56 using max

import time

time_start = time.time()

m=0
maxa =0
maxb =0
for a in range(1,101):
    for b in range(1,101):
        m=max(m,sum([int(x) for x in str(a**b)]))

    
print(m)
print("Time taken: ", str(time.time() - time_start))

