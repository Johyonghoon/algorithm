# 2665번 미로만들기
# https://www.acmicpc.net/problem/2665

"""
흰 방이 1, 검은 방이 0으로 저장되어 있지만,
검은 방을 방문할 때 1만큼 증가하는 방식으로 생각한다면 되지 않을까?
즉, 가중치 정보가 달라지므로 단순 BFS가 아닌 다익스트라 문제
"""
import heapq

n = int(input())
graph = []
for _ in range(n):
    arr = list(map(int, list(input())))
    for i in range(n):
        if arr[i]:
            arr[i] = 0
        else:
            arr[i] = 1
    graph.append(arr)

# 거리정보를 담을 2차원 배열 생성 / 시작지점 초기화
dist = [[int(1e9) for _ in range(n)] for _ in range(n)]
dist[0][0] = 0

# 단순 최단거리가 아닌 가능여부를 판단하며 이동해야 하므로 힙을 활용해야 하지 않을까
pq = []
heapq.heappush(pq, [0, 0, 0])

# 델타 탐색을 위한 배열
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]

# BFS
while pq:
    w, ny, nx = heapq.heappop(pq)

    if w > dist[ny][nx]:
        continue

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < n and 0 <= ex < n:
            if dist[ny][nx] + graph[ey][ex] < dist[ey][ex]:
                dist[ey][ex] = dist[ny][nx] + graph[ey][ex]
                heapq.heappush(pq, [dist[ey][ex], ey, ex])

print(dist[n-1][n-1])

