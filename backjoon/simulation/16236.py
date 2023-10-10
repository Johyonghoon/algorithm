# 16236번 아기 상어
# https://www.acmicpc.net/problem/16236

from pprint import pprint

"""
아기 상어의 초기 크기는 2, 1초에 상하좌우 인접한 한 칸씩 이동 (델타 탐색)
자신의 크기보다 큰 물고기가 있는 칸은 지날 수 없다.
자기 자신의 크기보다 작은 물고기를 먹을 수 있다.
자기 자신과 크기가 같은 경우 먹을 수는 없지만, 그 칸으로 지나갈 수는 있다.

이동을 결정하는 방법
- 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움을 요청
- 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러 간다.
  -> 물고기를 거리순으로 오름차순으로 정렬
- 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 간다. (BFS 탐색 필요)
  - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때 지나야 하는 칸의 개수의 최솟값
    즉, abs(shark_y - fish_y) + abs(shark_x - fish_y) 의 최소값
  - 거리가 가까운 물고기가 많다면, 가장 위의 물고기(y 값이 작은), 그러한 물고기가 많다면 가장 왼쪽의 물고기(x 값이 작은)를 먹는다.

아기 상어의 이동은 1초, 물고기를 먹는데 걸리는 시간은 없다고 가정
즉, 이동과 동시에 물고기를 먹는다. 물고기를 먹으면 그 칸은 빈 칸이 된다

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1 증가
즉, 아기 상어의 크기가 2일 때, 2마리를 먹어야 크기가 3으로 증가한다.

그래프 공간의 의미
- 0 : 빈칸
- 1, 2, 3, 4, 5, 6 : 칸에 있는 물고기의 크기
- 9 : 아기 상어의 위치(단 한 마리 존재)
"""
from collections import deque
import heapq

# 아기 상어, 물고기 크기와 좌표 정보를 저장
N = int(input())
graph = []
shark = []
size = 2    # 아기 상어 사이즈의 시작은 2
for y in range(N):
    arr = list(map(int, input().split()))
    for x, num in enumerate(arr):
        if num:
            if num == 9:
                shark = [y, x]
            # else:
            #     fish[num].append([y, x])
    graph.append(arr)

sec = 0
cnt = 0
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
# 가장 작은 물고기 사이즈보다 크면 종료
while True:

    # 아기 상어 좌표
    sy, sx = shark

    # 현재 상어 위치에서 각 좌표에 도달하는 거리 정보를 탐색, BFS
    # 잡아먹을 수 있는 물고기 위치에 도달하지 못할 수도 있으므로,,,
    dist = [[-1 for _ in range(N)] for _ in range(N)]
    q = deque()
    q.append(shark)
    dist[sy][sx] = 0

    eatable = []
    while q:
        ny, nx = q.popleft()
        for dy, dx in delta:
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey < N and 0 <= ex < N:
                # 상어보다 크다면 지나갈 수 없다.
                if graph[ey][ex] > size:
                    continue
                if dist[ey][ex] != -1:
                    continue
                dist[ey][ex] = dist[ny][nx] + 1

                # 만약 해당 좌표에 상어보다 작은 물고기가 있다면
                if 0 < graph[ey][ex] < size:
                    # 물고기까지의 거리, y 좌표, x 좌표 순서대로 저장
                    distance = dist[ey][ex]
                    heapq.heappush(eatable, [distance, ey, ex])
                # 만약 잡아먹을 수 있는 물고기 좌표를 지나가면, 지나감과 동시에 잡아먹게 되므로,
                # 먹지 않고 지나갈 수는 없게 된다. 따라서 그 길을 통해서 다른 작은 물고기에게 접근할 수는 없는 것이다.
                else:
                    # print(graph[ey][ex], size)
                    q.append([ey, ex])

    # pprint(dist)
    # pprint(graph)
    # print("size", size, cnt)
    # print("eatable", eatable)

    if eatable:
        fish_size, fy, fx = heapq.heappop(eatable)
        sec += dist[fy][fx]
        # print("sec", sec)
        graph[sy][sx] = 0
        graph[fy][fx] = 9
        shark = [fy, fx]

        cnt += 1
        if cnt == size:
            size += 1
            cnt = 0

    else:
        break

print(sec)

"""
5
0 0 0 0 0
1 0 0 0 2
0 0 3 3 0
3 3 0 0 9
1 3 0 0 0

7
3 5 0 6 4 5 5
1 6 3 3 0 2 2
6 2 1 3 1 5 1
9 2 2 3 4 2 3
2 1 6 2 0 0 4
4 5 0 6 1 1 0
5 4 3 2 1 4 0

>> 67
"""
