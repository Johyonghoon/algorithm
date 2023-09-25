# 1976번 여행 가자
# https://www.acmicpc.net/problem/1976

"""
계획한 한 도시에서 dfs 탐색하며 계획에 있는 모든 도시를 탐색한다면 성공
즉 dfs
도시의 번호는 1번부터 시작한다.
"""


import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node):
    visited[node] = 1

    for nxt in edges[node]:
        if visited[nxt]:
            continue
        recur(nxt)


N = int(input())
M = int(input())

edges = [[] for _ in range(N+1)]
for idx in range(1, N+1):
    arr = list(map(int, input().split()))
    for j, num in enumerate(arr):
        if num:
            edges[idx].append(j+1)

plan = list(map(int, input().split()))
visited = [0 for _ in range(N+1)]

recur(plan[0])

isTrue = True
for city in plan:
    if not visited[city]:
        isTrue = False
        break

# print(visited)
if isTrue:
    print("YES")
else:
    print("NO")
