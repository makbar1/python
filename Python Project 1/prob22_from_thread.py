import time
def chsum(str):
    x=0
    for t in str:
        x+=ord(t)-64
    return x

t=time.time()
f=open("names.txt")
x=f.read()
print(x)
#
#x=x.replace('"','').split(",")
x=x.split(",")
print(x)
x.sort()
print(x)
sum=0
for n in range(0,len(x)):
    sum+=(n+1)*chsum(x[n])
print(sum)