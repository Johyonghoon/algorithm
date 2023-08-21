# 5464번 주차장
# https://www.acmicpc.net/problem/5464

import sys
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())
# 주차 공간의 단위 무게당 요금 정보
charge = [0 for _ in range(N+1)]
for idx in range(1, N+1):
    charge[idx] = int(input())
# 차량 무게 정보
weight = [0 for _ in range(M+1)]
for idx in range(1, M+1):
    weight[idx] = int(input())

# 주차장 빈 공간 정보
stack = list(range(N, 0, -1))
d = {}
total = 0
for _ in range(2*M):
    car = int(input())
    if car > 0:
        parking_num = stack.pop()
        d[car] = parking_num
        print(parking_num, car)
        print(charge)
        total += charge[parking_num] * weight[car]
    else:   # car < 0
        car = -car
        stack.append(d[car])
        stack.sort(reverse=True)

print(total)
