# 15486번 퇴사 2
# https://www.acmicpc.net/problem/15486
import sys
sys.setrecursionlimit(10**7)

N = int(input())
input = sys.stdin.readline
arr = [0]
for _ in range(N):
    arr.append(list(map(int, input().split())))
dp = [-1 for _ in range(N+1)]

def recur(idx):
    global arr, dp
    if idx > N+1:
        return - int(1e9)
    if idx == N+1:
        return 0
    if dp[idx] != -1:
        return dp[idx]
    dp[idx] = max(recur(idx + arr[idx][0]) + arr[idx][1], recur(idx+1))
    return dp[idx]

recur(1)
print(max(dp))
