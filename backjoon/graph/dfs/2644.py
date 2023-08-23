# 2644번 촌수계산
# https://www.acmicpc.net/problem/2644

"""
1. 간선의 가중치가 1인 트리에서 루트를 확인하는 사람으로 두고 dfs 탐색하여, 깊이 탐색
"""


import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node):
    global result, cnt
    visited[node] = 1

    if node == G:
        result = cnt
        return

    for nxt in edges[node]:
        if visited[nxt]:
            continue
        cnt += 1
        recur(nxt)
        cnt -= 1


n = int(input())
S, G = map(int, input().split())
m = int(input())
edges = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    edges[n1].append(n2)
    edges[n2].append(n1)

result = -1
cnt = 0
recur(S)

print(result)
