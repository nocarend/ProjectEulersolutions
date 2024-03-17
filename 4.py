a = 999
k = 0
while a >= 100:
    if a % 11 == 0:
        db = 1
        b = 999
    else:
        b = 990
        db = 11
    while b >= a:
        if a * b <= k:
            break
        if str(a * b) == str(a * b)[::-1]:
            k = a * b
        b -= db
    a -= 1
print(k)
