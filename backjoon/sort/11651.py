# 11651번 좌표 정렬하기 2
# https://www.acmicpc.net/problem/11651

import sys

input = sys.stdin.readline


N = int(input())
arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((y, x))
arr.sort()
for x, y in arr:
    print(y, x)
