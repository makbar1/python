
# Read lines from a file and write 5 letter words


f1 = open("words.txt", "r")
f2 = open("doc2.txt", "w")

l = f1.readline()
while l:
    x = str(l)
    if len(x) == 6:
        f2.write(l)
        #print(l, len(x))
    l = f1.readline()
f1.close()
f2.close()