# 1916번 최소비용 구하기
# https://www.acmicpc.net/problem/1916

"""
N개의 도시와 M개의 간선
이동 비용을 최소화 : 다익스트라
A -> B 최소비용 구하기
버스는 단방향 이동 ?
"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
# 간선 정보 입력
edges = [[] for _ in range(N+1)]
dist = [int(1e9) for _ in range(N+1)]
for _ in range(M):
    n1, n2, w = map(int, input().split())
    edges[n1].append([w, n2])

# 출발 도착 도시 정보 // 출발지의 거리정보 초기화
A, B = map(int, input().split())
dist[A] = 0

# 힙을 통해 최소거리 구하기 // 시작 노드는 A이고 이때의 가중치는 0
pq = []
heapq.heappush(pq, [0, A])

# BFS
while pq:
    # print(pq)
    # print(dist)
    w, node = heapq.heappop(pq)

    # queue 처럼 모든 간선을 탐색한다.
    # 현재 노드로 오는 최소거리 정보가 여러 번 입력되었다면
    # 가장 최단거리의 정보를 먼저 탐색하고, 나중에 더 긴 거리의 정보를 탐색하기 때문에
    # 나중에 더 긴 거리를 다시 탐색하지 않기 위해 필터링해주는 과정이다.
    if w > dist[node]:
        continue

    for weight, nxt in edges[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(pq, [dist[nxt], nxt])

print(dist[B])
