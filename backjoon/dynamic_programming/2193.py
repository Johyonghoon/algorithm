# 2193번 이친수
# https://www.acmicpc.net/problem/2193

"""
이친수는 0으로 시작하지 않는다.
이친수에서는 1이 연속으로 두 번 나타나지 않는다.
즉, 11을 부분 문자열로 가지지 않는다.

1 다음에는 무조건 0
1   0   0   0   0
                1
            1   0
        1   0   0
                1
1   1   2   3   5
"""

N = int(input())
dp = [0 for _ in range(N+2)]
dp[0] = 1
dp[1] = 1

if N < 3:
    pass
else:
    for idx in range(2, N):
        dp[idx] = dp[idx-1] + dp[idx-2]

print(dp[N-1])
