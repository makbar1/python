### Euler problem 125 understanding
'''
need the sum of the squares of a continuous sequence
e.g. 3^2+4^2+5^2
The loop below will get the sequence for all numbers in a range
e.g 5
1^2+2^2=5
1^2+2^2+3^2=14
.
.
5^2+6^2=61

'''

x = []
a = 7
print("   a i j")
for i in range(1, a):
    tempnum = i**2
    for j in range(i+1, a):
        tempnum = tempnum + j**2
        print("a=",a,i,j,tempnum)
        