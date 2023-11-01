# 1890번 점프
# https://www.acmicpc.net/problem/1890

"""
가장 왼쪽 위 칸에서 가장 오른쪽 아래 칸으로 규칙에 맞게 점프
각 칸에 적혀있는 수만큼 점프해서 이동해야 한다.
다시 되돌아갈 수 없고, 왼쪽 또는 오른쪽으로만 이동하므로
출발지에서 각 좌표에 도달하는 개수를 저장하며 전체 탐색
"""


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1
delta = [[1, 0], [0, 1]]

for y in range(N):
    for x in range(N):
        if y == N-1 and x == N-1:
            break
        for dy, dx in delta:
            ey = y + dy * graph[y][x]
            ex = x + dx * graph[y][x]
            if ey < N and ex < N:
                dp[ey][ex] += dp[y][x]

print(dp[N-1][N-1])
