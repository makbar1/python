'''
Euler Problem 206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
'''
import math
import time

time_start = time.time()

#for i in range(1120000000, 1420000005): 
for i in range(1120000000, 1420000005, 10):
    x = i**2
    xs = str(x)
    #print(i, x, xs[2], xs[4], xs[6])
    if xs[2] == '2' and xs[4] == '3' and xs[6] == '4' and xs[8] == '5' \
        and xs[10] == '6' and xs[12] == '7' and xs[14] == '8' and xs[16] =='9' \
            and xs[18] =='0':
        print(i,x)
        break

print("Time taken: ", str(time.time() - time_start))

