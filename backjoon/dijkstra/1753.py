# 1753번 최단경로
# https://www.acmicpc.net/problem/1753
import heapq
import sys
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
edges = [[] for _ in range(V+1)]
# 거리 정보를 저장할 배열 생성 / 시작 노드 초기화
dist = [1_000_000_000 for _ in range(V+1)]
dist[K] = 0

for _ in range(E):
    n1, n2, w = map(int, input().split())
    if n1 == n2:
        continue
    edges[n1].append([w, n2])

pq = []
heapq.heappush(pq, [0, K])

while pq:
    w, node = heapq.heappop(pq)

    if w > dist[node]:
        continue

    for weight, nxt in edges[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(pq, [dist[nxt], nxt])

for idx in range(1, V+1):
    if dist[idx] == 1_000_000_000:
        print("INF")
    else:
        print(dist[idx])

"""
# 무한 회전 테케 
5 6
1
1 2 2
2 3 1
3 1 2
1 4 5
5 1 2
5 3 2

# 노드 1개 간선 1개 자기 자신에게 들어가는 것도 계산에 반영된다면 최소값이 되지 않을 것
1 1
1
1 1 1

# 노드 3개 간선 1개
3 1
1
1 3 1

# 노드 2개 간선 2개 동일한 방향의 노드가 두 개 있을 때?
2 2
1
1 2 3
1 2 4

# 출발 노드에 연결된 것이 없을 떄?
2 2
1
2 1 3
2 1 1

# 웨이트가 작은 순서대로 입력되지 않았을 떄?
5 5
1
1 3 3
1 2 1
2 3 1
1 4 5
3 4 1

"""