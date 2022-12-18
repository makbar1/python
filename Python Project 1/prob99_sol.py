import math
import time
from datetime import datetime
start_time = datetime.now()
start=time.time()
a_file = open("base_exp.txt")
mv, ml = 0, 0
for ln, li in enumerate(a_file):
    b, e = map(int, li.split(','))
    v = e * math.log(b)
    if v > mv:
        mv, ml = v, ln + 1
print(ml)
end=time.time()
print(end-start)
print("--- %s seconds ---" % (time.time() - start))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
