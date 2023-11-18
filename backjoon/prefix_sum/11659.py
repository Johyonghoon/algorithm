# 11659번 구간 합 구하기 4
# https://www.acmicpc.net/problem/11659

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))

prefix = [i for i in numbers]
for i in range(1, N+1):
    prefix[i] += prefix[i-1]
# print(prefix)

for _ in range(M):
    start, end = map(int, input().split())
    print(prefix[end] - prefix[start-1])
