# 17779번 게리맨더링 2
# https://www.acmicpc.net/problem/17779

"""
N * N 격자 형태
다섯 개의 선거구로 나눠야 하고, 각 구역은 다섯 선거구 중 하나에 포함
선거구는 구역을 적어도 하나 포함, 한 선거구에 포함되어 있는 구역은 모두 연결

0 <= d1, d2
1 <= x < x + d1 + d2 < N
d1 + d2 < N - x
1 <= y - d1
y + d2 < N
"""

import sys
input = sys.stdin.readline

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

for y in range(1, N-1):
    for x in range(1, N-1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if d1 + d2 < N - x:
                    if 1 <= y - d1:
                        if y + d2 < N:
                            print(x, y, d1, d2)
