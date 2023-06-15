# 12865번 평범한 배낭
# https://www.acmicpc.net/problem/12865
import sys

import numpy as np

input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
for _ in range(N):
    weight, value = map(int, input().split())
    arr.append([weight, value])
dp = [[-1 for _ in range(100001)] for _ in range(N)]

def recur(idx, weight):
    if weight > K:
        return - int(1e9)
    if idx == N:
        return 0
    if dp[idx][weight] != -1:
        return dp[idx][weight]
    print(idx, weight, max(recur(idx+1, weight+arr[idx][0]) + arr[idx][1], recur(idx+1, weight)))
    dp[idx][weight] = max(recur(idx+1, weight+arr[idx][0]) + arr[idx][1], recur(idx+1, weight))
    return dp[idx][weight]

recur(0, 0)
print(np.array(dp))

ls = []
for i in dp:
    ls = ls + i
print(max(ls))
"""
# 완전탐색(재귀) - 시간초과
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
arr = []
max_weight = 0
for _ in range(N):
    weight, value = map(int, input().split())
    arr.append([weight, value])
ans = 0

def recur(idx, weight, value):
    global ans
    if weight > K:
        return
    if idx == N:
        ans = max(ans, value)
        return
    recur(idx+1, weight+arr[idx][0], value+arr[idx][1])
    recur(idx+1, weight, value)

recur(0, 0, 0)
print(ans)
"""