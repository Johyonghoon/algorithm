# 17086번 아기 상어 2
# https://www.acmicpc.net/problem/17086

"""
기본적인 BFS 문제
이동은 대각선까지 가능하다.
"""

import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 거리 정보를 업데이트 할 배열 생성
dist = [[int(1e9) for _ in range(M)] for _ in range(N)]

# queue 를 활용하여 bfs 탐색
q = deque()

# 상어의 위치 저장
for y in range(N):
    for x in range(M):
        if graph[y][x]:
            dist[y][x] = 0
            q.append([y, x])

# BFS
delta = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
while q:
    ny, nx = q.popleft()

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < N and 0 <= ex < M:
            if dist[ny][nx] + 1 < dist[ey][ex]:
                dist[ey][ex] = dist[ny][nx] + 1
                q.append([ey, ex])

result = 0
for y in range(N):
    for x in range(M):
        result = max(result, dist[y][x])

print(result)