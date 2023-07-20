# 1520번 내리막길
# https://www.acmicpc.net/problem/1520
import numpy as np

M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for _ in range(M)]
dp[M-1][N-1] = 1

def recur(y, x):

    if y == M-1 and x == N-1:
        return dp[y][x]

    if dp[y][x] != -1:
        return dp[y][x]

    cnt = 0
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey = y + dy
        ex = x + dx
        if 0 <= ey < M and 0 <= ex < N:
            if graph[y][x] > graph[ey][ex]:
                cnt += recur(ey, ex)
    dp[y][x] = cnt
    # print(y, x, dp[y][x])
    return dp[y][x]

recur(0, 0)

# print(np.array(graph))
# print(np.array(dp))
print(dp[0][0])
