target = 1000000

collatz_dict = {1: 1}


def collatz(n):
    if n in collatz_dict:
        return collatz_dict[n]

    if (0 == (n % 2)):
        ans = 1 + collatz(n // 2)
    else:
        ans = 1 + collatz(3 * n + 1)

    collatz_dict[n] = ans

    return ans


max_chain = 0
max_n = 0

for n in range(1, target):
    chain_size = collatz(n)
    if (chain_size > max_chain):
        max_chain = chain_size
        max_n = n

print(max_n)
