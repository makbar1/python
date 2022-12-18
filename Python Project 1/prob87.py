import math
import time

def isprime(num):
    for n in range(2,int(num**1/2)+1):
        if num % n == 0:
            return False
    return True

primes=[]
for i in range(2, 11990):
    if isprime(i) == True:
        primes.append(i)
#print(len(primes),primes[139])
print(len(primes),primes[len(primes)-2])
#print(50000000**0.5)

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

         