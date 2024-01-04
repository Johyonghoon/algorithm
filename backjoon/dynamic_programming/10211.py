# 10211번 Maximum Subarray
# https://www.acmicpc.net/problem/10211

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    dp = [0 for _ in range(N)]
    dp[0] = numbers[0]
    for i in range(1, N):
        if dp[i-1] > 0:
            dp[i] = dp[i-1] + numbers[i]
        else:
            dp[i] = numbers[i]
    print(max(dp))
