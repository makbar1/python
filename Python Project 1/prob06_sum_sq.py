# Project Euler Prob 06
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


x = 0
y = 0
for i in range(1, 101):
    x = x + i**2
    y = y + i
print(x, y**2, y**2 - x)