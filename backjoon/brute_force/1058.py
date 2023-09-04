# 1058번 친구
# https://www.acmicpc.net/problem/1058

N = int(input())
edges = [[] for _ in range(N)]
for i in range(N):
    arr = list(map(int, list(input().replace("N", "0").replace("Y", "1"))))
    for j in range(N):
        if arr[j]:
            edges[i].append(j)
            edges[j].append(i)

result = 0
for idx in range(N):
    visited = [0 for _ in range(N)]
    for edge in edges[idx]:
        visited[edge] = 1
        for edge2 in edges[edge]:
            if edge2 == idx:
                continue
            visited[edge2] = 1
    result = max(result, visited.count(1))

print(result)