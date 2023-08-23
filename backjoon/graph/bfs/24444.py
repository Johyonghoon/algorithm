# 24444번 알고리즘 수업 - 너비 우선 탐색 1
# https://www.acmicpc.net/problem/24444

import sys
from collections import deque
input = sys.stdin.readline


def bfs():
    global cnt
    q = deque()
    q.append(R)

    cnt = 1
    visited[R] = 1
    result[R] = cnt

    while q:
        node = q.popleft()

        for nxt in edges[node]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            cnt += 1
            result[nxt] = cnt
            q.append(nxt)


N, M, R = map(int, input().split())
# dfs 때와 마찬가지로 정렬을 우선을 해준다.
arr = []
for _ in range(M):
    arr.append(list(map(int, input().split())))
arr.sort()
edges = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
result = [0 for _ in range(N+1)]
for u, v in arr:
    edges[u].append(v)
    edges[v].append(u)

bfs()

[print(i) for i in result[1:]]
