# 10826번 피보나치 수 4
# https://www.acmicpc.net/problem/10826

# Fn = Fn-1 + Fn-2 (N >= 2)
n = int(input())
dp = [0 for _ in range(10_001)]
dp[1] = 1
for idx in range(2, n+1):
    dp[idx] = dp[idx-1] + dp[idx-2]

print(dp[n])
