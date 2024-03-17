ans = 0
kk = 1
ans2 = 0
kek = set()
while True:
    if kk < 1e4:
        s = kk ** 2
        for i in range(kk + 1, 100000000):
            if (s + i ** 2 < 1e8):
                s += i ** 2
                if str(s) == str(s)[::-1] and kek.__contains__(s) == 0:
                    ans += 1
                    ans2 += s
                    kek.add(s)
            else:
                break
        kk += 1
    else:
        break
print(ans2)
# 2906969179
