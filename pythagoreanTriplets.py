def pythagoreanTriplets(n):
    a = 1
    b = 2
    for c in range(1000):
        cs = math.pow(c,2)
        for b in range(999):

        if ((a*a) + (b*b) == (c*c)):
