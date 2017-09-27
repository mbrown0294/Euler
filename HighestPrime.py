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


print(highestPrime(600851475143))

