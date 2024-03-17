man = []
for i in range(2, 150):
    for j in range(2, 150):
        tt = i ** j
        if len(str(tt)) > 1:
            lol = 0
            for k in str(tt):
                lol += int(k)
            if lol == i:
                man.append(tt)
man.sort()
for i in range(len(man)):
    print(i, man[i])
