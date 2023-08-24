# 10431번 줄세우기
# https://www.acmicpc.net/problem/10431

import sys
input = sys.stdin.readline

P = int(input())
for _ in range(P):
    arr = list(map(int, input().split()))
    tc = arr[0]
    students = arr[1:]

