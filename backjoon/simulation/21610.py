# 21610번 마법사 상어와 비바라기
# https://www.acmicpc.net/problem/21610
# from pprint import pprint

"""
N*N 격자의 각 칸에는 바구니가 하나 있고, 저장할 수 있는 물의 양은 제한이 없다.
격자의 경계선에는 반대쪽 칸과 연결되어 있다. 즉, N번 행 아래에는 1번 행이, 1번 행 위에는 N번 행이 존재한다.
비바라기 시전 시 (N-1, 0) (N-1, 1) (N-2, 0) (N-2, 1)에 비구름이 생긴다.
이제 구름에 이동을 N번 명령하는데 i번째 명령은 방향 di와 거리 si로 이루어져 있다.
방향은 상하좌우대각선의 8개 방향이 존재한다.
순서는 (0, -1) (-1, -1) (-1, 0) (-1, 1) (0, 1) (1, 1) (1, 0) (1, -1)

이동을 명령하면 다음 순서대로 진행
1. 모든 구름이 di 방향으로 si칸 이동
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가
3. 구름이 모두 사라진다.
4. 2에서 물이 증가한 칸 (r, c)에 물복사 버그 마법을 시전
    - 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 (r, c) 위치의 바구니의 물의 양 증가
    - 이때는 경계에 있는 칸에 대해서 연결된 칸의 범위를 포함하지 않는다.
5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
    - 이때, 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.

M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 합
"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

clouds = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
# 방향의 번호를 사용하기 위해 0번 인덱스 비우기
direction = [0, (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
# 구름이 이동한 후 4개 방향의 물을 확인하는 delta
delta = [[1, 1], [1, -1], [-1, 1], [-1, -1]]
for _ in range(M):
    d, s = map(int, input().split())
    # 이동한 좌표 정보
    rainy = []
    for y, x in clouds:
        ey = (N + y + direction[d][0] * s) % N
        ex = (N + x + direction[d][1] * s) % N
        rainy.append((ey, ex))

    visited = [[0 for _ in range(N)] for _ in range(N)]
    for y, x in rainy:
        graph[y][x] += 1
        visited[y][x] = 1

    # 미리 계산해버리면, 계산한 결과에 의해 이후에 계산하는 결과가 달라질까봐,,,
    # 생각해보면 또 아닐 것 같은데 일단 유지
    add_water_info = []
    for y, x in rainy:
        cnt = 0
        for dy, dx in delta:
            ey = y + dy
            ex = x + dx
            if 0 <= ey < N and 0 <= ex < N:
                if graph[ey][ex]:
                    cnt += 1
        add_water_info.append((y, x, cnt))

    # 계산한 값을 더해주기
    for y, x, water in add_water_info:
        graph[y][x] += water

    new_clouds = []
    for y in range(N):
        for x in range(N):
            if graph[y][x] >= 2:
                if not visited[y][x]:
                    graph[y][x] -= 2
                    new_clouds.append((y, x))

    clouds = new_clouds

    # pprint(graph)

result = 0
for y in range(N):
    for x in range(N):
        result += graph[y][x]

print(result)
