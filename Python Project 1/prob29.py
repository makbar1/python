# Project Euler Prob 29
# https://projecteuler.net/problem=1
# 
# How many distinct terms are in the sequence generated 
# by a^b for 2 ≤ a ≤ 100 and 2 ≤ b ≤ 100?
# 
x = 0
dlist = []

for a in range(2, 101):
    for b in range(2, 101):
        ab = a ** b
        if ab not in dlist:
            dlist.append(ab)
        x = x + 1
        #print(x, ab)

print(x, len(dlist))