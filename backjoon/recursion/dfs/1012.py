# 1012번 유기농 배추
# https://www.acmicpc.net/problem/1012

"""
1. dfs로 밭을 기준으로 인접 배추에 방문 처리하며 개수 확인
2. 배추 밭에 배추가 심어진 경우 1, 아닌 경우 0을 입력
3. 방문할 때마다 배추를 확인한 것이므로 0으로 변경
"""

import sys
sys.setrecursionlimit(int(1e9))


def recur(ny, nx):
    graph[ny][nx] = 0

    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey, ex = ny + dy, nx + dx
        if 0 <= ey < N and 0 <= ex < M:
            if not graph[ey][ex]:
                continue
            recur(ey, ex)


T = int(input())
for tc in range(1, T+1):
    # 배추 밭 정보 입력
    M, N, K = map(int, input().split())
    graph = [[0 for _ in range(M)] for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        graph[y][x] = 1

    # 최소의 배추흰지렁이 마리 수를 기록할 변수 초기화
    cnt = 0
    for y in range(N):
        for x in range(M):
            if not graph[y][x]:  # 배추가 아니거나, 이미 방문한 경우 0이므로 0일 경우 넘어가기
                continue
            cnt += 1
            recur(y, x)

    print(cnt)