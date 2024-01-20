# 9207번 페그 솔리테어
# https://www.acmicpc.net/problem/9207

"""
핀은 수평, 수직 방향으로 인접한 핀을 뛰어넘어서 그 핀의 다음 칸으로 이동하는 것만 허용
인접한 핀의 다음 칸은 비어있어야 하고 그 인접한 핀은 제거

핀을 적절히 움직여서 게임판에 남아있는 핀의 개수를 최소화
또 그렇게 남기기 위해 필요한 최소 이동 횟수를 구하기

"""

import sys
from collections import deque
input = sys.stdin.readline


def graph_to_string(g):
    a = []
    for i in g:
        a.append(" ".join(i))
    string = " ".join(a)
    return string


def string_to_graph(s):
    g = []
    a = list(s.split())
    for i in range(5):
        g.append([i for i in a[i*9:(i+1)*9]])
    return g


def find_pins(g):
    p = []
    for y in range(5):
        for x in range(9):
            if g[y][x] == '1':
                p.append((y, x))
    return p


def bfs():
    global min_cnt, min_move
    q = deque()

    for y, x in pins:
        q.append((y, x, len(pins), 0, graph_to_string(graph)))
    while q:
        ny, nx, cnt, move, string = q.popleft()

        for dy, dx in delta:
            ls = string_to_graph(string)
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey < 5 and 0 <= ex < 9:
                # 델타 방향에 핀이 있을 경우
                if ls[ey][ex] == "1":
                    my = ey + dy
                    mx = ex + dx
                    if 0 <= my < 5 and 0 <= mx < 9:
                        # 핀 너머가 빈 공간일 때
                        if ls[my][mx] == "0":
                            ls[ny][nx] = "0"
                            ls[ey][ex] = "0"
                            ls[my][mx] = "1"
                            if min_cnt > cnt-1:
                                min_cnt = cnt-1
                                min_move = [move+1]
                                if cnt-1 == 1:
                                    continue
                                for py, px in find_pins(ls):
                                    q.append((py, px, cnt-1, move+1, graph_to_string(ls)))
                            elif min_cnt == cnt-1:
                                min_move.append(move+1)
                                if cnt-1 == 1:
                                    continue
                                for py, px in find_pins(ls):
                                    q.append((py, px, cnt-1, move+1, graph_to_string(ls)))


delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]
T = int(input())
for _ in range(T):
    graph = []
    pins = []
    for y in range(5):
        arr = list(input().strip().replace("#", "9").replace(".", "0").replace("o", "1"))
        for x, num in enumerate(arr):
            if num == '1':
                pins.append((y, x))
        graph.append(arr)

    min_cnt = len(pins)
    min_move = [0]

    bfs()
    print(min_cnt, min(min_move))
    input()
