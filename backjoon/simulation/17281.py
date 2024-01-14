# 17281번 야구
# https://www.acmicpc.net/problem/17281

"""
야구는 9명으로 이루어진 두 팀이 공격과 수비를 번갈아 하는 게임
하나의 이닝은 공격과 수비로 이루어져 있고, 총 N이닝 동안 게임을 진행
한 이닝에 3아웃이 발생하면 이닝이 종료, 두 팀이 공격과 수비를 서로 바꾼다.

타순을 설정하면 변경할 수 없다.
3아웃이 발생하지 않은 상태라면 이닝은 끝나지 않고 1번 타자가 다시 타석에 선다.

- 1 : 안타: 타자와 모든 주자가 한 루씩 진루
- 2 : 2루타 : 타자와 모든 주자가 두 루씩 진루
- 3 : 3루타 : 타자와 모든 주자가 세 루씩 진루
- 4 : 홈런 : 타자와 모든 주자가 홈까지 진루
- 0 : 아웃 : 모든 주자는 진루하지 못하고, 공격 팀에 이웃이 하나 증가

9명의 타순을 결정하면 8!의 경우의 수

"""

import sys
from itertools import permutations
input = sys.stdin.readline


def simulation(b):
    global result
    score = 0
    inning = 0
    order = 0
    while inning < innings:
        out_count = 0
        first = 0
        second = 0
        third = 0
        while out_count < 3:
            # 타자가 안타 또는 홈런을 쳤을 때
            anta = rbis[inning][b[order]]
            if anta == 1:
                score += third
                third, second, first = second, first, 1
            elif anta == 2:
                score += third + second
                third, second, first = first, 1, 0
            elif anta == 3:
                score += third + second + first
                third, second, first = 1, 0, 0
            elif anta == 4:
                score += third + second + first + 1
                third, second, first = 0, 0, 0
            # 아웃
            else:
                out_count += 1

            # 주자 변경
            order = (order + 1) % 9

        # out count가 3일 경우 이닝 종료
        inning += 1

    result = max(result, score)


innings = int(input())
rbis = []
for _ in range(innings):
    rbis.append(list(map(int, input().split())))

result = 0
for p in permutations(range(1, 9), 8):
    batting_order = list(p)
    # print(batting_order[:3]+[0]+batting_order[3:])
    simulation(batting_order[:3]+[0]+batting_order[3:])

print(result)
