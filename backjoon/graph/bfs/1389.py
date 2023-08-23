# 1389번 케빈 베이컨의 6단계 법칙
# https://www.acmicpc.net/problem/1389

import sys
from collections import deque
input = sys.stdin.readline

# N : 유저의 수(node) // M : 관계의 수(edge)
N, M = map(int, input().split())
# 간선 정보 입력
edges = [set() for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    edges[n1].add(n2)
    edges[n2].add(n1)

# 모든 사람들의 최단 경로를 탐색해야 한다.
result = [0 for _ in range(N+1)]
for idx in range(1, N+1):
    visited = [0 for _ in range(N+1)]
    dist = [0 for _ in range(N+1)]

    q = deque()
    q.append(idx)
    visited[idx] = 1

    # 특정 사람에 대해 모든 사람과의 관계의 단계를 기록
    while q:
        node = q.popleft()

        for nxt in edges[node]:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            dist[nxt] = dist[node] + 1
            q.append(nxt)
    # print(dist)
    result[idx] = sum(dist)

mini = 10 ** 8
ans = 0
for idx, num in enumerate(result):
    if idx == 0:
        continue
    if mini > num:
        mini = num
        ans = idx

print(ans)