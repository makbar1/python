import time
# time at the start of program
start = time.time()


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True

primes=[1,2]
for x in range(3, 500000, 2):
    if is_prime(x) == True:
        primes.append(x)
print(primes)
end = time.time()

# total time taken
print(end - start)

