# 10427번 빚
# https://www.acmicpc.net/problem/10427

# from pprint import pprint

"""
M개의 돈을 고르면, 가장 많은 돈과의 차이만큼 추가적으로 갚아야 한다.
예를 들어, 2, 3, 5의 돈 중에 2, 3을 골랐다면 (3-2) + (3-3) 만큼 드는 것이다.
"""

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    arr = list(map(int, input().split()))
    N, money = arr[0], sorted(arr[1:])

    dp = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(y):
            dp[y][x] = money[y] - money[x]
    # pprint(dp)

    prefix = [int(1e9) for _ in range(N)]
    for idx in range(1, N):
        total = 0
        for j, num in enumerate(reversed(dp[idx][:idx])):
            total += num
            prefix[j] = min(prefix[j], total)

    print(sum(prefix[:N-1]))
