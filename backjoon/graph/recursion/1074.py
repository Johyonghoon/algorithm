# 1074번 Z
# https://www.acmicpc.net/problem/1074

"""
# 재귀로 모든 좌표를 찍으면 시간초과...
# 가능한 범위의 경우에만 탐색
(0, 0)~(1, 1)  (2, 0)~(3, 1)
(0, 2)~(1, 3)  (2, 2)~(3, 3)
"""


def recur(node, ny, nx):
    global cnt, breaky
    if ny == r and nx == c:
        print(cnt)
        breaky = True
        return

    for dy, dx in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        # 값이 나오면 리턴
        if breaky:
            return

        ey = ny + dy * (2 ** node)
        ex = nx + dx * (2 ** node)

        if ey <= r < ey + (2 ** node) and ex <= c < ex + (2 ** node):
            recur(node-1, ey, ex)
        else:
            cnt += (2 ** node) ** 2


N, r, c = map(int, input().split())
# 그래프를 그리고 있느라 느린 거였다.
# graph = [[0 for _ in range(2**N)] for _ in range(2**N)]

cnt = 0
breaky = False
recur(N-1, 0, 0)
