# 17142번 연구소 3
# https://www.acmicpc.net/problem/17142

"""
# BFS + @
주어진 바이러스에서 M개의 바이러스를 선택하여 활성화 시킬 때 모든 빈 칸에 바이러스가 있게 되는 최소 시간
주어진 바이러스 개수 중 M개의 바이러스를 선택하여 모두 탐색하는 방법은 시간초과에 걸릴 것 같다.
각 바이러스 위치에서 매 시간 탐색 결과를 확인하여 모든 좌표가 채워질 때 마지막으로 채워진 좌표에 영향을 끼치는 바이러스를 반드시 포함하면 될까
"""

from pprint import pprint

import sys
from collections import deque

input = sys.stdin.readline


def bfs(q):
    while q:
        ny, nx = q.popleft()
        for dy, dx in delta:
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey < N and 0 <= ex < N:
                if dist[ey][ex] == -1:
                    dist[ey][ex] = dist[ny][nx] + 1
                    q.append((ey, ex))
    return q


N, M = map(int, input().split())
dist = []
virus = deque()
for y in range(N):
    arr = list(map(int, input().split()))
    for x in range(N):
        if arr[x] == 0:
            arr[x] = -1
        elif arr[x] == 1:
            arr[x] = -2
        elif arr[x] == 2:
            virus.append((y, x))
            arr[x] = 0
    dist.append(arr)

virus_dist = []
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
for idx in range(len(virus)):
    bfs(virus[idx])
