# 2630번 색종이 만들기
# https://www.acmicpc.net/problem/2630

"""
하얀 색종이 : 0
파란 색종이 : 1

지역변수는 재귀가 이루어져도 변하지 않는다...
"""

import sys
from pprint import pprint

input = sys.stdin.readline


def recur(node, ny, nx):
    # print("node, ny, nx", node, ny, nx)

    cnt_minus = 0
    cnt_zero = 0
    cnt_plus = 0

    for dy, dx in delta:
        ey = ny + dy * node
        ex = nx + dx * node
        # print("ey, ex", ey, ex)

        if node > 1:
            recur(node//2, ey, ex)

        if graph[ey][ex] == -1:
            cnt_minus += 1
        elif graph[ey][ex] == 1:
            cnt_plus += 1
        else:
            cnt_zero += 1
    else:
        if cnt_minus or (cnt_zero and cnt_plus):
            d[0] += cnt_zero
            d[1] += cnt_plus
            # 반드시 잘라야 함을 나타내기 위해
            graph[ny][nx] = -1
        if node == N // 2:
            if cnt_plus // 4:
                d[1] += 1
            elif cnt_zero // 4:
                d[0] += 1

    # pprint(graph)
    # print(ny, nx)
    # print(d[0], d[1])


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

d = {0: 0, 1: 0}
delta = [[0, 0], [0, 1], [1, 0], [1, 1]]
recur(N//2, 0, 0)

print(d[0])
print(d[1])

"""
2
1 1
1 1
"""