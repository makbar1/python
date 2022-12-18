# Project Euler Prob 2
# https://projecteuler.net/problem=1
# By considering the terms in the Fibonacci sequence whose values 
# do not exceed four million, find the sum of the even-valued terms.
#
fibonacci_cache = {}

def fibonacci(n):
    # If value is defined in cache return it
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    # Compute the Nth Term    
    if n == 1:
        value = 1
    elif n == 2:
        value = 2
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)
    
    fibonacci_cache[n] = value
    return value

x = 0
for n in range(1, 35):
    y = fibonacci(n)
    if y % 2 == 0:
        x = x + y
        print(n, y, x)
print(x)

