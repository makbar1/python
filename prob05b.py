import math
print(math.lcm(*range(1, 21)))
x=1
for i in range(1,21):
    x = x * i
print(x, math.sqrt(x))
