# 9663번 N-Queen
# https://www.acmicpc.net/problem/9663
# not solved

import sys

N = int(sys.stdin.readline())
graph = [[0 for _ in range(N)] for _ in range(N)]
coordinate = []
for y in range(N):
    for x in range(N):
        coordinate.append([x, y])

ls = []
limit = -1
result = 0

def recur():
    global result, ls, limit
    if len(ls) == N:
        result += 1
        return

    for i, cr in enumerate(coordinate):
        if limit > i:
            continue
        x, y = cr
        if graph[y][x] != 0:
            continue

        for j in range(N):
            graph[y][j] += 1
            graph[j][x] += 1
            if y + j <= N - 1:
                if x + j <= N - 1: graph[y + j][x + j] += 1
                if x - j >= 0: graph[y + j][x - j] += 1

            if y - j >= 0
                if x + j <= N - 1: graph[y - j][x + j] += 1
                if x - j >= 0: graph[y - j][x - j] += 1

        ls.append((x, y))
        recur()

        for j in range(N):
            graph[y][j] -= 1
            graph[j][x] -= 1
            if y + j <= N - 1:
                if x + j <= N - 1: graph[y + j][x + j] -= 1
                if x - j >= 0: graph[y + j][x - j] -= 1

            if y - j >= 0:
                if x + j <= N - 1: graph[y - j][x + j] -= 1
                if x - j >= 0: graph[y - j][x - j] -= 1

        limit = i + 1
        ls.pop()

recur()
print(result)


"""
import sys

N = int(sys.stdin.readline())
graph = [[0 for _ in range(N*3)] for _ in range(N*3)]
coordinate = []
for y in range(N):
    for x in range(N):
        coordinate.append([x, y])

ls = []
limit = -1
result = 0

def recur():
    global result, ls, limit
    if len(ls) == N:
        result += 1
        return

    for i, cr in enumerate(coordinate):
        x, y = cr
        x, y = x + N, y + N
        if (x, y) in ls:
            continue
        if limit > i:
            continue
        if graph[y][x] == 0:
            for j in range(N):
                graph[y][N+j] += 1
                graph[N+j][x] += 1
                graph[y+j][x+j] += 1
                graph[y+j][x-j] += 1
                graph[y-j][x+j] += 1
                graph[y-j][x-j] += 1

            ls.append((x, y))
            recur()

            for j in range(N):
                graph[y][N+j] -= 1
                graph[N+j][x] -= 1
                graph[y+j][x+j] -= 1
                graph[y+j][x-j] -= 1
                graph[y-j][x+j] -= 1
                graph[y-j][x-j] -= 1

            ls.pop()
            limit = i + 1

recur()
print(result)
"""



"""
        if graph[y][x] == 0:
            z = 1
            while True:
                if z == N:
                    graph[y][x] += 1
                    ls.append((x, y))
                    recur()
                    ls.pop()
                    limit_i = i + 1
                    graph[y][x] -= 1
                    break

                if y + z <= N - 1:
                    if graph[y + z][x] != 0: break
                    if x + z <= N - 1:
                        if graph[y + z][x + z] != 0: break
                    if x - z >= 0:
                        if graph[y + z][x - z] != 0: break

                if y - z >= 0:
                    if graph[y - z][x] != 0: break
                    if x + z <= N - 1:
                        if graph[y - z][x + z] != 0: break
                    if x - z >= 0:
                        if graph[y - z][x - z] != 0: break

                if x + z <= N - 1:
                    if graph[y][x + z] != 0: break
                if x - z >= 0:
                    if graph[y][x - z] != 0: break

                z += 1
"""