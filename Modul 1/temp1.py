from math import sqrt
def primeCheck(prime):
    isPrime = True
    for i in range(2, int(sqrt(prime))+1):
        if prime%i == 0:
            isPrime = False
    if prime in [0, 1]:
        isPrime = False
    return isPrime
