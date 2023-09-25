# 1261번 알고스팟
# https://www.acmicpc.net/problem/1261

"""
# 다익스트라 : 가중치가 다르므로, BFS가 아닌 다익스트라
이 문제는 2665번과 유사하지만, 이미 벽에 대한 정보가 1로 주어지므로
별다르게 그래프 정보를 변경시켜줄 필요가 없다.
"""

import sys
import heapq
input = sys.stdin.readline

# 그래프 정보 입력
M, N = map(int, input().split())
graph = []
for _ in range(N):
    arr = list(map(int, list(input().strip())))
    graph.append(arr)

# 최단경로 정보를 저장할 2차원 배열
dist = [[int(1e9) for _ in range(M)] for _ in range(N)]
dist[0][0] = 0

# 최소경로를 탐색하기 위한 힙 사용
pq = []
heapq.heappush(pq, [0, 0, 0])

# 델타탐색
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# BFS
while pq:
    w, ny, nx = heapq.heappop(pq)

    if w > dist[ny][nx]:
        continue

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < N and 0 <= ex < M:
            if dist[ny][nx] + graph[ey][ex] < dist[ey][ex]:
                dist[ey][ex] = dist[ny][nx] + graph[ey][ex]
                heapq.heappush(pq, [dist[ey][ex], ey, ex])

print(dist[N-1][M-1])
