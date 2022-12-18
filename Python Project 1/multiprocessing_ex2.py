from ast import arg
import concurrent.futures
from concurrent.futures import process
import multiprocessing
import time

start = time.perf_counter()
import math

def is_palindrome(num):
    a = str(num)
    reverse = a[::-1]
    if a == reverse:
        return num
    return


max = 0  
maxi = 0 
maxj = 0

if __name__ == "__main__":

    palins = []
    for i in range(1,11):
        p = multiprocessing.Process(target=is_palindrome, arg=(i,))
        p.start()
        palins.append(p)
    
    for pa in palins:
        process.join()



finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')