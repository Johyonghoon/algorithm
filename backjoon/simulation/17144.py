# 17144번 미세먼지 안녕!
# https://www.acmicpc.net/problem/17144

"""
R * C 격자판
공기청정기는 항상 1번 열에 설치, 크기는 두 행을 차지
공기청정기가 설치되어 있지 않은 칸에 미세먼지가 있다.
1초동안 아래의 일이 순서대로 일어난다.
1. 미세먼지가 확산. 확산은 미세먼지가 있는 모든 칸에 동시에 발생
  - (r, c)에 있는 미세먼지는 인접한 네 방향으로 확산
  - 인접한 방향에 공기청정기가 있거나, 칸이 없으면 그 방향으로는 확산이 일어나지 않는다.
  - 확산되는 양은 graph[R][C]/5 이고 소수점은 버린다.
  - (r, c)에 남은 미세먼지의 양은 graph[R][C] - graph[R][C]/5 * 확산된 방향의 개수
2. 공기청정기 작동
  - 공기청정기에서 바람이 나온다.
  - 위쪽 공기청정기의 바람은 반시계 방향으로 순환, 아래쪽 바람은 시계방향으로 순환
  - 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
  - 공기청정기에서 부는 바람은 미세먼지가 없는 바람, 공기청정기로 들어간 미세먼지는 모두 정화

T초가 지난 후 방에 남아있는 미세먼지의 양
"""

import math
# from pprint import pprint


def diffusion():
    # 확산이 동시에 발생하기 때문에 확산량을 미리 계산하고 확산시키기
    change = [[0 for _ in range(C)] for _ in range(R)]
    for ny in range(R):
        for nx in range(C):
            if graph[ny][nx] == 0 or graph[ny][nx] == -1:
                continue
            # 확산되는 양
            diff = math.floor(graph[ny][nx] / 5)
            for dy, dx in delta:
                ey = ny + dy
                ex = nx + dx
                if 0 <= ey < R and 0 <= ex < C:
                    # 공기청정기가 있다면 패스
                    if graph[ey][ex] == -1:
                        continue
                    change[ey][ex] += diff
                    change[ny][nx] -= diff
    # pprint(change)
    # 확산
    for ny in range(R):
        for nx in range(C):
            graph[ny][nx] += change[ny][nx]
    # print("diffusion")
    # pprint(graph)


def clean():
    # 반시계 방향 움직임 (우, 상, 좌, 하)
    up_y, up_x = cleaner[0]
    # 다시 원래대로 돌아올 때까지 작동
    direction = 0
    # 반시계방향으로 이동하니까, 시계방향으로 땡겨오는걸로 할까
    clockwise = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    # 공기청정기 위 좌표부터 시작 // 가장 윗칸으로부터 2칸 이상 떨어져 있기 때문에 인덱스 에러 미발생
    ny, nx = up_y-1, up_x
    while True:  # 공기청정기 우측까지 왔다면 종료(공기청정기 좌표정보를 땡겨오면 안되기 때문)
        # 방향 이동
        dy, dx = clockwise[direction]
        ey = ny + dy
        ex = nx + dx
        # 더이상 이동할 수 없다면 방향 변경 // y축이 공기청정기 커버 범위를 넘어서는 것을 방지하기 위해 ey == up_y-1 사용
        if ey < 0 or ey == up_y+1 or ex < 0 or ex >= C:
            direction += 1
            dy, dx = clockwise[direction]
            ey = ny + dy
            ex = nx + dx
        # 만약 가져와야 하는 좌표가 공기청정기의 좌표라면 종료
        if graph[ey][ex] == -1:
            # 공기청정기가 밀어내니 0이 된다.
            graph[ny][nx] = 0
            break
        # 해당 좌표의 미세먼지 가져오기
        graph[ny][nx] = graph[ey][ex]
        ny, nx = ey, ex

    # 시계방향 움직임
    down_y, down_x = cleaner[1]
    # 다시 원래대로 돌아올 때까지 작동
    direction = 0
    # 반시계방향으로 미세먼지 땡겨오기
    counterclockwise = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # 공기청정기 아래 좌표부터 시작 // 가장 아래칸으로부터 2칸 이상 떨어져 있기 때문에 인덱스 에러 미발생
    ny, nx = down_y+1, down_x
    while True:  # 공기청정기 우측까지 왔다면 종료(공기청정기 좌표정보를 땡겨오면 안되기 때문)
        # 방향 이동
        dy, dx = counterclockwise[direction]
        ey = ny + dy
        ex = nx + dx
        # 더이상 이동할 수 없다면 방향 변경 // y축이 공기청정기 커버 범위를 넘어서는 것을 방지하기 위해 ey == down_y-1 사용
        if ey >= R or ey == down_y-1 or ex < 0 or ex >= C:
            direction += 1
            dy, dx = counterclockwise[direction]
            ey = ny + dy
            ex = nx + dx
        # 만약 가져와야 하는 좌표가 공기청정기의 좌표라면 종료
        if graph[ey][ex] == -1:
            graph[ny][nx] = 0
            break
        # 해당 좌표의 미세먼지 가져오기
        graph[ny][nx] = graph[ey][ex]
        ny, nx = ey, ex
    # print("clean")
    # pprint(graph)


delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
R, C, T = map(int, input().split())
graph = []
cleaner = []
for y in range(R):
    arr = list(map(int, input().split()))
    graph.append(arr)
    for x, num in enumerate(arr):
        if num == -1:
            cleaner.append((y, x))
# pprint(graph)

while T:
    diffusion()
    clean()
    # 1초가 지나갔다.
    T -= 1

result = 0
for y in range(R):
    for x in range(C):
        if graph[y][x] == -1:
            continue
        result += graph[y][x]

print(result)