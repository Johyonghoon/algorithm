# 30679번 별 가두기
# https://www.acmicpc.net/problem/30679

"""
문제 조건 : 첫 번째 열의 원하는 칸에 별을 올린다...
각 좌표를 탐색하며 이미 방문한 곳에 도달했을 때 같은 방향으로 다시 방문하는지 여부를 확인
별은 처음에 오른쪽을 바라보며, 별이 놓인 칸에 적힌 수만큼 이동하고, 시계방향으로 90도 회전
"""

import sys
input = sys.stdin.readline


def is_true(ny, nx):
    d = 0   # 초기 방향
    while True:
        # 방문한 좌표에 가야할 방향으로 이미 탐색했다면 loop가 발생한 것으로 별을 성공적으로 가둔 것
        if d in visited[ny][nx]:
            # print("success")
            return True
        # print(ny, nx, d)
        ey = ny + direction[d][0] * graph[ny][nx]
        ex = nx + direction[d][1] * graph[ny][nx]
        if 0 <= ey < N and 0 <= ex < M:
            visited[ny][nx].add(d)  # 방문한 방향 추가
            ny, nx = ey, ex
            d = (d+1) % 4
        else:   # 별이 격자를 벗어난다면 실패한 것
            # print("fail")
            return False


N, M = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))


direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
result = 0
# set으로 해서 순서가 틀릴 때가 있나?
rows = []
# 첫 번째 열의 원하는 칸에서 시작
for y in range(N):
    visited = [[set() for _ in range(M)] for _ in range(N)]
    if is_true(y, 0):
        result += 1
        rows.append(y+1)

print(result)
# 빈 배열을 출력하게 되어서 틀린건가?
if result:
    print(*rows)
