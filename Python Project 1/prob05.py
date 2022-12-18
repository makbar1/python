# Project Euler Prob 05
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

for i in range(10000, 30000000):
    x = 1
    for j in range(2, 21):
        if i % j == 0:
            x = x + 1
            if x == 19:
                print(i)
    