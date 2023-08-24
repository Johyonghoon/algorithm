# 10157번 자리배정
# https://www.acmicpc.net/problem/10157

width, height = map(int, input().split())
graph = [[0 for _ in range(width)] for _ in range(height)]
N = int(input())

# 좌석을 배정할 수 없는 경우
if N > width * height:
    print(0)
else:
    # 좌표 초기화
    y = 0
    x = 0

    # 방향의 경우 프로그래밍에서는 y축 좌표가 위에 있으므로 반대로 생각하자
    direction = "D"     # D R U L 순서로 이동한다.

    # 1번부터 시작
    idx = 1
    graph[y][x] = idx

    while idx < N:
        # print(idx, y, x)
        # 아래 방향(실제로는 위 방향)
        if direction == "D":
            if y == height-1 or graph[y+1][x]:
                direction = "R"
                x += 1
            else:
                y += 1

        # 오른쪽 방향(실제로도 오른쪽 방향)
        elif direction == "R":
            if x == width-1 or graph[y][x+1]:
                direction = "U"
                y -= 1
            else:
                x += 1

        # 위 방향(실제로는 아래 방향)
        elif direction == "U":
            if y == 0 or graph[y-1][x]:
                direction = "L"
                x -= 1
            else:
                y -= 1

        # 왼쪽 방향(실제로도 왼쪽 방향)
        elif direction == "L":
            if x == 0 or graph[y][x-1]:
                direction = "D"
                y += 1
            else:
                x -= 1

        # 이동한 인덱스에 값을 추가
        idx += 1
        graph[y][x] = idx

    # print(graph)
    # 인덱스로 계산했으므로, 실제 좌표는 1부터기 때문에 +1
    print(x+1, y+1)
