# 15683번 감시
# https://www.acmicpc.net/problem/15683

import sys
input = sys.stdin.readline


def search_up(ny, nx):
    cctv_range = []
    for ey in range(ny, -1, -1):
        if graph[ey][nx] == 6:
            break
        cctv_range.append((ey, nx))
    return cctv_range


def search_down(ny, nx):
    cctv_range = []
    for ey in range(ny, N):
        if graph[ey][nx] == 6:
            break
        cctv_range.append((ey, nx))
    return cctv_range


def search_left(ny, nx):
    cctv_range = []
    for ex in range(nx, -1, -1):
        if graph[ny][ex] == 6:
            break
        cctv_range.append((ny, ex))
    return cctv_range


def search_right(ny, nx):
    cctv_range = []
    for ex in range(nx, M):
        if graph[ny][ex] == 6:
            break
        cctv_range.append((ny, ex))
    return cctv_range


def find_range(ny, nx):
    cctv_num = graph[ny][nx]
    cctv_range = []
    if cctv_num == 1:
        cctv_range.append(search_up(ny, nx))
        cctv_range.append(search_down(ny, nx))
        cctv_range.append(search_left(ny, nx))
        cctv_range.append(search_right(ny, nx))
    elif cctv_num == 2:
        cctv_range.append(search_up(ny, nx)+search_down(ny, nx))
        cctv_range.append(search_left(ny, nx)+search_right(ny, nx))
    elif cctv_num == 3:
        cctv_range.append(search_up(ny, nx)+search_left(ny, nx))
        cctv_range.append(search_up(ny, nx)+search_right(ny, nx))
        cctv_range.append(search_down(ny, nx)+search_left(ny, nx))
        cctv_range.append(search_down(ny, nx)+search_right(ny, nx))
    elif cctv_num == 4:
        cctv_range.append(search_up(ny, nx)+search_down(ny, nx)+search_left(ny, nx))
        cctv_range.append(search_down(ny, nx)+search_left(ny, nx)+search_right(ny, nx))
        cctv_range.append(search_left(ny, nx)+search_right(ny, nx)+search_up(ny, nx))
        cctv_range.append(search_right(ny, nx)+search_up(ny, nx)+search_down(ny, nx))
    elif cctv_num == 5:
        cctv_range.append(search_up(ny, nx)+search_down(ny, nx)+search_left(ny, nx)+search_right(ny, nx))
    return cctv_range


def dfs(idx, cctv_ranges):
    global result
    if idx == L:
        new_graph = [[0 for _ in range(M)] for _ in range(N)]
        for ny, nx in cctv_ranges:
            new_graph[ny][nx] = 1
        for ny, nx in block:
            new_graph[ny][nx] = 1

        cnt = 0
        for ey in range(N):
            for ex in range(M):
                if new_graph[ey][ex] == 0:
                    cnt += 1
        # print(new_graph, cnt)
        result = min(result, cnt)
        return

    for cctv_range in cctv[idx]:
        dfs(idx+1, cctv_ranges+cctv_range)


N, M = map(int, input().split())
graph = []
cctv = []
block = []
for y in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)

for y in range(N):
    for x, num in enumerate(graph[y]):
        if num:
            if num == 6:
                block.append((y, x))
            else:
                cctv.append(find_range(y, x))
# print("cctv", cctv)

L = len(cctv)
result = int(1e9)
dfs(0, [])
print(result)

"""
# input
6 6
1 0 0 0 0 0
0 2 0 0 0 0
0 0 3 0 0 0
0 0 0 4 0 0
0 0 0 0 5 0
0 0 0 0 0 6
# output
4

"""
