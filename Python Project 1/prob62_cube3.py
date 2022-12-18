import math

def permutation(lst):
     
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
    l = []
    for i in range(len(lst)):
        m = lst[i]
        remLst = lst[:i] + lst[i+1:]
        for p in permutation(remLst):
           l.append([m] + p)
    return l


def iscube(n):
    cuberoot=round(math.pow(n,1/3))
    if cuberoot**3 == n:
        return True
    else:
        return False

cubes = []

for i in range(41063625, 52063699):
#for i in range(41063625, 42063699):
    if iscube(i) == True:
        cubes.append(i)       

### when the number has a lot of zeros at the end
### the permutations look the same.

x = cubes[5]
print(x)
istr = str(x)
lst = list(istr)
ppd = permutation(lst)
# using list comprehension
# to remove duplicated 
# from list 
pp = []
[pp.append(x) for x in ppd if x not in pp]
cub = []
#for i in range(0, len(pp)):
for i in range(0, 7):
    ppi = "".join(pp[i])
    ppint = int(ppi)
    print(ppint, pp[i])

'''
#print(cubes)
print(len(cubes))
for i in range(0, len(cubes)):
    x = cubes[i]
    istr = str(x)
    lst = list(istr)
    pp = permutation(lst)
    print(len(pp))
    cub = []
    for i in range(0, len(pp)):
        ppi = "".join(pp[i])
        ppint = int(ppi)

        if iscube(ppint) == True:
            cub.append(ppint)
        #print(i, len(pp), cub, ppint, round(math.pow(ppint,1/3)))
        print(cub)

'''
