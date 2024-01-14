# 15662번 톱니바퀴 2
# https://www.acmicpc.net/problem/15662

"""
8개의 톱니를 가진 톱니바퀴 T개가 일렬로 놓여져 있다.
K번 회전 시킬 때 회전은 시계 방향과 반 시계 방향
톱니바퀴를 회전시키려면 회전 시킬 톱니바퀴와 회전 시킬 방향을 결정
톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라서 옆에 있는 톱니바퀴를 회전시킬 수 있고, 회전시키지 않을 수 있다.
톱니 A를 회전할 때, 그 옆에 있는 톱니바퀴 B와 서로 맞닿은 톱니의 극이 다르다면 B는 A가 회전한 방향과 반대 방향으로 회전

최종 톱니바퀴 상태 출력
"""

import sys
from collections import deque
input = sys.stdin.readline


def rotate(idx, d):
    # 시계 방향
    if d == 1:
        tmp = gears[idx].pop()
        gears[idx].appendleft(tmp)
    # 반시계 방향
    elif d == -1:
        tmp = gears[idx].popleft()
        gears[idx].append(tmp)


def compare_right(idx, d, rotated_gear):
    # 오른쪽 비교. 제일 우측 톱니가 아닐 때
    if idx < T-1:
        # 톱니 접점의 극이 다를 때
        if gears[idx][2] != gears[idx+1][6]:
            rotated_gear[idx+1] = -d
            # 회전했다면 그 반대 톱니도 확인
            compare_right(idx+1, -d, rotated_gear)
    return rotated_gear


def compare_left(idx, d, rotated_gear):
    # 왼쪽 비교. 제일 왼쪽 톱니가 아닐 때
    if idx > 0:
        # 톱니 접점의 극이 다를 때
        if gears[idx][6] != gears[idx-1][2]:
            rotated_gear[idx-1] = -d
            # 회전했다면 그 반대 톱니도 확인
            compare_left(idx-1, -d, rotated_gear)
    return rotated_gear


def compare(idx, d):
    rotated_gear = [0 for _ in range(T)]
    rotated_gear[idx] = d
    rotated_gear = compare_left(idx, d, rotated_gear)
    rotated_gear = compare_right(idx, d, rotated_gear)
    # print(rotated_gear)
    return rotated_gear


T = int(input())
gears = []
for _ in range(T):
    q = deque(map(int, list(input().strip())))    # 12시 방향부터 시계방향 순서로 주어진다.
    gears.append(q)
# print(gears)

K = int(input())
for _ in range(K):
    num, direction = map(int, input().split())
    num -= 1
    rotated = compare(num, direction)
    for idx, direc in enumerate(rotated):
        if direc:
            rotate(idx, direc)

result = 0
for gear in gears:
    if gear[0]:
        result += 1

print(result)
