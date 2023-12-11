# 20056번 마법사 상어와 파이어볼
# https://www.acmicpc.net/problem/20056

"""
N * N 격자에 파이어볼 M개 발사
가장 처음에 파이어볼은 각자 위치에서 이동을 대기
i번 파이어볼의 위치는 ri, ci, 질량은 mi, 방향은 di, 속력은 si
격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결, 1번 행은 N번 열과 연결
파이어볼 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미
7   0   1
6       2
5   4   3
direction = [[-1, 0], [-1, 1], [0, 1], [1, 1],  [1, 0], [1, -1], [0, -1], [-1, -1]]

파이어볼에게 이동을 명령하면 다음의 일이 일어난다.
1. 모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동
  - 이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
2. 이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
  1) 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
  2) 파이어볼은 4개의 파이어볼로 나누어진다.
  3) 나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다
    - 질량 : (합쳐진 파이어볼 질량의 합 / 5) 내림
    - 속력 : (합쳐진 파이어볼 속력의 합 / 합쳐진 파이어볼의 개수) 내림
    - 합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
    - 질량이 0인 파이어볼은 소멸되어 없어진다.
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합
"""

import sys
from collections import deque
input = sys.stdin.readline


def move_fireball(y, x, mass, speed, direction):
    dy, dx = directions[direction]
    ey = y + dy * speed
    ex = x + dx * speed
    ey %= N
    ex %= N
    return ey, ex


def command_move_fireballs(q):
    dic = dict()
    while q:
        ny, nx, nm, ns, nd = q.popleft()
        ey, ex = move_fireball(ny, nx, nm, ns, nd)
        coor = str(ey).zfill(2) + str(ex).zfill(2)
        if coor not in dic:
            dic[coor] = list()
        dic[coor].append([nm, ns, nd])

    new_fires = deque()
    for k, v in dic.items():
        ny = int(k[:2])
        nx = int(k[2:])
        # 2개 이상의 파이어볼이 존재할 때만 분리
        if len(v) < 2:
            new_fires.append([ny, nx] + v[0])
            continue
        cnt = 0
        total_mess = 0
        total_speed = 0
        cnt_odd = 0
        cnt_even = 0
        for nm, ns, nd in v:
            cnt += 1
            total_mess += nm
            total_speed += ns
            if nd % 2:
                cnt_odd += 1
            else:
                cnt_even += 1
        mess = total_mess // 5
        speed = total_speed // cnt
        if mess:  # 질량이 없는 경우 소멸
            # 모든 파이어볼이 모두 홀수나 짝수로 일치하지 않을 경우(2개 초과일 경우를 고려)
            if cnt_odd and cnt_even:  # 1, 3, 5, 7
                for i in [1, 3, 5, 7]:
                    new_fires.append([ny, nx, mess, speed, i])
            else:
                for i in [0, 2, 4, 6]:
                    new_fires.append([ny, nx, mess, speed, i])
    return new_fires


directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
N, M, K = map(int, input().split())

fires = deque()
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r -= 1
    c -= 1
    fires.append((r, c, m, s, d))

for _ in range(K):
    fires = command_move_fireballs(fires)

# print(fires)
result = 0
for _, _, mess, _, _ in fires:
    result += mess

print(result)
