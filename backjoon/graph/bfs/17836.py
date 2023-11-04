# 17836번 공주님을 구해라
# https://www.acmicpc.net/problem/17836

"""
성의 마법 벽을 피해 해당 위치에 최단거리로 도달하는 문제
이때, graph[y][x]의 값이 2라면 graph에서 1로 되어있던 값들은 모두 0이 된다.
검을 찍고 돌아서 직행하는 경우도 있을 수 있음
그럼 아래의 상황을 고려해야 하지 않을까?
1. 첫 위치에서 바로 해당 위치에 도달하는 경우
2. 검에 도달하고 나서 해당 위치에 도달하는 경우
  - 검에 도달한 순간을 저장해두고, 해당 위치까지의 거리를 더해주면 최단거리가 될듯

"""

from collections import deque


def bfs():
    q = deque()
    q.append([0, 0])
    dist[0][0] = 0

    delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while q and dist[N-1][M-1] == -1:
        ny, nx = q.popleft()
        for dy, dx in delta:
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey < N and 0 <= ex < M:
                if dist[ey][ex] != -1:
                    continue
                if graph[ey][ex] != 1:
                    dist[ey][ex] = dist[ny][nx] + 1
                    q.append([ey, ex])


def from_gram_to_destination():
    global result
    if gy != -1 and gx != -1:
        if dist[gy][gx] != -1:
            result = dist[gy][gx] + ((N-1) - gy) + ((M-1) - gx)


N, M, T = map(int, input().split())
graph = []
gy, gx = -1, -1
for y in range(N):
    arr = list(map(int, input().split()))
    # 검 gram 위치 저장
    for x, num in enumerate(arr):
        if num == 2:
            gy = y
            gx = x
    graph.append(arr)
dist = [[-1 for _ in range(M)] for _ in range(N)]

result = int(1e9)
bfs()
from_gram_to_destination()
if dist[N-1][M-1] != -1:
    result = min(result, dist[N-1][M-1])
if result == -1 or result > T:
    print('Fail')
else:
    print(result)
