# 2660번 회장뽑기
# https://www.acmicpc.net/problem/2660

"""
# BFS
친구들 거리가 가까운 사람이 회장 후보
"""
from collections import deque


def bfs(person, queue):
    while queue:
        node = queue.popleft()
        for nxt in edges[node]:
            if dist[person][nxt] != -1:
                continue
            dist[person][nxt] = dist[person][node] + 1
            q.append(nxt)
            # print(dist[idx])


N = int(input())
edges = [[] for _ in range(N+1)]
dist = [[-1 for _ in range(N+1)] for _ in range(N+1)]
while True:
    n1, n2 = map(int, input().split())
    if n1 == n2 == -1:
        break
    edges[n1].append(n2)
    edges[n2].append(n1)
# print(edges)

scores = [0 for _ in range(N+1)]
for idx in range(1, N+1):
    dist[idx][idx] = 0
    q = deque()
    q.append(idx)
    bfs(idx, q)
    scores[idx] = max(dist[idx])

# print(scores)
target = min(scores[1:])
candidates = []
for idx, score in enumerate(scores):
    if score == target:
        candidates.append(idx)

print(target, len(candidates))
print(*candidates)
