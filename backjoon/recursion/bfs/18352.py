# 18352번 특정 거리의 도시 찾기
# https://www.acmicpc.net/problem/18352

import sys
from collections import deque
input = sys.stdin.readline

# N : 도시의 개수 // M : 도로의 개수 // K : 거리 정보 // X : 출발 도시의 번호
N, M, K, X = map(int, input().split())
# 단방향 도로 정보
edges = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    edges[n1].append(n2)

# 방문 정보 / 시작점으로부터의 거리 정보
visited = [0 for _ in range(N+1)]
dist = [0 for _ in range(N+1)]

# bfs 탐색으로 최단거리 파악
q = deque()
q.append(X)
visited[X] = 1

while q:
    node = q.popleft()

    # 거리 정보 입력
    for nxt in edges[node]:
        if visited[nxt]:
            continue
        visited[nxt] = 1
        dist[nxt] = dist[node] + 1
        q.append(nxt)

result = []
for idx, distance in enumerate(dist):
    if distance == K:
        result.append(idx)

# 없을 경우 -1 출력
if result:
    [print(i) for i in result]
else:
    print(-1)

