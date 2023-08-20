# 2178번 미로 탐색
# https://www.acmicpc.net/problem/2178

import sys
from collections import deque
from pprint import pprint

input = sys.stdin.readline

N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input().strip()))))
visited = [[0 for _ in range(M)] for _ in range(N)]

q = deque()
# 시작점의 좌표, 문제에서는 (1, 1)로 주어지지만,
# 입력을 받은 좌표들의 인덱스 정보는 0, 0 부터 시작하므로 이렇게 둔다.
q.append([0, 0])
visited[0][0] = 1

while q:
    ny, nx = q.popleft()

    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey, ex = ny + dy, nx + dx

        if 0 <= ey < N and 0 <= ex < M:
            if graph[ey][ex]:
                if visited[ey][ex]:
                    continue
                visited[ey][ex] = visited[ny][nx] + 1
                q.append([ey, ex])

# pprint(visited)
print(visited[N-1][M-1])
