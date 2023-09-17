# 11501번 주식
# https://www.acmicpc.net/problem/11501

T = int(input())
for _ in range(T):
    N = int(input())
    stocks = list(map(int, input().split()))

    idx = N-1
    maxi = stocks[idx]
    total = 0
    while idx >= 0:
        # print(idx, maxi, total)
        if maxi <= stocks[idx]:
            maxi = stocks[idx]
        else:
            total += maxi - stocks[idx]
        idx -= 1

    print(total)
