'''Project Euler Prob 22
Sort names in file names.txt
'''

f1 = open("names.txt", "r")
#f1 = open("abc.txt", "r")
f2 = open("names.out", "w")

names=sorted(f1.read().replace('"','').split(','),key=str)

def name_weight(name):
    sum = 0
    for i in range(0, len(name)):
        x = ord(name[i]) - 64
        sum = sum + int(x)
    return(sum)

f1.close()
#f2.close()

# Open a Dictionary of the form Name:Weight e.g. COLIN:53
NameDict = {}

print(len(names))
for i in range(0, len(names)):
    #f2.write(names[i])
    x = name_weight(names[i] * (i+1))
    NameDict[names[i]]=x
    a=NameDict.items()
    f2.write(str(a))
    f2.write("\n")
f2.close()

'''
a = "COLIN"
sum = 0
for i in range(0, len(a)):
    x = ord(a[i]) - 64
    sum = sum + int(x)
print(sum)
print(name_weight("COLIN"))
'''

sum = 0
for x, y in NameDict.items():
    #print(x, y)
    sum = sum + y
print(sum)

# Answer was correct


