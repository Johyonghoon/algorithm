# 2589번 보물섬
# https://www.acmicpc.net/problem/2589

height, length = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(height)]
result = 0

# 보물은 서로 간 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 두 곳에 위치
for y in range(height):
    for x in range(length):
        # 육지로만 이동 가능
        if graph[y][x] == "L":
            # (x, y) 좌표에서 이동할 때의 최단 거리
            distance = [[0 for _ in range(length)] for _ in range(height)]
            visited = [[False for _ in range(length)] for _ in range(height)]
            for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                ey, ex = y - dy, x - dx

                if 0 <= ey < height and 0 <= ex < length:
                    if not visited[ey][ex] and graph[ey][ex] == "L":
                        distance[ey][ex] = distance[y][x] + 1
                        visited[ey][ex] = True

            result = max(result, max(map(max, distance)))

print(result)
