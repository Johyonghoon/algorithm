# 9461번 파도반 수열
# https://www.acmicpc.net/problem/9461

dp = [0 for _ in range(101)]
dp[1:11] = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
for idx in range(11, 101):
    dp[idx] = dp[idx-1] + dp[idx-5]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])
