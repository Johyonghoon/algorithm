# 14938번 서강그라운드
# https://www.acmicpc.net/problem/14938

"""
# 다익스트라
거리 정보가 업데이트되었다면 다시 탐색하지 않는 방식으로 하니 틀렸다.
당연한 것... 먼저 탐색한 곳이 더 짧다는 보장은 없음...
그것이 다익스트라니까...
"""
import heapq


def dijkstra(i):
    pq = []
    pq.append([0, i])
    dist = [int(1e9) for _ in range(N+1)]
    dist[i] = 0
    while pq:
        weight, node = heapq.heappop(pq)
        for w, nxt in edges[node]:
            if dist[nxt] > dist[node] + w:
                dist[nxt] = dist[node] + w
                heapq.heappush(pq, [dist[nxt], nxt])
    cnt = 0
    for j, distance in enumerate(dist):
        if distance <= M:
            cnt += items[j]
    # print(i, dist, cnt)
    return cnt


N, M, R = map(int, input().split())
items = [0] + list(map(int, input().split()))
# print(items)
edges = [[] for _ in range(N+1)]
for _ in range(R):
    n1, n2, d = map(int, input().split())
    edges[n1].append([d, n2])
    edges[n2].append([d, n1])

result = 0
for idx in range(1, N+1):
    result = max(result, dijkstra(idx))

print(result)
