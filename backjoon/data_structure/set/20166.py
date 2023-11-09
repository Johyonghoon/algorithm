# 20166번 문자열 지옥에 빠진 호석
# https://www.acmicpc.net/problem/20166

import sys
from collections import deque, defaultdict

input = sys.stdin.readline


def bfs(ay, ax):
    q = deque()
    s = graph[ay][ax]
    q.append((ay, ax, s))

    while q:
        ny, nx, string = q.popleft()
        d[string] += 1

        # 델타 탐색
        for dy, dx in delta:
            ey = ny + dy
            ex = nx + dx
            # 행 이동
            if ey < 0:
                ey += N
            elif ey == N:
                ey = 0
            # 열 이동
            if ex < 0:
                ex += M
            elif ex == M:
                ex = 0

            if len(string) < 5:
                q.append((ey, ex, string+graph[ey][ex]))


N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input().strip()))

delta = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

# 해당 문자열이 나오는 경우의 수를 저장
d = defaultdict(int)

# 모든 경우의 수 탐색
for y in range(N):
    for x in range(M):
        bfs(y, x)

for _ in range(K):
    S = input().strip()
    print(d[S])
