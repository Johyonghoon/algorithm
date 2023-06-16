# 1520번 내리막길
# https://www.acmicpc.net/problem/1520
"""
M, N = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(M)]
dp = [[0 for _ in range(M)] for _ in range(N)]

def recur(idx, x, y):
    for dx, dy in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ex, ey = x + dx, y + dy
        if graph[ey][ex] > graph[y][x]:
            dp[ey][ex] += dp[y][x]
            """