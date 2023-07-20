import numpy as np

n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

for a in range(n+1):
    for b in range(n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for a in range(1, n+1):
    for b in range(1, n+1):
        for c in range(1, n+1):
            graph[b][c] = min(graph[b][c], graph[b][a] + graph[a][c])

x, k = map(int, input().split())
distance = graph[1][k] + graph[k][x]
if distance >= INF:
    print(-1)
else:
    print(distance)

