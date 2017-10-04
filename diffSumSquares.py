import math

def sumSquared(n):
    sum = 0
    for x in range(1,n + 1):
        sum += math.pow(x,2)
    return sum


def squaredSum(n):
    sum = 0
    for x in range(1, n+1):
        sum += x
    sum = math.pow(sum,2)
    return sum



print(math.fabs(sumSquared(100) - squaredSum(100)))