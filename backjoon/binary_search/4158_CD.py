# 4158번 CD
# https://www.acmicpc.net/problem/4158
# not solved

import sys
from collections import defaultdict

input = sys.stdin.readline


while True:
    d = defaultdict(bool)
    cnt = 0
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    for _ in range(n):
        d[int(input())] = True
    for _ in range(m):
        if d[int(input())]:
            cnt += 1
    print(cnt)
