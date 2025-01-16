from typing import List

global_sum = 0
flag = False


def rec(ssq, arr: List, start_ind):
    global flag
    if flag:
        return
    klen = len(ssq)
    if start_ind == klen:
        sumk = 0
        ind_sum = 0
        num_arr = []
        for i in arr:
            n = ssq[ind_sum:ind_sum + i]
            num_arr.append(n)
            sumk += int(n)
            ind_sum += i
        if sumk ** 2 == int(ssq):
            global global_sum
            global_sum += sumk ** 2
            flag = True
            print(sumk, arr, num_arr, ssq)
        return

    for i in range(start_ind, klen):
        c_arr = arr.copy()
        diff = i - start_ind + 1
        c_arr.append(diff)
        rec(ssq, c_arr, diff + start_ind)


for i in range(2, 1000001):
    sq = i ** 2
    start_ind = 0
    end_ind = 0
    arr = []
    ssq = str(sq)
    flag = False
    rec(ssq, [], 0)

print(global_sum)
