# 3187번 양치기 꿍
# https://www.acmicpc.net/problem/3187

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(ny, nx, wolf, sheep):
    visited[ny][nx] = 1

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < R and 0 <= ex < C:
            if visited[ey][ex]:
                continue

            if graph[ey][ex] == 9:
                continue
            elif graph[ey][ex] == 1:
                wolf += 1
            elif graph[ey][ex] == 2:
                sheep += 1

            wolf, sheep = dfs(ey, ex, wolf, sheep)

    return wolf, sheep


R, C = map(int, input().split())
graph = []
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
for _ in range(R):
    arr = list(map(int, list(input().strip()
               .replace(".", "0")
               .replace("#", "9")
               .replace("v", "1")
               .replace("k", "2"))))
    graph.append(arr)

visited = [[0 for _ in range(C)] for _ in range(R)]

result = [0, 0]
for y in range(R):
    for x in range(C):
        if visited[y][x]:
            continue
        v, k = dfs(y, x, 0, 0)
        if k > v:
            result[0] += k
        else:
            result[1] += v

print(*result)