# 1063번 킹
# https://www.acmicpc.net/problem/1063
import numpy as np


"""
행은 가장 아래가 1, 가장 위가 8...
상하반전을 좌표를 변경해주는 과정에서 해주자.
"""


def find_coordinate(x):
    nx, ny = list(x)
    nx = ord(nx) - ord("A")
    # 행의 가장 아래가 1이므로 상하반전을 위해
    ny = 8 - int(ny)
    return nx, ny


def return_coordinate(nx, ny):
    x = chr(nx + ord("A"))
    # 원복시킬 때 상하반전을 고려해야 함
    coordinate = x + str(8 - ny)
    return coordinate


# 좌표 정보 입력
KING, STONE, N = input().split()
kx, ky = find_coordinate(KING)
sx, sy = find_coordinate(STONE)

# 말 이동
for idx in range(int(N)):
    command = input()
    # print(ky, kx, sy, sx)

    if command == "R":
        if kx < 8-1:
            if sx == kx+1 and sy == ky:
                if sx < 8-1:
                    kx += 1
                    sx += 1
                else:
                    continue
            else:
                kx += 1

    if command == "L":
        if kx > 0:
            if sx == kx-1 and sy == ky:
                if sx > 0:
                    kx -= 1
                    sx -= 1
                else:
                    continue
            else:
                kx -= 1

    if command == "B":
        if ky < 8-1:
            if sy == ky+1 and sx == kx:
                if sy < 8-1:
                    ky += 1
                    sy += 1
                else:
                    continue
            else:
                ky += 1

    if command == "T":
        if ky > 0:
            if sy == ky-1 and sx == kx:
                if sy > 0:
                    ky -= 1
                    sy -= 1
                else:
                    continue
            else:
                ky -= 1

    if command == "RT":
        if kx < 8-1 and ky > 0:
            if sx == kx+1 and sy == ky-1:
                if sx < 8-1 and sy > 0:
                    kx += 1
                    sx += 1
                    ky -= 1
                    sy -= 1
                else:
                    continue
            else:
                kx += 1
                ky -= 1

    if command == "LT":
        if kx > 0 and ky > 0:
            if sx == kx-1 and sy == ky-1:
                if sx > 0 and sy > 0:
                    kx -= 1
                    sx -= 1
                    ky -= 1
                    sy -= 1
                else:
                    continue
            else:
                kx -= 1
                ky -= 1

    if command == "RB":
        if kx < 8-1 and ky < 8-1:
            if sx == kx+1 and sy == ky+1:
                if sx < 8-1 and sy < 8-1:
                    kx += 1
                    sx += 1
                    ky += 1
                    sy += 1
                else:
                    continue
            else:
                kx += 1
                ky += 1

    if command == "LB":
        if kx > 0 and ky < 8-1:
            if sx == kx-1 and sy == ky+1:
                if sx > 0 and sy < 8-1:
                    kx -= 1
                    sx -= 1
                    ky += 1
                    sy += 1
                else:
                    continue
            else:
                kx -= 1
                ky += 1

    # graph = [[0 for _ in range(8)] for _ in range(8)]
    # graph[ky][kx] = 1
    # graph[sy][sx] = 1
    #
    # print("#", idx)
    # print(np.array(graph))

# 좌표 변경 및 출력
print(return_coordinate(kx, ky))
print(return_coordinate(sx, sy))
