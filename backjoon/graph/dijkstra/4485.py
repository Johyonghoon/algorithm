# 4485번 녹색 옷 입은 애가 젤다지?
# https://www.acmicpc.net/problem/4485

import sys
import heapq
input = sys.stdin.readline


def bfs():
    pq = []
    heapq.heappush(pq, (graph[0][0], 0, 0))  # y, x
    dist[0][0] = graph[0][0]
    while pq:
        w, ny, nx = heapq.heappop(pq)
        # if dist[N-1][N-1] != int(1e9):
        #     break

        if w > dist[ny][nx]:
            continue

        for dy, dx in delta:
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey < N and 0 <= ex < N:
                if dist[ey][ex] > dist[ny][nx] + graph[ey][ex]:
                    dist[ey][ex] = dist[ny][nx] + graph[ey][ex]
                    heapq.heappush(pq, (dist[ey][ex], ey, ex))


tc = 1
delta = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 상하좌우
while True:
    N = int(input())
    if N == 0:
        break

    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    dist = [[int(1e9) for _ in range(N)] for _ in range(N)]
    bfs()
    print(f"Problem {tc}: {dist[N-1][N-1]}")
    tc += 1
