import math
import time

# Euler Prob 145
# 
# For instance, 36 + 63 = 99 and 409 + 904 = 1313. 
# We will call such numbers reversible; so 36, 63, 409, and 904 are reversible

# 145b make code efficient

from functools import lru_cache

time_start = time.time()

@lru_cache
def flip(num):
    s = list(str(num))
    ls = len(s)
    # Have different loops for odd and even digits
    if ls % 2 == 0:
        a = ls
        i = 0
        b = ls
        sr = []
        for i in range(0,ls):
            sr.append(s[b-1])
            b = b -1
        # make it into a single integer
        x = int("".join(sr))
        return x
    else:
        a = ls + 1
        i = 0
        b = ls
        sr = []
        for i in range(0,ls):
            sr.append(s[b-1])
            #print(b,sr[i])
            b = b -1
        # make it into a single integer
        x = int("".join(sr))
        return x

def checkodd(num):
    s = list(str(num))
    ls = len(s)
    #for i in range(0, ls):
    for i in s:
        if int(i) % 2 == 0:
            return False
            break
    return True

reversable = []
rev=0
for num in range(1, 1000001):
    # Ignore numbers ending in 0 e.g reverse of 50 is 05 
        xp = flip(num)
        x = xp + num
        if x % 2 != 0 and num % 10 != 0:
            if checkodd(x) == True:
                #reversable.append(num)
                rev = rev + 1
                #reversable.append(xp)
                #print("Reversible", num, x)

xr = sorted(set(reversable))
#print(len(xr))
#print(len(xr))
print(rev)

print("Time taken: ", str(time.time() - time_start))