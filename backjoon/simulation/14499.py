# 14499번 주사위 굴리기
# https://www.acmicpc.net/problem/14499

"""
일단 x, y 좌표 형태가 일반적으로 주어지는 형태와 반대이다.
주사위 정보가 계속해서 업데이트 되는데 어떻게 공간 정보를 이해할 수 있을까...
회전 시에 대한 주사위 좌표 변경을 계속 추적
"""
import sys
input = sys.stdin.readline


def turning_dice(dicection):
    global y, x, dice
    dy, dx = delta[dicection]
    ey = y + dy
    ex = x + dx
    # 이동할 수 있다면
    if 0 <= ey < N and 0 <= ex < M:
        # 주사위 회전하기
        turned_dice = [0, 0, 0, 0, 0, 0]
        for idx in range(6):
            turned_dice[idx] = dice[turn[dicection][idx]]
        dice = turned_dice

        # 좌표 변경 후 윗면 출력
        y, x = ey, ex
        print(dice[1])

        # 만약 해당 좌표에 값이 있다면 칸에 쓰여 있는 숫자가 주사위로 복사되고, 좌표의 값은 0이 된다.
        if graph[y][x]:
            dice[3] = graph[y][x]
            graph[y][x] = 0
        # 해당 좌표에 값이 없다면 주사위 아랫면의 숫자가 좌표에 복사
        else:
            graph[y][x] = dice[3]


#        동       서       북        남
delta = [[], [0, 1], [0, -1], [-1, 0], [1, 0]]
#       N  U  S  D  W  E
#  idx  0  1  2  3  4  5
dice = [0, 0, 0, 0, 0, 0]
turn = [
    [],
    [0, 4, 2, 5, 3, 1],     # E
    [0, 5, 2, 4, 1, 3],     # W
    [3, 0, 1, 2, 4, 5],     # N
    [1, 2, 3, 0, 4, 5]      # S
]

N, M, y, x, K = map(int, input().split())
graph = []
for _ in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)

moves = list(map(int, input().split()))
for move in moves:
    turning_dice(move)
