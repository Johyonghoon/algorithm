# 5972번 택배 배송
# https://www.acmicpc.net/problem/5972

"""
# 다익스트라 : 가중치가 일정하지 않으므로 BFS 가 아닌 다익스트라
양방향 이동이 가능하다.
"""

import sys
import heapq
input = sys.stdin.readline


# N : 노드 / M : 간선
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2, w = map(int, input().split())
    edges[n1].append([w, n2])
    edges[n2].append([w, n1])

# 거리정보를 업데이트할 배열 생성 / 출발지 정보 초기화
dist = [int(1e9) for _ in range(N+1)]
dist[1] = 0

# 최단경로를 탐색하기 위해 힙 활용 / 시작지점 push
pq = []
heapq.heappush(pq, [0, 1])

# BFS
while pq:
    w, node = heapq.heappop(pq)

    if w > dist[node]:
        continue

    for weight, nxt in edges[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(pq, [dist[nxt], nxt])

# 헛간 N에 도달하는 거리 출력
print(dist[N])

