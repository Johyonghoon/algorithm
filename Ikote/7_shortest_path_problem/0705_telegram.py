import heapq
import sys

input = sys.stdin.readline

n, m, start = map(int, input().split())
INF = int(1e9)

graph = [[] for _ in range(n+1)]
distance = [INF for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)
cnt, max_distance = 0, 0

for d in distance:
    if d != int(1e9):
        cnt += 1
        max_distance = max(max_distance, d)

print(cnt-1, max_distance)
