# 16929번 Two Dots
# https://www.acmicpc.net/problem/16929

"""
모든 k개의 점은 서로 다르다
k는 4보다 크거나 같다
모든 점의 색은 같다
모든 1 <= i <= k-1 에 대해서 di와 di+1 은 인접하다.
또, dk와 d1도 인접해야 한다. 두 점이 인접하다는 것은 각각의 점이 들어있는 칸이 변을 공유한다는 의미다.
"""


def recur(ny, nx, prvy, prvx, c):
    global isCycle
    visited[ny][nx] = 1

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < N and 0 <= ex < M:
            if visited[ey][ex]:
                if ey == sy and ex == sx:
                    if prvy != sy and prvx != sx:
                        isCycle = True
                continue
            if graph[ey][ex] == c:
                recur(ey, ex, ny, nx, c)



N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
isCycle = False
for y in range(N):
    for x in range(M):
        color = graph[y][x]
        sy, sx = y, x
        visited = [[0 for _ in range(M)] for _ in range(N)]
        recur(y, x, -1, -1, color)
        if isCycle:
            break
    if isCycle:
        break

if isCycle:
    print("Yes")
else:
    print("No")
