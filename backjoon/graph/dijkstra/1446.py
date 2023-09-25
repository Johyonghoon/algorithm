# 1446번 지름길
# https://www.acmicpc.net/problem/1446

"""
# 다익스트라
1. D 킬로미터의 고속도로를 지난다.
2. 역주행이 불가능하다 : 일방통행
3. 고속도로는 바로 다음 킬로미터로 이동 가능하다
  ex) 0km -> 1km : weight 1
"""
import heapq

N, D = map(int, input().split())
# 가중치 정보 입력
edges = [[] for _ in range(D+1)]
for _ in range(N):
    n1, n2, w = map(int, input().split())
    # 역주행이 불가능하므로 도착 위치를 넘어선다면 넘어가자
    if n2 > D:
        continue
    edges[n1].append([w, n2])

# 고속도로는 주어진 지름길 정보 외에도 다음 거리의 위치까지 이동할 수 있다.
for idx in range(D):
    edges[idx].append([1, idx+1])

# print(edges)

# 거리 정보를 업데이트할 배열 생성
dist = [int(1e9) for _ in range(D+1)]
dist[0] = 0

# 힙을 활용하여 최단거리를 찾는 방식을 선택
pq = []
# 가중치와 시작 노드를 삽입
heapq.heappush(pq, [0, 0])

# BFS 탐색
while pq:
    _w, node = heapq.heappop(pq)
    for weight, nxt in edges[node]:
        if dist[node] + weight < dist[nxt]:
            dist[nxt] = dist[node] + weight
            heapq.heappush(pq, [dist[nxt], nxt])

print(dist[D])



