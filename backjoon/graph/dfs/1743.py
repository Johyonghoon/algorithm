# 1743번 음식물 피하기
# https://www.acmicpc.net/problem/1743

# DFS 탐색으로 최대 개수를 구한다.
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(ny, nx, cnt):
    visited[ny][nx] = 1
    cnt += 1

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < N and 0 <= ex < M:
            if visited[ey][ex]:
                continue
            if graph[ey][ex]:
                cnt = recur(ey, ex, cnt)

    # print(ny, nx, cnt)
    return cnt


N, M, K = map(int, input().split())
graph = [[0 for _ in range(M)] for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

result = 0
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for y in range(N):
    for x in range(M):
        if visited[y][x]:
            continue
        if graph[y][x]:
            result = max(result, recur(y, x, 0))

print(result)
