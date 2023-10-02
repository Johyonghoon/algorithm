# 9205번 맥주 마시면서 걸어가기
# https://www.acmicpc.net/problem/9205

"""
50미터마다 맥주를 한 병 마셔야 한다. 맥주는 최대 20개를 들고 이동할 수 있다.
20개 맥주가 들어 있는 한 박스를 들고 이동하며, 편의점에서 맥주를 최대 20개까지 구매할 수 있다.
집에서 펜타포스까지 맥주가 떨어지지 않고 갈 수 있다면 happy, 아니라면 sad 를 출력한다.

완전탐색
최종 목적지와 방문할 수 있는 편의점의 좌표를 한 배열에 저장하고,
모든 좌표를 방문할 수 있을 때 방문하고 지나가며 최종 목적지에 도달할 수 있다면 해피를 출력
# 시간 초과 : dfs
각 좌표에 대해 이동 가능한 좌표를 미리 정렬해두고 탐색
# BFS
"""

import sys
from collections import deque

input = sys.stdin.readline


T = int(input())
for tc in range(T):
    N = int(input())

    coordinate = []
    # 0번 노드에서 마지막 노드로 탐색할 수 있게,,,
    sx, sy = map(int, input().split())
    coordinate.append((sy, sx))
    for _ in range(N):
        # 계산하기 쉽게 (y, x) 형태로 저장
        x, y = map(int, input().split())
        coordinate.append((y, x))
    # 목적지 정보는 따로 저장
    desx, desy = map(int, input().split())
    coordinate.append((desy, desx))

    # 연결 노드 저장
    edges = [[] for _ in range(N+2)]
    for i in range(N+2):
        for j in range(i+1, N+2):
            ay, ax = coordinate[i]
            by, bx = coordinate[j]
            if abs(ay - by) + abs(ax - bx) <= 1000:
                edges[i].append(j)
                edges[j].append(i)

    # print(edges)
    visited = [0 for _ in range(N+2)]
    q = deque()
    q.append(0)
    visited[0] = 1
    isHappy = False

    # BFS
    while q:
        # print(q, visited)
        node = q.popleft()
        for nxt in edges[node]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            q.append(nxt)

    if visited[N+1]:
        print("happy")
    else:
        print("sad")
