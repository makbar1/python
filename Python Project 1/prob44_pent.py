import math
import time

# Euler Prob 44
# 
# Pn=n(3n−1)/2.

def mkpent(num):
    pent = int(num * (3 * num -1)/2)
    return pent

pentlist=[]
for i in range(1, 3000):
    x = mkpent(i)
    pentlist.append(x)

lenpent=len(pentlist)
print(7042750-1560090)
for i in range(0, len(pentlist)-1):
    for j in range(0, lenpent-1):
        p = pentlist[i]
        pp = pentlist[j+1]
        #print(p, pp, p + pp)
        if (p + pp) in pentlist and abs(p-pp) in pentlist:
        #if (p + pp) in pentlist:
            print(p, pp)

    


'''
sqp=[]
for i in primes:
    for j in primes:
        for k in primes:
            num = i**2 + j**3 + k**4
            if num <= 50000000:
                sqp.append(num)
            ## if the number is greater than 50million exit loop - save time
            else:
                break

print(len(sqp))

# The above list will have duplicates e.g 2x3 and 3x2
# Remove duplicates

uniq_list = list(set(sqp))
print(len(uniq_list))

## Answer was correct

al = [1,2,2,3,3,4,5]
print(al)
print(set(al),type(set(al)))
'''
