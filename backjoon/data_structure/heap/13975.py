# 13975번 파일 합치기 3
# https://www.acmicpc.net/problem/13975

import sys
import heapq

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    numbers = list(map(int, input().split()))
    heapq.heapify(numbers)

    cost = 0
    while N > 1:
        n1 = heapq.heappop(numbers)
        n2 = heapq.heappop(numbers)
        heapq.heappush(numbers, n1+n2)
        cost += n1 + n2
        # print(numbers)
        N -= 1

    print(cost)
