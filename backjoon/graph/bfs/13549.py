# 13549번 숨바꼭질 3
# https://www.acmicpc.net/problem/13549
from collections import deque

N, K = map(int, input().split())

visited = [10**6 for _ in range(100_001)]

q = deque()
# 출발 위치와 sec 정보 저장
q.append([N, 0])
visited[N] = 0

while q:
    node, time = q.popleft()

    # 미리 중단시킨다면 2배 했을 때의 시간은 증가하지 않으므로 최소가 되지 않을 수 있다.
    # if node == K:
    #     break

    for idx in [-1, 1, node]:
        nxt = node + idx
        if 0 <= nxt <= 100_000:
            # 최소값이 되지 않는다면 필터링링
            if visited[nxt] < time+1:
                continue
            if idx == node:
                q.append([nxt, time])
                visited[nxt] = visited[node]
            else:
                q.append([nxt, time+1])
                visited[nxt] = visited[node] + 1

# print(visited)
print(visited[K])




