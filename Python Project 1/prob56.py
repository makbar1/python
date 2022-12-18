# Euler Prob 56

import time

time_start = time.time()
ans = 0
maxsum = 0
maxa = 0
maxb = 0
for a in range(1, 101):
    for b in range(1, 101):
        x = a**b
        xs = str(x)
        xl = len(xs)
        sum = 0
        for i in range(0, xl):
            sum = sum + int(xs[i])
            if sum > maxsum:
                maxsum = sum
                maxa = a
                maxb = b
print(maxa,maxb,maxsum, maxa**maxb)

print("Time taken: ", str(time.time() - time_start))
