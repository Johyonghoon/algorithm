# 1699번 제곱수의 합
# https://www.acmicpc.net/problem/1699

N = int(input())
dp = [int(1e9) for _ in range(N+1)]
dp[0] = 0
dp[1] = 1
for i in range(2, N+1):
    maxi = int(i ** (1/2))
    if i == maxi ** 2:
        dp[i] = 1
        continue
    for j in range(1, maxi+1):
        dp[i] = min(dp[i], dp[j**2] + dp[i-j**2])

print(dp[N])
