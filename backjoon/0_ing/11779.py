# 11779번 최소비용 구하기 2
# https://www.acmicpc.net/problem/11779

import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
edges = [[] for _ in range(n+1)]
for _ in range(m):
    n1, n2, w = map(int, input().split())
    edges[n1].append([w, n2])
start, end = map(int, input().split())
# print(edges)

# 거리 정보와 현재 위치 정보 넣기
dist = [[10**9, []] for _ in range(n+1)]
dist[start] = [0, [start]]
result = 10**9

# print(dist)
pq = []
heapq.heappush(pq, [0, start])

while pq:
    w, node = heapq.heappop(pq)

    if w > result:
        continue

    for weight, nxt in edges[node]:
        if dist[node][0] + weight < dist[nxt][0]:
            dist[nxt] = [dist[node][0] + weight, dist[node][1] + [nxt]]
            heapq.heappush(pq, [dist[nxt][0], nxt])

print(dist[end][0])
print(len(dist[end][1]))
print(*dist[end][1])
