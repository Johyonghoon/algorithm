# 1303번 전쟁 - 전투
# https://www.acmicpc.net/problem/1303

"""
아군(흰색 옷)과 적군(파란색 옷)의 위력을 구하는 문제
인접한 아군의 수의 제곱 수만큼 위력을 가진다.
아군을 0, 적군을 1로 저장하여 풀이
DFS를 통해 인접한 아군의 수를 구하여 위력 저장
"""


def dfs(ny, nx, team, cnt):
    visited[ny][nx] = 1
    cnt += 1

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < M and 0 <= ex < N:
            if visited[ey][ex]:
                continue
            if graph[ey][ex] == team:
                cnt = dfs(ey, ex, team, cnt)
    return cnt


# 팀 정보
N, M = map(int, input().split())
graph = []
for _ in range(M):
    # 아군 : 0, 적군 : 1
    arr = list(input().replace("W", "0").replace("B", "1"))
    graph.append(list(map(int, arr)))

# 각 좌표에서 DFS 탐색
visited = [[0 for _ in range(N)] for _ in range(M)]
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
our = 0
enemy = 0
for y in range(M):
    for x in range(N):
        if visited[y][x]:
            continue
        # 현재 좌표, 팀 정보, 인접한 같은 팀원 수 전달
        power = dfs(y, x, graph[y][x], 0) ** 2
        if graph[y][x]:
            enemy += power
        else:
            our += power
        # print(visited)
        # print(graph[y][x], power)

print(our, enemy)
