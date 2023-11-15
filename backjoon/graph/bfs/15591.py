# 15591번 Mootube (silver)
# https://www.acmicpc.net/problem/15591

"""
# BFS : 통과
# DFS : 시간초과
K에 대한 정보를 기반으로 추천할 동영상의 개수를 묻는 질문을 Q개 답변하려면
최대 5000개이므로, 미리 각 좌표에 대한 거리를 탐색하는게 좋을 것 같다.
"""

import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


# def recur(start, node):
#     visited[node] = 1
#
#     for nxt, d in edges[node]:
#         if visited[nxt]:
#             continue
#         dist[start][nxt] = min(d, dist[start][node])
#         recur(start, nxt)


def bfs(start):
    q = deque()
    q.append((start, dist[start][start]))
    while q:
        node, weight = q.popleft()
        for nxt, w in edges[node]:
            if dist[start][nxt] == int(1e10):
                dist[start][nxt] = min(weight, w)
                q.append((nxt, dist[start][nxt]))


N, Q = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2, r = map(int, input().split())
    edges[n1].append((n2, r))
    edges[n2].append((n1, r))
# print(edges)

dist = [[int(1e10) for _ in range(N+1)] for _ in range(N+1)]

for idx in range(1, N+1):
    # recur(idx, idx)
    bfs(idx)

# print(dist)

for _ in range(Q):
    k, v = map(int, input().split())

    cnt = 0
    for j in range(1, N+1):
        if j == v:
            continue
        if dist[v][j] >= k:
            cnt += 1

    print(cnt)
