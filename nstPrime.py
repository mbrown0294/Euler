from HighestPrime import isPrime


def nstPrime(n):
    primes = [0] * n
    x = 0
    z = 2
    while x < n:
        if isPrime(z):
            primes[x] = z
            x += 1
        z += 1
    return primes[len(primes)-1]


print(nstPrime(10001))