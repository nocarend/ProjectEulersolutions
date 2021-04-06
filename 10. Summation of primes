sieve = [True] * 2000000
sieve[0] = sieve[1] = False
sum_of_primes = 0
for i in range(2, 2000000):
    if sieve[i]:
        sum_of_primes += i
        for n in range(i * i, 2000000, i):
            sieve[n] = False
print(sum_of_primes)
