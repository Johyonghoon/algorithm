# 2589번 보물섬
# https://www.acmicpc.net/problem/2589
import numpy as np
import sys
input = sys.stdin.readline
from collections import deque

height, length = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(height)]
result = 0

# 보물은 서로 간 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 두 곳에 위치
for y in range(height):
    for x in range(length):
        # 육지로만 이동 가능
        if graph[y][x] == "L":
            # (x, y) 좌표에서 이동할 때의 최단 거리
            distance = [[0 for _ in range(length)] for _ in range(height)]
            visited = [[False for _ in range(length)] for _ in range(height)]

            q = deque()
            q.append([y, x])

            while q:
                ey, ex = q.popleft()
                visited[ey][ex] = True
                for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    ny, nx = ey - dy, ex - dx

                    if 0 <= ny < height and 0 <= nx < length:
                        if graph[ny][nx] == "L":
                            if not visited[ny][nx]:
                                distance[ny][nx] = distance[ey][ex] + 1
                                q.append([ny, nx])
                        result = max(result, distance[ny][nx])

print(result)
