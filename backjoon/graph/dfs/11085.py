# 11085번 군사 이동
# https://www.acmicpc.net/problem/11085

"""
모든 길은 양방향, 각 길마다 너비가 존재하여 이에 비례하는 수의 군사가 지나갈 수 있다.
경로 상에 있는 길 중 너비가 가장 좁은 길의 너비를 최대화 하는 경로를 선택
수도 c에서 v로 향하는 경로 중 너비의 최소값이 가장 큰 경우를 찾는 문제
"""


import sys
import heapq
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(node, visited, mini):
    global result
    if result >= mini:
        return
    if node == v:
        result = max(result, mini)
        return

    for _width, nxt in sorted(edges[node], reverse=True):
        if nxt in visited:
            continue
        visited.add(nxt)
        dfs(nxt, visited, min(mini, _width))
        visited.remove(nxt)


p, w = map(int, input().split())
c, v = map(int, input().split())
edges = [[] for _ in range(p+1)]
for _ in range(w):
    p1, p2, width = map(int, input().split())
    edges[p1].append((width, p2))
    edges[p2].append((width, p1))
# print(edges)

result = 0
dfs(c, set(), int(1e9))
print(result)
