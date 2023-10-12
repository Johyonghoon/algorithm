# 17141번 연구소 2
# https://www.acmicpc.net/problem/17141
from collections import deque
from itertools import combinations


def bfs():
    global result
    while q:
        ny, nx = q.popleft()
        for dy, dx in delta:
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey < N and 0 <= ex < N:
                if dist[ey][ex] != int(1e9):
                    continue
                dist[ey][ex] = dist[ny][nx] + 1
                q.append([ey, ex])

    sec = 0
    for y in range(N):
        for x in range(N):
            sec = max(sec, dist[y][x])

    result = min(result, sec)


# 바이러스 좌표를 저장하고, 그래프 정보 입력
N, M = map(int, input().split())
graph = []
virus = []
walls = []
for y in range(N):
    arr = list(map(int, input().split()))
    for x, num in enumerate(arr):
        if num == 2:
            virus.append([y, x])
        elif num == 1:
            walls.append([y, x])
    graph.append(arr)

combis = list(combinations(range(len(virus)), M))
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# 조합
result = int(1e9)
for combi in combis:
    q = deque()
    dist = [[int(1e9) for _ in range(N)] for _ in range(N)]
    # 바이러스 정보 입력
    for idx in combi:
        q.append(virus[idx])
        y, x = virus[idx]
        dist[y][x] = 0
    # 벽 정보 입력
    for wall in walls:
        y, x = wall
        dist[y][x] = -1

    bfs()

if result == int(1e9):
    print(-1)
else:
    print(result)
