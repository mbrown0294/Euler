import math

def highestPrime(n):
  for x in range(n, 1,-1):
      if (isPrime(x)) & (n % x == 0):
          return x


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
    primes[0] = False
    primes[1] = False
    count = 0
    for x in range(3, n + 1):
        if !isPrime(x):
            primes[x] = False
            count += 1




print(highestPrime(600851475143))

