import math

def primefactors(n):
    if n % 2 == 0:
        print(2)
        
    for i in range(3,int(math.sqrt(n))+1, 2):
        if n % i == 0:
            print (i)
    

for i in range(3,int(math.sqrt(100)), 2 ):
    print(i)
#primefactors(21)
