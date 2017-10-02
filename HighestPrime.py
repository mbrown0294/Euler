import math

def highestPrime(n):
    primes = primesList(int(math.sqrt(n)))
    for x in range(len(primes)-1, 0, -1):
        prime = primes[x]
        if n % prime == 0:
            return prime


def isPrime(n):
    count = 0
    for x in range(1, int(math.sqrt(n)) + 1):
        if (n % x == 0) & (x != 1):
            count += 1
    if count == 0:
        return True
    return False


def primesList(n):
    primes = (n+1) * [True]
    count = 0
    primes[0] = False
    primes[1] = False
    for x in range(2,n + 1):
        if primes[x] == False:
            continue
        else:
            count += 1
            y = 2
            while (x * y) < (n + 1):
                primes[x * y] = False
                y += 1
    done = count * [0]
    z = 0
    for x in range(n + 1):
        if primes[x] == True:
            done[z] = x
            z += 1
    return done


#print(primesList(11)) #Output: 2, 3, 5, 7, 11
print(highestPrime(600851475143))