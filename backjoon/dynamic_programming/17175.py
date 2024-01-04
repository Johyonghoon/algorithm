# 17175번 피보나치는 지겨웡~
# https://www.acmicpc.net/problem/17175

"""
자기 자신이 사용되는 것도 호출에 포함
dp[2] = fibo(1) + fibo(0)
"""

N = int(input())
dp = [0 for _ in range(N+1)]
dp[:3] = [1, 1, 3]
for i in range(3, N+1):
    dp[i] = (1 + dp[i-1] + dp[i-2]) % 1_000_000_007
print(dp[N])
