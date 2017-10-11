from HighestPrime import primesList


def primeSum(n):
    primeList = primesList(n)
    sum = 0
    for x in primeList:
        sum += x
    return sum


print(primeSum(2000000))