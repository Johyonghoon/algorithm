# 2573번 빙산
# https://www.acmicpc.net/problem/2573

import sys
from collections import deque
input = sys.stdin.readline


def melting():
    for y, x, m in melt:
        graph[y][x] -= m
        if graph[y][x] < 0:
            graph[y][x] = 0


def bfs(y, x, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    while q:
        ny, nx = q.popleft()
        m = 0
        for dy, dx in delta:
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey < N and 0 <= ex < M:
                if graph[ey][ex]:
                    if visited[ey][ex]:
                        continue
                    q.append((ey, ex))
                    visited[ey][ex] = 1
                else:
                    m += 1
        else:
            melt.append((ny, nx, m))
    return visited


def every_year():
    global is_split, melt, result
    cnt = 0
    while cnt < 2:
        visited = [[0 for _ in range(M)] for _ in range(N)]
        for y in range(N):
            for x in range(M):
                if visited[y][x]:
                    continue
                if not graph[y][x]:
                    visited[y][x] = 1
                    continue
                visited = bfs(y, x, visited)
                cnt += 1
        if cnt == 0:
            is_split = False
            break
        if cnt > 1:
            break
        cnt = 0
        result += 1
        melting()
        melt = []


N, M = map(int, input().split())
graph = []
melt = []
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for _ in range(N):
    graph.append(list(map(int, input().split())))

result = 0
is_split = True
every_year()
if is_split:
    print(result)
else:
    print(0)
