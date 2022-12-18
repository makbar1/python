def ispalind(num):
    s = list(str(num))
    ls = len(s)
    # Have different loops for odd and even digits
    if ls % 2 == 0:
        a = int(len(s)/2)
        i = 0
        b = ls
        while i <a:
            #print(s[i],s[b-1])
            if s[i] != s[b-1]:
                break
            i = i + 1
            b = b -1
        if i == b:
            return True
    else:
        a = int(len(s)/2+1)
        i = 0
        b = ls
        while i <a:
            if s[i] != s[b-1]:
                break
            i = i + 1
            b = b -1
        if i == b + 1:
            return True




#print(ispalind(1221))
#x = int(595**0.5)
a = 0
b = 1

palindromes = []
for i in range(1, 1000001):
    if ispalind(i) == True:
        palindromes.append(i)
palins=sorted(set(palindromes))

#print(bin(2)[2:])

x = []
#print(xb)
for i in range(0, len(palins)):
    xb = bin(palins[i])[2:]
    if ispalind(xb) == True:
        x.append(palins[i])

print(sum(x))

## Answer was correct
    

