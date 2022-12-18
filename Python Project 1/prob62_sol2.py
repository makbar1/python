import time
# time at the start of program
start = time.time()

# list to store cubes
cubes = []

# iterator
i = 0

# while loop
while True:
    # cube of the number
    cube = sorted(list(str(i**3)))
    # appending the cube to cubes list
    cubes.append(cube)
    #print(i,"cube=",cube,"cubes=", cubes, cubes.count(cube))
    #time.sleep(1)
    # check if it occured 5 times
    if cubes.count(cube) == 5:
    # print the cube of the smallest such cube
        print((cubes.index(cube))**3)
        break
    i += 1
# time at the end of program
end = time.time()

# total time taken
print(end - start)

i = 27

c = []
# str(i**3)
print(str(i**3))

# list(str(i**3))
print(list(str(i**3)))

# sorted(list(str(i**3)))
x = sorted(list(str(i**3)))
print(x)
c.append(x)
print(c)
i = 10
x = sorted(list(str(i**3)))
print(x)
c.append(x)
print(c)
c.append(x)
print(c)
print(c.index(x))
c.append(x)
print(c)
print(c.index(x), c.count(x))
