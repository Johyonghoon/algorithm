# 2225번 합분해
# https://www.acmicpc.net/problem/2225

"""
1 <= N <= 200
1 <= K <= 200
0부터 N까지의 정수 K개를 더해 그 합이 N이 되는 경우

20 1 ?
20 => 1가지
20 2
0 20
...
20 0

6 4
6 (0, 0, 0) => 세 수로 0을 만드는 법
5 (1, 0, 0) (0, 1, 0) (0, 0, 1)

개수/수
    0   1   2   3   4   5   6   7   8   9   10
0   0   0   0   0   0   0   0   0   0   0   0
1   1   1   1   1   1   1   1   1   1   1   1
2   1   2   3   4   5   6   7   8   9   10  11
3   1   3   6   10  15  21  28
4   1   4   10  20  35  56  84
...
dp[y][x] = dp[y-1][x] + dp[y][x-1]
"""
N, K = map(int, input().split())
dp = [[0 for _ in range(N+1)] for _ in range(K+1)]
for y in range(1, K+1):
    for x in range(N+1):
        if x == 0:
            dp[y][x] = 1
            continue
        dp[y][x] = (dp[y-1][x] + dp[y][x-1]) % int(1e9)

print(dp[K][N])
