# 15903번 카드 합체 놀이
# https://www.acmicpc.net/problem/15903

"""
카드 합체 규칙
1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산 (x != y)
2. 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.

가진 수들 중 가장 작은 두 수를 구하여 합을 다시 카드에 삽입하는 방식이므로,
최소 힙을 사용해보면 어떨까...
"""

import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

pq = numbers
heapq.heapify(pq)

while m:
    num1 = heapq.heappop(pq)
    num2 = heapq.heappop(pq)

    heapq.heappush(pq, num1+num2)
    heapq.heappush(pq, num1+num2)

    m -= 1

print(sum(pq))
