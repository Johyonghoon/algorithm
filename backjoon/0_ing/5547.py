# 5547번 일루미네이션
# https://www.acmicpc.net/problem/5547

"""
지도의 가장 왼쪽 위의 좌표는 1,1
x, y 오른쪽에 있는 정육각형의 좌표는 (x+1, y)
y가 홀수일 때, 아래쪽에 있는 정육각형의 좌표는 (x, y+1)
y가 짝수일 때, 오른쪽 아래에 있는 정육각형의 좌표는 (x, y+1)

(0, 0)부터 출발한다고 가정하면
y가 짝수일 때, 아래쪽에 있는 정육각형의 좌표는 (x, y+1)
y가 홀수일 때, 오른쪽 아래에 있는 정육각형의 좌표는 (x, y+1)

1의 개수를 카운트하고 접점을 뺄까
접점은 x축이 증가할 때 두 좌표가 같다면 빼주기
근데 안쪽으로 접점이 없는 경우에는 조명을 설치하지 않는데 어떻게 판단하지
"""

import sys
sys.setrecursionlimit(10**5)


def dfs(ny, nx):
    global result
    visited[ny][nx] = 1
    if ny % 2:
        delta = delta_odd
    else:
        delta = delta_even

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < H+2 and 0 <= ex < W+2:
            if visited[ey][ex]:
                continue
            if graph[ey][ex]:
                result += 1
            else:
                dfs(ey, ex)


import sys
input = sys.stdin.readline

W, H = map(int, input().split())
graph = [[0 for _ in range(W+2)] for _ in range(H+2)]
for y in range(1, H+1):
    arr = list(map(int, input().split()))
    for x, num in enumerate(arr):
        graph[y][x+1] = num

# 건물이 아닌 좌표가 건물 안이 아닌 경우를 미리 탐색
result = 0
visited = [[0 for _ in range(W+2)] for _ in range(H+2)]
delta_even = [[0, -1], [-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1]]
delta_odd = [[0, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0]]

for y in range(H+2):
    for x in range(W+2):
        if 0 < y < H+1 and 0 < x < W+1:
            continue

        # 이미 확인했다면 패스
        if visited[y][x]:
            continue

        # 건물은 아니니까 패스
        if graph[y][x]:
            continue

        dfs(y, x)

# print(visited)
print(result)

"""
# 더 복잡하게 풀었던 첫 번째 풀이 : 계속 틀린건 delta_odd 정보를 틀려서...

import sys
sys.setrecursionlimit(10**5)


def dfs(ny, nx):
    visited[ny][nx] = 1
    if ny % 2:
        delta = delta_odd
    else:
        delta = delta_even

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < H and 0 <= ex < W:
            if visited[ey][ex]:
                continue
            if graph[ey][ex]:
                continue
            dfs(ey, ex)


import sys
input = sys.stdin.readline

W, H = map(int, input().split())
graph = []
cnt = 0
for _ in range(H):
    arr = list(map(int, input().split()))
    cnt += arr.count(1)
    graph.append(arr)
cnt *= 6

# 건물이 아닌 좌표가 건물 안이 아닌 경우를 미리 탐색
visited = [[0 for _ in range(W)] for _ in range(H)]
delta_odd = [[0, -1], [-1, -1], [-1, 0], [0, 1], [1, 0], [1, -1]]
delta_even = [[0, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0]]
for y in range(H):
    for x in range(W):
        if 0 < y < H-1 and 0 < x < W-1:
            continue

        # 이미 확인했다면 패스
        if visited[y][x]:
            continue

        # 건물은 아니니까 패스
        if graph[y][x]:
            continue

        dfs(y, x)

for y in range(H):
    for x in range(W):

        # 일단 해당 좌표가 건물일 때만 생각
        if graph[y][x] == 1:

            # x축 비교
            if x < W-1:
                if graph[y][x] == graph[y][x+1]:
                    cnt -= 2

            if y < H - 1:
                # y축이 홀수일 때
                if y % 2:
                    # 오른쪽 아래는 (x, y+1)
                    if graph[y][x] == graph[y+1][x]:
                        cnt -= 2
                    # 왼쪽 아래는 (x-1, y+1)
                    if x > 0:
                        if graph[y][x] == graph[y+1][x-1]:
                            cnt -= 2

                # y축이 짝수일 때
                else:
                    # 왼쪽 아래는 (x, y+1)
                    if graph[y][x] == graph[y+1][x]:
                        cnt -= 2
                    # 오른쪽 아래는 (x+1, y+1)
                    if x < W-1:
                        if graph[y][x] == graph[y+1][x+1]:
                            cnt -= 2

        # graph[y][x] == 0일 때, 바깥에 해당하는 visited 좌표가 아니라면 조명을 설치하지 않음
        else:
            if not visited[y][x]:
                visited[y][x] = 1
                if y % 2:
                    for dy, dx in delta_odd:
                        ey = y + dy
                        ex = x + dx
                        # 이미 아웃바운드에 있는건 필터링 되어 있다.
                        if graph[y][x] != graph[ey][ex]:
                            cnt -= 1
                else:
                    for dy, dx in delta_even:
                        ey = y + dy
                        ex = x + dx
                        if graph[y][x] != graph[ey][ex]:
                            cnt -= 1

print(cnt)
"""