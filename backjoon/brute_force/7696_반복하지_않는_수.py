# 7696번 반복하지 않는 수
# https://www.acmicpc.net/problem/7696
from collections import defaultdict

dp = [0 for _ in range(int(1e6)+1)]

while True:
    N = int(input())

    if N == 0:
        break

    for idx in range(1, N+1):
        if dp[idx] != 0:
            continue


    if N < 10:
        print(N)
        continue
    while cnt != N:
        ls = list(map(int, str(N // 10)))
        print(ls)
        for i in range(max(ls)+1):
            cnt += 1
            if i in ls:
                continue
            n += 1
            if cnt == N:
                print(n)
                breaky = True
                break


"""
# 시간초과

while True:
    n = 0
    cnt = 0
    N = int(input())
    if N == 0:
        break
    while True:
        n += 1
        if n > 10:
            breaky = False
            d = defaultdict(int)
            temp = str(n)
            for i in temp:
                if temp.count(i) > 1:
                    breaky = True
                    break
            if breaky:
                continue
        cnt += 1
        if cnt == N:
            break
    if cnt == N:
        print(n)
        continue
"""