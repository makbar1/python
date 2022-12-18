'''
i = 1
# str(i**3)
print(str(i**3))

# list(str(i**3))
print(list(str(i**3)))

# sorted(list(str(i**3)))
print(sorted(list(str(i**3))))
'''
# import time
from audioop import reverse
import re
import time

def isbouncy(n):
    num = list(str(n))
    num_sorted = sorted(num)
    num_reverse = sorted(num, reverse=True)
    if num == num_sorted or num == num_reverse:
        return True
    return False

'''
i = 12789
iss = list(str(i))
isss = sorted(iss)
issr = sorted(iss,reverse=True)
isl= len(iss)
checkup = 0
checkd = 0
print(iss)
print(isss)
print(issr)
if iss == isss or iss == issr:
    print("Not Bouncy")
for x in range(0, isl - 1):
    if int(iss[x]) > int(iss[x+1]):
        print("Decreasing")
        break
'''

x = 0
percent_bouncy = 0
for i in range(1,9999999):
    if isbouncy(i) == False:
        x = x + 1
    percent_bouncy = int(x/i * 100)
    if percent_bouncy == 99:
        print(percent_bouncy, i)
        break
### Answer was correct