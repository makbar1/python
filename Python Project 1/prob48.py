# Project Euler Prob 48
# 
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

ans = 0
for i in range(1, 1001):
    ans = ans + i**i

print(str(ans))
print(str(ans)[-10:])