# 2468번 안전 영역
# https://www.acmicpc.net/problem/2468

"""
1. 가장 높은 지점을 기준으로 수위를 낮추며 잠기지 않는 안전 영역을 확인하고
2. 안전 영역의 개수가 감소하는 시점부터 중단
"""
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(ny, nx, h):
    visited[ny][nx] = 1

    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey, ex = ny + dy, nx + dx
        if 0 <= ey < N and 0 <= ex < N:
            if visited[ey][ex] or graph[ey][ex] <= h:
                continue
            recur(ey, ex, h)


# 영역 정보 입력
N = int(input())
graph = []
maxi = 0    # 최대 지역 높이 업데이트
for _ in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    maxi = max(maxi, max(arr))

result = 0
# 물의 높이는 문제 조건에 포함되지 않음
for height in range(maxi, -1, -1):
    cnt = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # 방문처리 되었거나, 물에 잠긴 좌표라면 넘어가며 dfs로 안전영역 탐색
    for y in range(N):
        for x in range(N):
            if visited[y][x] or graph[y][x] <= height:
                continue
            cnt += 1
            recur(y, x, height)

    # 안전영역는 점점 증가하다가 하나의 안전영역로 합쳐져 개수가 감소하게 될 것
    if result <= cnt:
        result = cnt

print(result)

"""
5
5 5 5 5 5
5 1 2 3 5
5 3 4 2 5
5 3 2 1 5
5 5 5 5 5
"""