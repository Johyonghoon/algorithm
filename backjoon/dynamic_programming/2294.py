# 2294번 동전 2
# https://www.acmicpc.net/problem/2294

"""
코인의 가치 + dp[k - 코인의 가치] 의 최소값 찾기
"""

import sys
input = sys.stdin.readline
INF = int(1e9)

n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
coin.sort()

dp = [INF for _ in range(k+1)]
for c in coin:
    if c > k:
        continue
    dp[c] = 1

for idx in range(2, k+1):
    for c in coin:
        if idx < c:
            break
        if dp[idx-c] != -1:
            dp[idx] = min(dp[idx], dp[c] + dp[idx-c])

# print(dp)
if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
