# 2563번 색종이
# https://www.acmicpc.net/problem/2563

N = int(input())
coordinate = []
max_x = 0
max_y = 0
for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append([x, y])
    max_x = max(max_x, x+10)
    max_y = max(max_y, y+10)

graph = [[False for _ in range(max_x+1)] for _ in range(max_y+1)]

for x, y in coordinate:
    for ey in range(y, y+10):
        for ex in range(x, x+10):
            graph[ey][ex] = True

result = 0
for ls in graph:
    result += ls.count(True)

print(result)

