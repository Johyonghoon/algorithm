# 2012번 등수 매기기
# https://www.acmicpc.net/problem/2012

import sys
input = sys.stdin.readline

N = int(input())
ranks = []
for _ in range(N):
    ranks.append(int(input()))

ranks.sort()

result = 0
for idx, rank in enumerate(ranks):
    result += abs(rank-1 - idx)

# print(ranks)
print(result)
