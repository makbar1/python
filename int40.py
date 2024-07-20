import time
import math

#Original Amount
org = 137.2
x1 = 0.85

#New 
x1_17 = 0.83
x1_18 = 0.82


m = 1.0435

a = org * x1
b = org * m * x1
c = org * m * x1_17
d = org * m * x1_18

print(f"If 15 than current amount= {a:.2f}")
print(f"If 15 than new amount= {b:.2f}")
print(f"If 17 than new amount= {c:.2f}")
print(f"If 18 than new amount= {d:.2f}")

