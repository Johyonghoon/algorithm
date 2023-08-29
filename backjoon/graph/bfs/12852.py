# 12852번 1로 만들기 2
# https://www.acmicpc.net/problem/12852

from collections import deque

N = int(input())
q = deque()
q.append(N)
visited = [0 for _ in range(N+1)]
route = [[] for _ in range(N+1)]
route[N] = [N]
visited[N] = 1

while q:
    node = q.popleft()
    if node == 1:
        break

    # 3으로 나누어 떨어질 때
    if node % 3 == 0:
        if not visited[node//3]:
            q.append(node//3)
            visited[node//3] = 1
            route[node//3] = route[node] + [node//3]

    # 2로 나누어 떨어질 때
    if node % 2 == 0:
        if not visited[node//2]:
            q.append(node//2)
            visited[node//2] = 1
            route[node//2] = route[node] + [node//2]

    # 1을 뺄 때
    if not visited[node-1]:
        q.append(node-1)
        visited[node-1] = 1
        route[node-1] = route[node] + [node-1]

# 자기 자신을 포함하지 않는 횟수를 가지기 때문에 -1
print(len(route[1])-1)
print(*route[1])
