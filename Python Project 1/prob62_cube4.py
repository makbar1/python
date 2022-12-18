import math
import time

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

#for i in range(41063625, 52063699):
t0 = time.time()
for i in range(127035954683, 127035954684):
    if iscube(i) == True:
        cubes.append(i)    
t1 = time.time()
print(t1-t0)   

print(len(cubes))

### when the number has a lot of zeros at the end
### the permutations look the same. Therefore need to
### remove duplicates from the list.


for i in range(0, len(cubes)):
    x = cubes[i]
    istr = str(x)
    lst = list(istr)
    ppd = permutation(lst)
    # using list comprehension
    # to remove duplicated 
    # from list 
    pp = []
    [pp.append(x) for x in ppd if x not in pp]
    print(len(pp))
    cub = []
    for i in range(0, len(pp)):
        ppi = "".join(pp[i])
        ppint = int(ppi)

        if iscube(ppint) == True:
            cub.append(ppint)
        #print(i, len(pp), cub, ppint, round(math.pow(ppint,1/3)))
    if len(cub) > 2:
        print(cub)
