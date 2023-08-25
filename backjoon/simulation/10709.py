# 10709번 기상캐스터
# https://www.acmicpc.net/problem/10709

H, W = map(int, input().split())
graph = []
for _ in range(H):
    graph.append(list(input()))

result = [[-1 for _ in range(W)] for _ in range(H)]
for y in range(H):
    isCloud = False
    minute = 0
    for x in range(W):
        if graph[y][x] == "c":
            isCloud = True
            result[y][x] = 0
            minute = 0
            continue
        if isCloud:
            minute += 1
            result[y][x] = minute

[print(*i) for i in result]
