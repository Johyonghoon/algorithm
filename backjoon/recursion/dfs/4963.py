# 4963번 섬의 개수
# https://www.acmicpc.net/problem/4963

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

"""
1. dfs로 8방 탐색하며 연결된 땅을 확인하며 방문 처리
"""


def recur(ny, nx):
    # 방문 처리
    graph[ny][nx] = 0

    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]:
        ey, ex = ny + dy, nx + dx
        if 0 <= ey < h and 0 <= ex < w:
            if not graph[ey][ex]:
                continue
            recur(ey, ex)


while True:
    # 지도 정보 입력
    w, h = map(int, input().split())

    # 종료 조건
    if w == 0 and h == 0:
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int, input().split())))

    # 섬의 개수 초기화
    cnt = 0

    # dfs 탐색
    for y in range(h):
        for x in range(w):
            if not graph[y][x]:
                continue
            cnt += 1
            recur(y, x)

    # 섬의 개수 출력
    print(cnt)
