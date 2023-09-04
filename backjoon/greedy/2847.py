# 2847번 게임을 만든 동준이
# https://www.acmicpc.net/problem/2847

import sys
input = sys.stdin.readline

N = int(input())
scores = []
for _ in range(N):
    scores.append(int(input()))

result = 0
for idx in range(N-2, -1, -1):
    while scores[idx] >= scores[idx+1]:
        scores[idx] -= 1
        result += 1

print(result)
