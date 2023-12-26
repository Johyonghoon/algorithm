# 13699번 점화식
# https://www.acmicpc.net/problem/13699

"""
t(0) = 1
t(1) = t(0) * t(0)
t(2) = t(0) * t(1) + t(1) * t(0)
t(3) = t(0) * t(2) + t(1) * t(1) + t(2) * t(0)
t(i) = sum(t(j) * t(i-j-1))
"""
n = int(input())
dp = [0 for _ in range(n+1)]
dp[0] = 1
for i in range(1, n+1):
    for j in range(i):
        dp[i] += dp[j] * dp[i-j-1]

print(dp[n])
