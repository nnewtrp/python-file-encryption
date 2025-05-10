from math import *
import random

def primeInRange(x, y):
    prime_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_list.append(n)
            
    return prime_list

def PUKeyGen(key):
    prime = primeInRange(10,31)
    
    p = random.choice(prime)
    q = random.choice(prime)
    n = p*q

    while n < key:
        p = random.choice(prime)
        q = random.choice(prime)
        n = p*q
    
    phiOfn = (p-1)*(q-1)

    E = []

    for i in range(1,phiOfn):
        if gcd(i,phiOfn)==1:
            E.append(i)

    e = random.choice(E)

    PUkey = (e,n)

    return PUkey,phiOfn

def PRKey(PUkey,phiOfn):
    e,n = PUkey

    for i in range(1, phiOfn):
        if i*e%phiOfn==1:
            d = i
            break
    
    PRkey = (d,n)

    return PRkey
