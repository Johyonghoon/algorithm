# 14620번 꽃길
# https://www.acmicpc.net/problem/14620

"""
3개의 꽃을 심을 때 가장 적은 비용을 들여 심을 수 있는 경우의 비용
주의할 점
1. 꽃이 핀 후 서로 다른 꽃잎이 닿게 될 경우 두 꽃 모두 죽는다.
2. 꽃 잎이 화단 밖으로 나가게 될 경우에도 죽어버린다.
  -> 화단 범위에서는 꽃을 심을 수 없다.
"""


def flower(ny, nx, isTrue):
    if isTrue:
        d = 1
    else:
        d = -1
    for dy, dx in delta:
        ey, ex = ny + dy, nx + dx
        if 0 <= ey < N and 0 <= ex < N:
            visited[ey][ex] += d


def recur(cnt, arr):
    global result
    if cnt == 3:
        total = 0
        for fy, fx in arr:
            total += graph[fy][fx] + graph[fy-1][fx] + graph[fy+1][fx] + \
                        graph[fy][fx-1] + graph[fy][fx+1]
        result = min(result, total)
        return

    # 화단의 좌표는 0~N-1이므로 N-1을 포함하지 않아야 한다.
    for y in range(1, N-1):
        for x in range(1, N-1):
            if visited[y][x]:
                continue
            flower(y, x, True)
            arr.append([y, x])
            recur(cnt+1, arr)
            arr.pop()
            flower(y, x, False)


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

visited = [[0 for _ in range(N)] for _ in range(N)]
delta = [[-2, 0], [-1, -1], [-1, 0], [-1, 1],
         [0, -2], [0, -1], [0, 0], [0, 1], [0, 2],
         [1, -1], [1, 0], [1, 1], [2, 0]]
result = 10**9
recur(0, [])

print(result)
