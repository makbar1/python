'''
Euler Problem 206
Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.
'''
import math
import time

time_start = time.time()

a = 1929374254627488900
print(a // 10000000000 % 10)
#for i in range(1120000000, 1420000005): 
for i in range(1120000000, 1420000005, 10):
    x = i**2
    if x // 100 % 10 == 9 and x // 10000 % 10 ==8 and x // 1000000 % 10 == 7 \
    and x // 100000000 % 10 == 6 and x // 10000000000 % 10 == 5 \
        and x // 1000000000000 % 10 == 4 and x // 100000000000000 % 10 == 3 \
            and x // 10000000000000000 % 10 == 2:
        print(i,x)
        #break

print("Time taken: ", str(time.time() - time_start))