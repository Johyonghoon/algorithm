# 15988번 1, 2, 3 더하기 3
# https://www.acmicpc.net/problem/15988

"""
순서가 다른 더하기 연산은 다른 경우의 수로 취급
[1, 2, 3]
1   1   (1 0 0)
2   2   (2 0 0) (0 1 0)
3   4   (3 0 0) (1 1 0) (0 0 1)
4   7   (4 0 0) (2 1 0) (1 0 1) (0 2 0)
5   13  (5 0 0) (3 1 0) (2 0 1) (1 2 0) (0 1 1)
6       (6 0 0) (4 1 0) (3 0 1) (2 2 0) (1 1 1) (0 3 0) (0 0 2)
"""

dp = [0 for _ in range(1_000_001)]
dp[:4] = [0, 1, 2, 4]

for idx in range(4, 1_000_001):
    dp[idx] = (dp[idx-1] + dp[idx-2] + dp[idx-3]) % 1_000_000_009

T = int(input())
for _ in range(T):
    n = int(input())
    print(dp[n])
