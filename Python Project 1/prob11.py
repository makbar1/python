# import numpy module for matrix operations
#from numpy import *

# read the file with the matrix of numbers
filename = 'euler11.txt'

# store each line of the file into an array
with open(filename, "r") as ins:
    array = []
    for line in ins:
        array.append(line)
print(array[:1])