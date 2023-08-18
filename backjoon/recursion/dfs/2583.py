# 2583번 영역 구하기
# https://www.acmicpc.net/problem/2583
from pprint import pprint

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(ny, nx, volume):
    # 방문 처리 // 면적 검사
    graph[ny][nx] = 1
    volume += 1

    # 사방 탐색
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        nxy, nxx = ny + dy, nx + dx
        if 0 <= nxy < M and 0 <= nxx < N:
            if graph[nxy][nxx]:
                continue
            volume = recur(nxy, nxx, volume)

    return volume


# 영역 그리기
M, N, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(M)]
for _ in range(K):
    ax, ay, bx, by = map(int, input().split())
    for ey in range(ay, by):
        for ex in range(ax, bx):
            graph[ey][ex] = 1

result = []
for y in range(M):
    for x in range(N):
        if graph[y][x]:
            continue
        # 이동할 좌표 정보와 면적 정보를 재귀로 방문
        vol = recur(y, x, 0)
        result.append(vol)


result.sort()
# 영역의 개수와 면적을 출력
print(len(result))
print(*result)
