# 17484번 진우의 달 여행 (small)
# https://www.acmicpc.net/problem/17484

"""
문제의 함정. 우주선은 전에 움직인 방향으로 움직일 수 없다.
"""


def recur(ny, nx, total, prv):
    global result
    # print(ny, nx, total)
    if ny == N:
        result = min(result, total)
        return

    for d in delta:
        if d == prv:
            continue
        ex = nx + d
        if 0 <= ex < M:
            recur(ny+1, ex, total+graph[ny][ex], d)


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

delta = [-1, 0, 1]
result = 10**8
for x in range(M):
    recur(1, x, graph[0][x], -2)

print(result)

