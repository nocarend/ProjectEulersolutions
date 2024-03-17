def divisors(num):
    div = 0
    for i in range(1, int(num ** 0.5) + 1):

        if num % i == 0:
            div += 2

            if i * i == num:
                div -= 1

    return div


def TriangleNumber(div):
    n = 1
    while (True):
        triangle = (n * (n + 1)) / 2
        count = 0

        if n % 2 == 0:
            count = divisors(n / 2) * divisors(n + 1)
        else:
            count = divisors((n + 1) / 2) * divisors(n)

        if count >= div:
            print(triangle)
            break

        n += 1


TriangleNumber(500)
