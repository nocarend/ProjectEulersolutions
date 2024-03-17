import math
def smallest_d(k):
    prime_factors = [2]
    i = 3
    while i < k:
        factor = i
        for x in range(0, len(prime_factors)):
            if i % prime_factors[x] == 0:
                factor //= prime_factors[x]
        if factor > 1:
            prime_factors.append(factor)
        i += 1
    return math.prod(prime_factors)
