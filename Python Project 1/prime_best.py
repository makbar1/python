nums = range(2,120000)

def is_prime(num):
    if num == 2:
        return True
    if num == 3: 
        return True
    for x in range(2, int(num**1/2)+1):
        if (num%x) == 0:
            return False
    return True


primes = list(filter(is_prime, nums))

#print(primes,len(primes))
print(len(primes))
print(primes[10000])
    
    