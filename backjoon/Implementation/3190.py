# 3190번 뱀
# https://www.acmicpc.net/problem/3190

# from pprint import pprint

"""
Dummy 게임
뱀은 맨 위, 맨 좌측에 위치, 뱀의 길이 1, 뱀의 처음 방향 오른쪽
뱀의 이동 규칙
- 뱀은 몸길이를 늘려 머리를 다음 칸에 위치
- 만약 이동한 칸에 벽이나 자기 자신의 몸이 있다면 게임 종료
- 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않음
- 만약 이동한 칸에 사과가 없다면, 꼬리가 위치한 칸의 몸통이 사라짐
방향 전환 횟수 L
다음 L개의 줄에 X초가 끝난 뒤에 회전하는 방향 C(L: 왼쪽, D: 오른쪽) 정보가 주어짐

ㅇㄴ 1행 1열부터 시작 제발...
"""

import sys
from collections import deque
input = sys.stdin.readline


def move():
    global time, is_finished
    time += 1
    ny, nx = q[-1]
    ey = ny + directions[d][0]
    ex = nx + directions[d][1]
    if 0 <= ey < N and 0 <= ex < N:
        q.append((ey, ex))
        if graph[ey][ex] == 0:
            py, px = q.popleft()
            graph[py][px] = 0
            graph[ey][ex] = 9
        elif graph[ey][ex] == 1:
            graph[ey][ex] = 9
        elif graph[ey][ex] == 9:
            is_finished = True
    else:
        is_finished = True


N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

K = int(input())
for _ in range(K):
    r, c = map(lambda x: int(x)-1, input().split())
    graph[r][c] = 1

time = 0
q = deque()
q.append((0, 0))
graph[0][0] = 9
d = 0
directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]

is_finished = False
L = int(input())
for _ in range(L):
    sec, direction = input().strip().split()
    sec = int(sec)

    while time < sec and not is_finished:
        move()

    if is_finished:
        break

    # 방향 전환
    if direction == 'D':
        d = (d+1) % 4
    elif direction == 'L':
        d = (d-1) % 4

# print(d, time)
# pprint(graph)
while not is_finished:
    move()

print(time)
