# 1952번 달팽이
# https://www.acmicpc.net/problem/1952

M, N = map(int, input().split())
visited = [[False for _ in range(N)] for _ in range(M)]

# (0, 0) 좌표에서 시계 방향 출발이므로 오른쪽 이동을 먼저 한다.
# 방향이 바뀔 때마다 cnt + 1 하여 결과를 찾는다.
y = 0
x = 0
direction = "right"
cnt = 0
while True:
    # 방문 표시
    visited[y][x] = True

    # 방향으로 이동
    if direction == "right":
        # 만약 이동 예정인 곳이 범위 바깥이거나, 이미 방문했다면
        # 방향을 시계방향으로 바꾸고, 방향 전환 횟수를 카운트
        if x+1 == N or visited[y][x+1]:
            direction = "down"
            cnt += 1
            continue
        x += 1
    elif direction == "down":
        if y+1 == M or visited[y+1][x]:
            direction = "left"
            cnt += 1
            continue
        y += 1
    elif direction == "left":
        if x == 0 or visited[y][x-1]:
            direction = "up"
            cnt += 1
            continue
        x -= 1
    elif direction == "up":
        if y == 0 or visited[y-1][x]:
            direction = "right"
            cnt += 1
            continue
        y -= 1

    # 상하좌우 모두 방문했거나 범위 바깥이라면 종료
    if (x+1 == N or visited[y][x+1]) and (y+1 == M or visited[y+1][x]) \
            and (x == 0 or visited[y][x-1]) and (y == 0 or visited[y-1][x]):
        break

print(cnt)
