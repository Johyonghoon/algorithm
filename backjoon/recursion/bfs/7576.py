# 7576번 토마토
# https://www.acmicpc.net/problem/7576

"""
1. 익은 토마토에 인접한 익지 않은 토마토는 하루 뒤에 익게 된다.
2. 전체 토마토를 너비우선탐색으로 탐색한 뒤 가장 늦게 도달하는 위치의 거리 정보를 출력하면 최소 일수를 알 수 있다.
3. 익은 토마토는 여러 개가 존재할 수 있으므로, 익은 토마토를 기준으로 전체를 탐색하며 기록하고,
4. 만약 이미 익은 토마토에 대한 정보가 담겨 있다면, 최소 시간을 파악하여 저장한다.
5. 시간 초과
6. 이 문제는 익은 토마토를 미리 queue에 넣고 시작한다면 익은 토마토를 기준으로 최소 시간을 탐색할 수 있게 된다.
7. 따라서, 익은 토마토마다 bfs를 반복하지 않고 모든 익은 토마토를 큐에 넣고 시작한다면 해결할 수 있다.
"""

import sys
from collections import deque
from pprint import pprint
input = sys.stdin.readline

M, N = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 익은 토마토를 queue에 먼저 다 넣어준 후 시작
q = deque()
tomato = []
visited = [[0 for _ in range(M)] for _ in range(N)]
result = [[-1 for _ in range(M)] for _ in range(N)]

for y in range(N):
    for x in range(M):
        # -1인 경우 탐색하지 않는다.
        if graph[y][x] == -1:
            visited[y][x] = 1
            result[y][x] = 0
        # 1일 때만 탐색
        if graph[y][x] == 1:
            visited[y][x] = 1
            result[y][x] = 0
            q.append([y, x])

while q:
    ny, nx = q.popleft()

    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey, ex = ny + dy, nx + dx

        if 0 <= ey < N and 0 <= ex < M:
            if visited[ey][ex]:
                continue
            # 0일 때만 탐색
            if graph[ey][ex] == 0:
                visited[ey][ex] = 1
                result[ey][ex] = result[ny][nx] + 1
                q.append([ey, ex])

# pprint(result)
isPossible = True
maxi = 0
for i in result:
    for j in i:
        if j == -1:
            maxi = -1
            isPossible = False
            break
        if maxi < j:
            maxi = j
    if not isPossible:
        break

print(maxi)

"""
6 4
1 0 0 -1 0 0
0 0 -1 0 -1 0
0 0 0 -1 0 0
0 0 0 0 0 1
"""