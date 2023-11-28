# 11286번 절댓값 힙
# https://www.acmicpc.net/problem/11286

import sys
import heapq

input = sys.stdin.readline

N = int(input())
pq = []

for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(pq, (abs(x), x))
    else:
        if pq:
           print(heapq.heappop(pq)[1])
        else:
            print(0)
