# 1967번 트리의 지름
# https://www.acmicpc.net/problem/1967

"""
# dfs
한 노드에서 가장 깊은 리프 노드를 찾아, 그 리프 노드를 기준으로 다시 가장 깊은 리프 노드 찾기
# 시간초과 :: DFS 리프 노드를 기준으로 DFS를 활용하여 가장 긴 깊이를 가진 노드의 거리 찾기
# 시간초과 :: DFS 각 노드를 루트로 두고, 리프까지의 거리가 가장 긴 2개의 길이의 합
"""
import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline


def dfs(node, prnt, l):
    global target, maxi
    if maxi < l:
        maxi = l
        target = node

    for nxt, weight in edges[node]:
        if nxt == prnt:
            continue
        dfs(nxt, node, l+weight)


N = int(input())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2, w = map(int, input().split())
    edges[n1].append([n2, w])
    edges[n2].append([n1, w])

maxi = 0
target = 0
# 가장 깊은 노드 찾기
dfs(1, 0, 0)
# 가장 깊은 노드를 기준으로 가장 깊은 노드 찾기
dfs(target, 0, 0)
print(maxi)
