# 6593번 상범 빌딩
# https://www.acmicpc.net/problem/6593
# from pprint import pprint
import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    q = deque()
    z, y, x = start
    q.append(start)
    dist[z][y][x] = 0
    while q:
        nz, ny, nx = q.popleft()
        for dz, dy, dx in delta:
            ez = nz + dz
            ey = ny + dy
            ex = nx + dx
            if 0 <= ez < L and 0 <= ey < R and 0 <= ex < C:
                if dist[ez][ey][ex] != -1:
                    continue
                if cube[ez][ey][ex] == "." or cube[ez][ey][ex] == "E":
                    dist[ez][ey][ex] = dist[nz][ny][nx] + 1
                    q.append((ez, ey, ex))


while True:
    L, R, C = map(int, input().strip().split())
    if L == 0 and R == 0 and C == 0:
        break
    dist = [[[-1 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    delta = [[1, 0, 0], [-1, 0, 0], [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]]
    cube = []
    start = (0, 0, 0)  # L R C
    end = (L-1, R-1, C-1)
    for z in range(L):
        graph = []
        for y in range(R):
            arr = list(input().strip())
            for x, element in enumerate(arr):
                if element == "S":
                    start = (z, y, x)
                elif element == "E":
                    end = (z, y, x)
            graph.append(arr)
        cube.append(graph)
        input()

    bfs()

    # pprint(dist)
    if dist[end[0]][end[1]][end[2]] == -1:
        print("Trapped!")
    else:
        print(f"Escaped in {dist[end[0]][end[1]][end[2]]} minute(s).")
