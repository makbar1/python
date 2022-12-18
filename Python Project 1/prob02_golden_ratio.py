from functools import lru_cache

@lru_cache(maxsize=1000)
def fibonacci(n):
    # Check n is an integer
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise ValueError("n must be a positive integer")
        
    # Compute the Nth Term    
    if n == 1:
        return  1
    elif n == 2:
        return  2
    elif n > 2:
        return  fibonacci(n-1) + fibonacci(n-2)
    
# Show golden ratio
for i in range(1, 50):
    print(i, ":" , fibonacci(i+1)/fibonacci(i))
