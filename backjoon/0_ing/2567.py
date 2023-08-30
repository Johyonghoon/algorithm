# 2567번 색종이 2
# https://www.acmicpc.net/problem/2567


graph = [[0 for _ in range(101)] for _ in range(101)]
N = int(input())
for _ in range(N):
    px, py = map(int, input().split())

    # x축의 직사각형 바깥을 표시
    for y in [py, py+10]:
        for x in range(px, px+11):
            if graph[y][x] != -1:
                graph[y][x] = 1
