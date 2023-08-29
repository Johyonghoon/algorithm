# 11403번 경로 찾기
# https://www.acmicpc.net/problem/11403

import sys
from collections import deque
input = sys.stdin.readline


def recur(node):
    visited[node] = 1

    for nxt in edges[node]:
        if visited[nxt]:
            continue
        recur(nxt)


N = int(input())
edges = [[] for _ in range(N)]
for i in range(N):
    arr = list(map(int, input().split()))
    for j, isTrue in enumerate(arr):
        if isTrue:
            edges[i].append(j)

result = []
for idx in range(N):
    visited = [0 for _ in range(N)]
    q = deque()
    q.append(idx)

    # 자기 자신으로 다시 돌아오는 지를 확인하기 위해 방문처리를 미리 하지 않음
    while q:
        node = q.popleft()

        for nxt in edges[node]:
            if visited[nxt]:
                continue
            q.append(nxt)
            visited[nxt] = 1

    result.append(visited)


[print(*i) for i in result]

