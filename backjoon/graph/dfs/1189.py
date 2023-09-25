# 1189번 컴백홈
# https://www.acmicpc.net/problem/1189


"""
# R, C가 각각 5밖에 되지 않으므로 완전탐색
"""


def dfs(ny, nx, cnt):
    global result
    if ny == 0 and nx == C-1:
        if cnt == K:
            result += 1
        return

    if cnt == K:
        return

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < R and 0 <= ex < C:
            # T 위치를 0으로 저장하여 이동하지 못하게 함
            if graph[ey][ex] and not visited[ey][ex]:
                visited[ey][ex] = 1
                dfs(ey, ex, cnt+1)
                visited[ey][ex] = 0


R, C, K = map(int, input().split())
graph = []
for _ in range(R):
    arr = list(map(int, list(input().replace(".", "1").replace("T", "0"))))
    graph.append(arr)

result = 0
# 출발 지점이 왼쪽 아래
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
visited = [[0 for _ in range(C)] for _ in range(R)]
visited[R-1][0] = 1
dfs(R-1, 0, 1)

print(result)
