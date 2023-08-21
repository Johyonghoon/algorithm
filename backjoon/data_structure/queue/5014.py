# 5014번 스타트링크
# https://www.acmicpc.net/problem/5014

import sys
from collections import deque
input = sys.stdin.readline

# F: 최고층 / S: 현재층 / G: 목적지 / U: 올라가는 층 / D: 내려가는 층
F, S, G, U, D = map(int, input().split())
visited = [0 for _ in range(F+1)]
dist = [-1 for _ in range(F+1)]

q = deque()
q.append(S)
visited[S] = 1
dist[S] = 0

while q:
    node = q.popleft()

    for nxt in [node + U, node - D]:
        if 1 <= nxt <= F:
            if visited[nxt]:
                continue
            visited[nxt] = 1
            dist[nxt] = dist[node] + 1
            q.append(nxt)

if dist[G] == -1:
    print("use the stairs")
else:
    print(dist[G])
