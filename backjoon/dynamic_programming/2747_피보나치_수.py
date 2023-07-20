# 2747번 피보나치 수
# https://www.acmicpc.net/problem/2747

N = int(input())
dp = [0 for _ in range(N+1)]
dp[1:3] = [1, 1]
for n in range(3, N+1):
    dp[n] = dp[n-1] + dp[n-2]
print(dp[N])
