# 17212번 달나라 토끼를 위한 구매대금 지불 도우미
# https://www.acmicpc.net/problem/17212

"""
1, 2, 5, 7원 동전을 사용해 동전의 개수가 최소가 되게 하는 개수
1 = 1
2 = 1
3 = 2
4 = 2
5 = 1
6 = 2
7 = 1
"""

N = int(input())
dp = [0 for _ in range(100_001)]
dp[1:8] = [1, 1, 2, 2, 1, 2, 1]
for i in range(8, N+1):
    dp[i] = min(dp[i-1], dp[i-2], dp[i-5], dp[i-7]) + 1

print(dp[N])
