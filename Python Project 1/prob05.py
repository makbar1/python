# Project Euler Prob 05
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

for i in range(232000000, 232792569):
    x = 1
    for j in range(2, 21):
        if i % j == 0:
            x = x + 1
        exit
    if x == 20:
        print(i)

    