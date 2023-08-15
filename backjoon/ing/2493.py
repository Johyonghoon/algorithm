# 2493번 탑
# https://www.acmicpc.net/problem/2493

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [0 for _ in range(N)]

stack = []
for idx in range(N):
    if stack:
        if arr[stack[-1]] > arr[idx]:
            result[idx] = idx
        else:
            stack.append(idx)
    else:
        stack.append(idx)

print(*result)