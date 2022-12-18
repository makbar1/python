'''
Euler Prob 43 - Pandigital
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each 
of the digits 0 to 9 in some order,

'''

def pandig(num):
    a = list(str(num))
    if len(set(a)) == len(a):
        return True      

pandigitalnums =[]
for i in range(1034567892, 1134567890):
    if pandig(i) == True:
        pandigitalnums.append(i)

print(len(pandigitalnums))