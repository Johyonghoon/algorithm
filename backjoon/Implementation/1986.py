# 1986번 체스
# https://www.acmicpc.net/problem/1986


def queen(ny, nx):
    for dy, dx in delta_queen:
        ey = ny + dy
        ex = nx + dx
        while 0 <= ey < n and 0 <= ex < m:
            if graph[ey][ex] == 0 or graph[ey][ex] == -1:
                graph[ey][ex] = -1
                ey += dy
                ex += dx
            else:
                break


def knight(ny, nx):
    for dy, dx in delta_knight:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < n and 0 <= ex < m:
            if graph[ey][ex] == 0 or graph[ey][ex] == -1:
                graph[ey][ex] = -1


n, m = map(int, input().split())
graph = [[0 for _ in range(m)] for _ in range(n)]

delta_queen = [[1, 0], [0, 1], [-1, 0], [0, -1],
               [1, 1], [1, -1], [-1, 1], [-1, -1]]
queen_arr = list(map(int, input().split()))
for i in range(queen_arr[0]):
    graph[queen_arr[2*i+1]-1][queen_arr[2*i+2]-1] = 1

delta_knight = [[-2, -1], [-2, 1], [-1, -2], [-1, 2],
                [1, -2], [1, 2], [2, -1], [2, 1]]
knight_arr = list(map(int, input().split()))
for i in range(knight_arr[0]):
    graph[knight_arr[2*i+1]-1][knight_arr[2*i+2]-1] = 2

pawn_arr = list(map(int, input().split()))
for i in range(pawn_arr[0]):
    graph[pawn_arr[2*i+1]-1][pawn_arr[2*i+2]-1] = 3

for y in range(n):
    for x in range(m):
        if graph[y][x] == 1:
            queen(y, x)
        elif graph[y][x] == 2:
            knight(y, x)

result = 0
for y in range(n):
    for x in range(m):
        if graph[y][x] == 0:
            result += 1

print(result)
