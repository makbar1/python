# Euler 24


x = 123
xs = str(x)
lst = []
l2=[]
l3=[]

### List append does not work within a command. It returns None
### e.g list1 = list1.append(2) will not work
### But the following will
### list1.append(2)
### print(list1)
'''
for a in range(0, len(xs)):
    lst.append(xs[a])
print(lst)
'''


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



data = list('0123456789')
print(data)
nth = 0
for p in permutation(data):
    nth = nth + 1
    if nth == 1000000:
        print(nth,p)
        # Write list of numbers as one number
        print("".join(p))
        break

### Answer was correct