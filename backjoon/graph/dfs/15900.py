# 15900번 나무 탈출
# https://www.acmicpc.net/problem/15900

"""
0. 트리의 모든 리프 노드에 게임말이 하나씩 놓여있는 채로 시작
1. 1번 정점을 루트 노드로 설정
2. 모든 리프 노드들의 높이를 파악하면 루트 노드까지 옮겨야 하는 말의 이동 수를 구할 수 있다.
3. 이동 수가 홀수일 경우 성원이가 이길 수 있다.
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node, cnt):
    global move
    # print(node, cnt)
    visited[node] = 1

    if node != 1 and len(edges[node]) == 1:
        move += cnt
        return

    for nxt in edges[node]:
        if visited[nxt]:
            continue
        recur(nxt, cnt+1)


N = int(input())
nodes = [0 for _ in range(N+1)]
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2 = map(int, input().split())
    edges[n1].append(n2)
    edges[n2].append(n1)


visited = [0 for _ in range(N+1)]
move = 0
recur(1, 0)

if move % 2:
    print("Yes")
else:
    print("No")
