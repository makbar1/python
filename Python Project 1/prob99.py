# Prob 99 
# Read lines from a file and write 5 letter words

import math
import time

f1 = open("base_exp.txt", "r")
f2 = open("doc2.txt", "w")
greatest=0
r=0
i=1
line=0
l = f1.readline()
while l:
    x = str(l)
    #x=x.replace('"','').split(",")
    x=x.split(",")
    x0=int(x[0])
    x1=int(x[1])
    r=x1*math.log(x0,10)
    #print(i,x0,x1,r,type(r))
    #time.sleep(1)
    if r > greatest:
        greatest=r
        gx0=x0
        gx1=x1
        line=i
    i+=1
    #if len(x) == 6:
        #f2.write(l)
        #print(l, len(x))
    l = f1.readline()
f1.close()
f2.close()
print("Line:",line,"===>",gx0,"**",gx1," has the greatest numerical value")

## Answer was correct

#print(13846**72521)
# Python code to demonstrate the working of
# log(a,Base)
# Natural log of 14
# print (math.log(14))
# Log base 5 of 14
# print(math.log(14,5))
#519432**525806
