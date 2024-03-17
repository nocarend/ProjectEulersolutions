b = []
max = 0
for i in range(20):
    b.append([])
    b[i] = [int(s) for s in input().split()]
for i in range(20):
    for j in range(20):
        if j + 3 < 20:
            k = b[i][j]
            s = 1
            for gorznt in range(4):
                k = b[i][j + gorznt]
                s *= k
            if s > max:
                max = s
        if i + 3 < 20:
            k = b[i][i]
            s = 1
            for vert in range(4):
                k = b[i + vert][j]
                s *= k
            if s > max:
                max = s
        if i + 3 < 20 and j + 3 < 20:
            k = b[i][j]
            s = 1
            for diagnright in range(4):
                k = b[i + diagnright][j + diagnright]
                s *= k
            if s > max:
                max = s
        if i + 3 < 20 and j - 3 > -1:
            k = b[i][j]
            s = 1
            for diagnleft in range(4):
                k = b[i + diagnleft][j - diagnleft]
                s *= k
            if s > max:
                max = s
print(max)

