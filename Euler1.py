# Multiples of 3 and 5
#'''If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

def sumMult(multOf, inThis):
    sum = 0
    for x in range(inThis):
        if x % multOf == 0:
            sum += x
    return sum


if __name__== '__main__':
    print((sumMult(3, 1000) + sumMult(5, 1000)) - sumMult(15, 1000))