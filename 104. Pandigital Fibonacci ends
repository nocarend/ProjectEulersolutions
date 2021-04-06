from itertools import permutations
from math import log10, pow
from decimal import Decimal


def mantissa(number):
    (s, dig, ex) = Decimal(number).as_tuple()
    return dig[:9]


PDhead = set(permutations(range(1, 10)))
PDtail = {int(''.join(p)) for p in permutations('123456789')}

sq5 = 5 ** (0.5)
phi = (1 + sq5) / 2
logsq5 = log10(sq5)
logphi = log10(phi)


def fib(n):
    f = 10 ** ((n * logphi - logsq5) % 1)
    return f


fa = 1
fb = 1
n = 2
stop = False

while not stop:
    fa, fb = fb, (fa + fb) % 1000000000
    n = n + 1
    if fb in PDtail:
        head = fib(n)
        stop = mantissa(head) in PDhead

print(n)
