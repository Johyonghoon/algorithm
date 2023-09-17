# 14940번 쉬운 최단거리
# https://www.acmicpc.net/problem/14940

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

sy, sx = 0, 0
result = [[-1 for _ in range(m)] for _ in range(n)]
q = deque()
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            result[y][x] = 0
        if graph[y][x] == 2:
            q.append([y, x])
            result[y][x] = 0
            sy, sx = y, x

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while q:
    ny, nx = q.popleft()
    for dy, dx in delta:
        ey, ex = ny + dy, nx + dx
        if 0 <= ey < n and 0 <= ex < m:
            if ey == sy and ex == sx:
                continue
            if result[ey][ex] != -1:
                continue
            if graph[ey][ex] == 1:
                result[ey][ex] = result[ny][nx] + 1
                q.append([ey, ex])

[print(*i) for i in result]

"""
15 15
0 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1 0 1 1 1 1
1 1 1 1 1 1 1 1 1 1 0 1 0 0 0
1 1 1 1 1 1 1 1 1 1 0 1 1 1 2

"""

