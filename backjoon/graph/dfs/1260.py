# 1260번 DFS와 BFS
# https://www.acmicpc.net/problem/1260

import sys
from collections import deque
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node):
    global dfs_cnt
    dfs_visited[node] = 1
    dfs_result.append(node)

    for nxt in edges[node]:
        if dfs_visited[nxt]:
            continue

        dfs(nxt)


def bfs(start):
    q = deque()
    q.append(start)
    bfs_visited[start] = 1
    bfs_result.append(start)

    while q:
        node = q.popleft()

        for nxt in edges[node]:
            if bfs_visited[nxt]:
                continue
            bfs_visited[nxt] = 1
            bfs_result.append(nxt)
            q.append(nxt)


N, M, V = map(int, input().split())
edges = [[] for _ in range(N+1)]
bfs_visited = [0 for _ in range(N+1)]
dfs_visited = [0 for _ in range(N+1)]


for _ in range(M):
    n1, n2 = map(int, input().split())
    edges[n1].append(n2)
    edges[n2].append(n1)
    edges[n1].sort()
    edges[n2].sort()

dfs_result = []
bfs_result = []
dfs(V)
bfs(V)

print(*dfs_result)
print(*bfs_result)
