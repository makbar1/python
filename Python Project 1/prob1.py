# Project Euler Prob 1
# https://projecteuler.net/problem=1
# Find the sum of all multiples of 3 or 5 below 1000
#

x = 0

for i in range(1000):
    if i % 3 == 0 or i % 5 == 0:
        x += i

print(x)