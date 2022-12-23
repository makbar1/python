n = 600851475143
n=100
p = 2
while n > 1:
    if n % p == 0:
        #n //= p
        n = n // p
        print(n,p)
    else:
        p += 1
print(p)