# 2666번 벽장문의 이동
# https://www.acmicpc.net/problem/2666

"""
# dfs
N : 벽장의 개수
door : 문, 문의 개수는 2개
M : 벽장 사용 개수
visit : 벽장 사용 순서
"""

import sys
from collections import deque

input = sys.stdin.readline


def dfs(node, d, cnt):
    global result
    if node == M:
        result = min(result, cnt)
        return

    target = visit[node]
    left = d[0]
    right = d[1]
    # print(target, left, right, cnt)
    if target < right:
        mv = abs(left - target)
        dfs(node+1, [target, right], cnt+mv)
    if target > left:
        mv = abs(target - right)
        dfs(node+1, [left, target], cnt+mv)


N = int(input())
door = sorted(list(map(int, input().split())))

M = int(input())
visit = []
for _ in range(M):
    visit.append(int(input()))

dist = [int(1e9) for _ in range(M)]
result = int(1e9)
dfs(0, door, 0)
print(result)
