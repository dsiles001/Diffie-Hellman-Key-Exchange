import random as r
import sympy
from tabulate import tabulate

def makePrime():
    while True:
        num = r.randint(10, 1000)
        if sympy.isprime(num):
            return num


# make prime numbers 
p = makePrime()

# find primitive roots
g = sympy.primitive_root(p)



# generate random private keys
a = r.randint(1, p-1)
b = r.randint(1, p-1)


# print(f"Alice's private key: {a}")
# print(f"Bob's private key: {b}")

# exchange of keys here
A = pow(g, a, p)
B = pow(g, b, p)


Asecret = pow(B, a, p)
Bsecret = pow(A, b, p)
print(f"Alice shared secret: {Asecret}")
print(f"Bob shared secret: {Bsecret}")

print(tabulate([['1', 'p', 'nothing', 'nothing'],
                ['2', 'p, g', 'nothing', 'nothing'],
                ['3', 'p, g, a', 'b', 'nothing'],
                ['4', 'p, g, a, A', 'b, B', 'nothing'],
                ['5', 'p, g, a, A, B', 'b, B, A, p, g', 'p, g, A, B'],
                ['6', 'p, g, a, A, B, S', 'b, B, A, p, g, S', 'p, g, A, B']], headers = ['Steps','A knows', 'B knows', 'Eve knows']))

