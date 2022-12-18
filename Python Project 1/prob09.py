# Project Euler Prob 09
# 
# There exists exactly one Pythagorean triplet for which a + b + c = 1000


for a in range(1, 201):
    for b in range(1, 501):
        for c in range(1, 501):
            if (a**2 + b**2) == c**2:
                if (a+b+c) == 1000:
                    print(a*b*c,a+b+c, a,b,c)
