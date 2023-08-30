# 14503번 로봇 청소기
# https://www.acmicpc.net/problem/14503
import numpy as np


def turn(direction):
    direction -= 1
    if direction < 0:
        direction = 3
    return direction


N, M = map(int, input().split())
# (ny, nx) : 로봇 청소기 좌표 // d : 0 = 북쪽 1 = 동쪽 2 = 남쪽 3 = 서쪽
ny, nx, d = map(int, input().split())
graph = []
for _ in range(N):
    # 값이 0인 경우 청소되지 않은 빈칸, 1인 경우 벽이 있는 것
    # 로봇 청소기가 있는 칸은 항상 빈 칸
    graph.append(list(map(int, input().split())))

cnt = 0
coordinate_d = [[-1, 0], [0, 1], [1, 0], [0, -1]]

while True:
    if graph[ny][nx] == 0:
        cnt += 1
        graph[ny][nx] = -1

    for idx in range(4):
        d = turn(d)
        dy, dx = coordinate_d[d]
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < M and 0 <= ex < N:
            if graph[ey][ex] == 0:
                ny = ey
                nx = ex
                print(ny, nx)
                print(np.array(graph))
                break
    # 4방향을 모두 탐색했을 때
    else:
        dy, dx = coordinate_d[d-2]
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < N and 0 <= ex < M:
            if graph[ey][ex] == 1:
                break
            else:
                ny = ey
                nx = ex
        else:
            break

print(cnt)
