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

#print(cubes)
print(len(cubes))
for i in range(0, len(cubes)):
    x = cubes[i]
    istr = str(x)
    lst = list(istr)
    pp = permutation(lst)

    cub = []
    for i in range(0, len(pp)):
        ppi = "".join(pp[i])
        ppint = int(ppi)

        if iscube(ppint) == True:
            cub.append(ppint)
        else:
            break
        #print(i, len(pp), cub, ppint, round(math.pow(ppint,1/3)))
        print(cub)

'''
for i in range(41063625, 41063626):
    if iscube(i) == True:
        istr = str(i)
        lst = list(istr)
        pp = permutation(lst)
    
for i in range(1, len(pp)):
    # Convert the list of numbers to a single number
    ppi = "".join(pp[i])
    ppint = int(ppi)
    if iscube(ppint) == True:
        print(i, len(pp), ppint, round(math.pow(ppint,1/3)))
'''
