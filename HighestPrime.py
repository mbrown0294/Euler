import math

def highestPrime(n):
  for x in range(n, 1,-1):
      if (isPrime(x)) & (n % x == 0):
          return x


def isPrime(n):
    if (n == 1) | (n == 0):
        return False
    for x in range(1, int(math.sqrt(n)) + 1):
        if (n % x == 0) & (x != 1):
            return False
    return True


<<<<<<< Updated upstream
=======
def primesList(n):
    primes = (n+1) * [True]
    count = 0
    for x in range(n + 1):
        if primes[x] == False:
            continue
        elif isPrime(x):
            primes[x] = True
            count += 1
        else:
            primes[x] = False
        y = 2
        while (x * y) < (n + 1):
            primes[x * y] = False
            y += 1
    done = count * [0]
    z = 0
    for x in range(n + 1):
        if primes[x] == True:
            done[z] = primes[x]
            z += 1
    return done

>>>>>>> Stashed changes
print(highestPrime(600851475143))

