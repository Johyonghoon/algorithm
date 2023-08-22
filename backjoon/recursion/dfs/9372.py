# 9372번 상근이의 여행
# https://www.acmicpc.net/problem/9372

"""
모든 국가를 방문하기 위한 최소 간선의 개수
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node):
    global cnt
    visited[node] = 1

    for nxt in edges[node]:
        # 이미 방문한 국가라면 패스
        if visited[nxt]:
            continue

        cnt += 1
        recur(nxt)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    edges = [[] for _ in range(N+1)]
    for _ in range(M):
        n1, n2 = map(int, input().split())
        edges[n1].append(n2)
        edges[n2].append(n1)

    mini = 10 ** 8

    # 모든 국가를 방문하기 위한 간선의 개수
    visited = [0 for _ in range(N+1)]
    cnt = 0
    recur(1)

    print(cnt)
