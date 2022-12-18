import math
from pickle import APPEND
import time

start = time.time()
cubes=[]
i = 0
#for i in range(0, 100000):
while True:
    #cube = str(i**3)
    cubel = sorted(list(str(i**3)))
    cubes.append(cubel)
    if cubes.count(cubel) == 5:
        print(cubes.index(cubel)**3)
        break
    i = i + 1


end = time.time()
print(end-start)
