# 3085번 사탕 게임
# https://www.acmicpc.net/problem/3085

"""
브루트 포스로 모든 좌표에서 사탕의 색이 다른 인접한 두 칸을 맞바꾸어 최대 길이를 구하기
"""


def maximum_candy():
    global maxi
    # x축 탐색
    for ey in range(N):
        candy = ""
        cnt = 0
        for ex in range(N):
            if candy == graph[ey][ex]:
                cnt += 1
            else:
                cnt = 1
                candy = graph[ey][ex]
            maxi = max(maxi, cnt)
    # y축 탐색
    for ex in range(N):
        candy = ""
        cnt = 0
        for ey in range(N):
            if candy == graph[ey][ex]:
                cnt += 1
            else:
                cnt = 1
                candy = graph[ey][ex]
            maxi = max(maxi, cnt)


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(input()))

# 인접한 색이 다른 사탕을 골라 교환한 후 최대 길이를 구해 본다.
maxi = 0

# y축 탐색
for y in range(N):
    for x in range(N):
        if y < N-1:
            # 사탕의 색이 다를 경우 서로 바꾼 후 최대 개수 구하기
            if graph[y][x] != graph[y+1][x]:
                graph[y][x], graph[y+1][x] = graph[y+1][x], graph[y][x]
                maximum_candy()
                graph[y][x], graph[y + 1][x] = graph[y + 1][x], graph[y][x]

# x축 탐색
for x in range(N):
    for y in range(N):
        if x < N-1:
            # 사탕의 색이 다를 경우 서로 바꾼 후 최대 개수 구하기
            if graph[y][x] != graph[y][x+1]:
                graph[y][x], graph[y][x+1] = graph[y][x+1], graph[y][x]
                maximum_candy()
                graph[y][x], graph[y][x + 1] = graph[y][x + 1], graph[y][x]

print(maxi)

