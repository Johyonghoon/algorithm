# 7569번 토마토
# https://www.acmicpc.net/problem/7569

import sys
from collections import deque

input = sys.stdin.readline

M, N, H = map(int, input().split())
# 3차원 배열 생성
cube = []
for _ in range(H):
    # 2차원 배열 생성
    graph = []
    for _ in range(N):
        graph.append(list(map(int, input().split())))
    cube.append(graph)

# 토마토의 이동 정보 : 위 아래 왼쪽 오른쪽 앞 뒤
rear = [[1, 0, 0], [-1, 0, 0], [0, 0, -1], [0, 0, 1], [0, 1, 0], [0, -1, 0]]
# 익는데에 걸리는 시간을 담을 배열 생성
dist = [[[1_000_001 for _ in range(M)] for _ in range(N)] for _ in range(H)]
visited = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
# 1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토가 들어 있지 않은 칸
q = deque()
for h in range(H):
    for y in range(N):
        for x in range(M):
            # queue에 삽입되는 노드들은 모두 익은 토마토
            if cube[h][y][x] == 1:
                q.append([h, y, x])
                visited[h][y][x] = 1
                dist[h][y][x] = 0
            # 토마토가 없는 곳
            if cube[h][y][x] == -1:
                visited[h][y][x] = 1
                dist[h][y][x] = -1

# BFS 탐색
while q:
    nh, ny, nx = q.popleft()
    # 델타 탐색
    for dh, dy, dx in rear:
        eh, ey, ex = nh + dh, ny + dy, nx + dx
        # 가능한 좌표 확인
        if 0 <= eh < H and 0 <= ey < N and 0 <= ex < M:
            # 이미 방문했다면 패스
            if visited[eh][ey][ex]:
                continue
            # 익지 않은 토마토라면 거리 정보는 현재 노드를 기준으로 +1
            if cube[eh][ey][ex] == 0:
                q.append([eh, ey, ex])
                dist[eh][ey][ex] = min(dist[eh][ey][ex], dist[nh][ny][nx] + 1)
                visited[eh][ey][ex] = 1

# print(cube)
# print(dist)
# 모든 토마토에 방문했는지 확인하고 거리 확인
maxi = 0
for h in range(H):
    for y in range(N):
        for x in range(M):
            # BFS로 최단 시간을 구했는데 이중에 가장 큰 값을 저장
            maxi = max(maxi, dist[h][y][x])

if maxi == 1_000_001:
    print(-1)
else:
    print(maxi)

"""
4 3 3
1 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0
0 0 0 0 
0 0 0 0
0 0 0 0 
0 0 0 0
0 0 0 0

4 3 3
1 0 0 0
0 0 0 0
0 0 0 -1
0 0 0 0
0 0 0 -1 
0 0 -1 0
0 0 0 0 
0 0 0 0
0 0 0 -1

2 2 1
1 -1
-1 0

2 2 2
1 -1
-1 0
0 0
0 0

2 2 3
1 -1
-1 0
0 -1
-1 0
0 0
-1 0
"""