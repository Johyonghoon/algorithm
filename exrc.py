import numpy as np

N = int(input())
graph = [[0 for _ in range(N)] for _ in range(N)]

print(graph)
for i in graph:
    print(i.count(0))

