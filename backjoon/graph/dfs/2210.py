# 2210번 숫자판 점프
# https://www.acmicpc.net/problem/2210

"""
5 * 5 숫자판
임의의 위치에서 인접한 네 방향으로 다섯 번 이동하며 6자리 숫자를 만드는 경우의 수
dfs로 6회 탐색
"""


def recur(cnt, ny, nx, arr):
    if cnt == 6:
        number = int("".join(map(str, arr)))
        result.add(number)
        return

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < 5 and 0 <= ex < 5:
            recur(cnt+1, ey, ex, arr + [graph[ey][ex]])


graph = []
for _ in range(5):
    graph.append(list(map(int, input().split())))

delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
result = set()
for y in range(5):
    for x in range(5):
        recur(1, y, x, [graph[y][x]])

print(len(result))
