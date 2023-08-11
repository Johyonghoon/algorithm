# 1388번 바닥 장식
# https://www.acmicpc.net/problem/1388

# 바닥 장식 정보 입력
N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(input()))

# 나무 판자의 개수 초기화
result = 0

# 가로 방향 탐색
for y in range(N):
    isRow = False
    for x in range(M):
        if graph[y][x] == "-":
            isRow = True
            if x+1 != M and graph[y][x+1] == "-":
                continue
            else:
                isRow = False
                result += 1
    else:
        if isRow:
            result += 1

# 세로 방향 탐색
for x in range(M):
    isColumn = False
    for y in range(N):
        if graph[y][x] == "|":
            isColumn = True
            if y+1 != N and graph[y+1][x] == "|":
                continue
            else:
                isColumn = False
                result += 1
    else:
        if isColumn:
            result += 1

print(result)