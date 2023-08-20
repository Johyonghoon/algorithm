# 1697번 숨바꼭질
# https://www.acmicpc.net/problem/1697

import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0 for _ in range(100_001)]

q = deque()
q.append(N)
visited[N] = 1

while q:
    node = q.popleft()

    # 너비우선탐색이기 때문에 최초로 도달했다면 중단시켜도 되지 않을까? 싶긴 한데 일단 완전탐색
    # if node == K:
    #     break

    for nxt in [node-1, node+1, node*2]:
        if 0 <= nxt <= 100_000:
            if visited[nxt]:
                continue

            visited[nxt] = visited[node] + 1
            q.append(nxt)

print(visited[K]-1)  # 시작 노드를 1로 두고 시작했기 때문
