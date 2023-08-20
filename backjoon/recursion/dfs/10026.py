# 10026번 적록색약
# https://www.acmicpc.net/problem/10026

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(ny, nx, color):
    visited[ny][nx] = 1

    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey, ex = ny + dy, nx + dx
        if 0 <= ey < N and 0 <= ex < N:
            if visited[ey][ex]:
                continue
            if graph[ey][ex] == color:
                recur(ey, ex, color)


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))

# 적록색약이 아닌 사람
visited = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
for y in range(N):
    for x in range(N):
        if visited[y][x]:
            continue
        recur(y, x, graph[y][x])
        cnt += 1

# 적록색약인 사람을 위해 색깔 통일 (G -> R)
for y in range(N):
    for x in range(N):
        if graph[y][x] == "G":
            graph[y][x] = "R"

# 적록색약인 사람
visited = [[0 for _ in range(N)] for _ in range(N)]
cnt_weak = 0
for y in range(N):
    for x in range(N):
        if visited[y][x]:
            continue
        recur(y, x, graph[y][x])
        cnt_weak += 1

print(cnt, cnt_weak)
