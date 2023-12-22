# 16562번 친구비
# https://www.acmicpc.net/problem/16562

"""
노드가 연결된 정보를 찾아, 해당 그룹의 가장 적은 코스트를 판단하기
"""

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def dfs(node, prv, mini):
    visited[node] = 1
    mini = min(mini, cost[node])
    for nxt in edges[node]:
        if nxt == prv:
            continue
        if visited[nxt]:
            continue
        mini = dfs(nxt, node, mini)
    return mini


N, M, k = map(int, input().split())
cost = list(map(int, input().split()))
edges = [[] for _ in range(N)]
for _ in range(M):
    v, w = map(int, input().split())
    v, w = v-1, w-1
    edges[v].append(w)
    edges[w].append(v)

visited = [0 for _ in range(N)]
INF = int(1e9)
result = 0
for idx in range(N):
    if visited[idx]:
        continue
    result += dfs(idx, -1, INF)

# 문제좀 읽어라
if result > k:
    print("Oh no")
else:
    print(result)
