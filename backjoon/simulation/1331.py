# 1331번 나이트 투어
# https://www.acmicpc.net/problem/1331

graph = [[0 for _ in range(6)] for _ in range(6)]

ny, nx = 0, 0
sy, sx = 0, 0
isTrue = True
mv = [[2, 1], [2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2], [-2, 1], [-2, -1]]
for idx in range(36):
    arr = list(input())
    x = ord(arr[0]) - ord("A")
    y = int(arr[1]) - 1
    if idx == 0:
        graph[y][x] = 1
        ny, nx = y, x
        sy, sx = y, x
    elif idx == 35:
        graph[y][x] = 1
        if [y-sy, x-sx] not in mv:
            # print(idx, y, sy, x, sx)
            isTrue = False
    else:
        if [ny-y, nx-x] in mv:
            graph[y][x] = 1
        else:
            # print(idx, y, ny, x, nx)
            isTrue = False

    ny, nx = y, x

for y in range(6):
    for x in range(6):
        if not graph[y][x]:
            isTrue = False
            break

if isTrue:
    print("Valid")
else:
    print("Invalid")
