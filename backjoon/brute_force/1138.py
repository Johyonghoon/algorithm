# 1138번 한 줄로 서기
# https://www.acmicpc.net/problem/1138

"""
완전 탐색
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def recur(node, arr):
    if node == N:
        print(*arr)
        return

    # print(node, arr)
    for nxt in range(1, N+1):
        if visited[nxt]:
            continue

        cnt = 0
        for idx in arr:
            if idx > nxt:
                cnt += 1
        # print(nxt, cnt, ls[nxt-1])

        if cnt == ls[nxt-1]:
            visited[nxt] = 1
            arr.append(nxt)
            recur(node+1, arr)
            arr.pop()
            visited[nxt] = 0


N = int(input())
ls = list(map(int, input().split()))

visited = [0 for _ in range(N+1)]
visited[0] = 1

recur(0, [])
