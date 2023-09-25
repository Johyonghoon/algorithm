# 13305번 주유소
# https://www.acmicpc.net/problem/13305

"""
현재 위치의 기름 가격보다 이전 위치의 기름 가격이 작을 때를 기록하여 그때까지의 거리만큼만 기름을 구매하기
"""

import sys
input = sys.stdin.readline

N = int(input())
dist = list(map(int, input().split()))
prices = list(map(int, input().split()))
dp = [0 for _ in range(N)]

dp[0] = prices[0]
for idx in range(1, N):
    if prices[idx] > dp[idx-1]:
        dp[idx] = dp[idx-1]
    else:
        dp[idx] = prices[idx]

result = 0
for idx in range(N-1):
    result += dist[idx] * dp[idx]

print(result)

