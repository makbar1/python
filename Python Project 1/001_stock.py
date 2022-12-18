import math
import time

t1=10000
t2=5000
t3=5000
t4=3000

p1=28.17
p2=27.6
p3=27.09
p4=25.13

total_shares=(t1/p1)+(t2/p2)+(t3/p3)+(t4/p4)
current_price = 28.17

Total = total_shares*current_price

print("Shares = %2.7f Total = %5.2f" % (total_shares,Total))
