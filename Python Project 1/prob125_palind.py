import math
import time

# Euler Prob 125
# 
# Palindrome

def ispalind(num):
    s = list(str(num))
    ls = len(s)
    # Have different loops for odd and even digits
    if ls % 2 == 0:
        a = int(len(s)/2)
        i = 0
        b = ls
        while i <a:
            #print(s[i],s[b-1])
            if s[i] != s[b-1]:
                break
            i = i + 1
            b = b -1
        if i == b:
            return True
    else:
        a = int(len(s)/2+1)
        i = 0
        b = ls
        while i <a:
            if s[i] != s[b-1]:
                break
            i = i + 1
            b = b -1
        if i == b + 1:
            return True

#print(ispalind(1221))
#x = int(595**0.5)
a = 0
b = 1

palindromes = []
for i in range(1, 100000001):
    if ispalind(i) == True:
        palindromes.append(i)
palins=sorted(set(palindromes))

a = 1000000
b = 1
j = 0
c = 1
x = []
for i in range(1, a):
    tempnum = i**2
    for j in range(i+1, a):
        tempnum = tempnum + j**2
        if tempnum > 100000000:
            #print(tempnum)
            break
        if tempnum in palindromes:
            #print(tempnum)
            x.append(tempnum)


#print(x,sum(x))
y = sorted(set(x))
print(sum(y),len(palins), len(y))

###  Answer was correct 2906969179