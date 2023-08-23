# 24479번 깊이 우선 탐색 1
# https://www.acmicpc.net/problem/24479

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node, cnt):
    visited[node] = 1
    cnt += 1
    result[node] = cnt

    for nxt in edges[node]:
        if visited[nxt]:
            continue
        cnt = recur(nxt, cnt)

    return cnt


N, M, R = map(int, input().split())

# 간선 정보를 오름차순으로 받기 때문에 미리 정렬 후 간선 배열을 생성하자
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

recur(R, 0)

[print(i) for i in result[1:]]

"""
5 5 1
1 4
4 2
2 3
3 5
3 5
"""