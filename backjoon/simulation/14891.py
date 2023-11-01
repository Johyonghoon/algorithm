# 14891번 톱니바퀴
# https://www.acmicpc.net/problem/14891

"""
N극 0, S극 1
극이 다르다면, A가 회전한 방향과 반대로 B가 회전하게 된다.
맞닿은 톱니의 맞닿은 부분이 같은 극이라면 회전하지 않는다.
"""
from collections import deque


def turning(my_gear, direction):
    if direction == 1:  # 시계방향
        tmp = gears[my_gear].pop()
        gears[my_gear].appendleft(tmp)
    else:   # 반시계방향
        tmp = gears[my_gear].popleft()
        gears[my_gear].append(tmp)


# 전달받은 값은 회전할 경우의 방향
def compare_left(left, direction):
    # 왼쪽에 기어가 없다면 돌아가기
    if left == -1:
        return
    # 원래 기어와 비교해서 같다면 회전하지 않는다
    if gears[left][2] == gears[left+1][6]:
        return
    compare_left(left-1, -direction)
    turning(left, direction)


def compare_right(right, direction):
    if right == 4:
        return
    if gears[right][6] == gears[right-1][2]:
        return
    # 다음 톱니의 회전 방향을 전달
    compare_right(right+1, -direction)
    # 내 회전방향
    turning(right, direction)


gears = []
for _ in range(4):
    gears.append(deque(map(int, list(input()))))

K = int(input())
for _ in range(K):
    num, d = map(int, input().split())
    num -= 1
    compare_left(num-1, -d)
    compare_right(num+1, -d)
    turning(num, d)

# 결과값
# print(gears)
result = 0
for idx in range(4):
    result += gears[idx][0] * (2 ** idx)

print(result)
