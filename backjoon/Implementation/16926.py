# 16926번 배열 돌리기 1
# https://www.acmicpc.net/problem/16926

# from pprint import pprint

"""
(4 + 4) * 2 - 4
(0, 0) (4-1, 0) (4-1, 4-1) (0, 4-1)
(1, 1) (4-1-1, 1)
delta = (1, 1), (-1, 1) (-1, -1) (1, -1)

1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8 
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
1 2 3 4 5 6 7 8
"""
import sys
input = sys.stdin.readline


def turn(c):
    ay, ax = c[0]
    by, bx = c[1]
    cy, cx = c[2]
    dy, dx = c[3]

    # 방문 처리
    for ny in range(ay, by+1):
        visited[ny][ax] = 1
        visited[ny][cx] = 1
    for nx in range(ax, dx+1):
        visited[ay][nx] = 1
        visited[by][nx] = 1

    for _ in range(R % (((cy-ay) + (cx-ax)) * 2)):

        tmp1 = graph[by][bx]
        for ny in range(by, ay, -1):
            graph[ny][ax] = graph[ny-1][ax]
        graph[ay][ax] = graph[ay][ax+1]

        tmp2 = graph[cy][cx]
        for nx in range(cx, bx+1, -1):
            graph[by][nx] = graph[by][nx-1]
        graph[by][bx+1] = tmp1

        tmp3 = graph[dy][dx]
        for ny in range(dy, cy-1):
            graph[ny][cx] = graph[ny+1][cx]
        graph[cy-1][cx] = tmp2

        for nx in range(ax+1, dx-1):
            graph[dy][nx] = graph[dy][nx+1]
        graph[dy][dx-1] = tmp3

        # pprint(graph)


N, M, R = map(int, input().split())
graph = []
for _ in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)

target = min(N, M)
coor = [[0, 0], [N-1, 0], [N-1, M-1], [0, M-1]]
delta = [(1, 1), (-1, 1), (-1, -1), (1, -1)]
visited = [[0 for _ in range(M)] for _ in range(N)]

while coor[0][0] < N // 2 or coor[0][1] < M // 2:
    turn(coor)
    for i, d in enumerate(delta):
        dy, dx = d
        coor[i][0] += dy
        coor[i][1] += dx
    if visited[coor[0][0]][coor[0][1]]:
        break

if N % 2 and N < M and R % 2:
    graph[coor[0][0]][coor[0][1]], graph[coor[0][0]+1][coor[0][1]] = graph[coor[0][0]+1][coor[0][1]], graph[coor[0][0]][coor[0][1]]
if M % 2 and M < N and R % 2:
    graph[coor[0][0]][coor[0][1]], graph[coor[0][0]][coor[0][1]+1] = graph[coor[0][0]][coor[0][1]+1], graph[coor[0][0]][coor[0][1]]

for g in graph:
    print(*g)
