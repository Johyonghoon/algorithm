# 7562번 나이트의 이동
# https://www.acmicpc.net/problem/7562

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    L = int(input())
    sx, sy = map(int, input().split())
    endx, endy = map(int, input().split())

    visited = [[0 for _ in range(L)] for _ in range(L)]
    dist = [[0 for _ in range(L)] for _ in range(L)]
    q = deque()
    q.append([sy, sx])
    visited[sy][sx] = 1
    knight = [[2, -1], [2, 1], [1, -2], [1, 2], [-1, -2], [-1, 2], [-2, -1], [-2, 1]]

    while q:
        ny, nx = q.popleft()
        if ny == endy and nx == endx:
            break

        for dy, dx in knight:
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey < L and 0 <= ex < L:
                if visited[ey][ex]:
                    continue
                q.append([ey, ex])
                visited[ey][ex] = 1
                dist[ey][ex] = dist[ny][nx] + 1

    print(dist[endy][endx])



