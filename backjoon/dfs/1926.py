# 1926번 그림
# https://www.acmicpc.net/problem/1926

import sys
sys.setrecursionlimit(10**9)


def recur(ny, nx, cnt):
    graph[ny][nx] = 0
    cnt += 1

    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey, ex = ny + dy, nx + dx
        if 0 <= ey < n and 0 <= ex < m:
            if not graph[ey][ex]:
                continue
            cnt = recur(ey, ex, cnt)

    return cnt


# 그림 정보 저장
n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 가장 넓은 그림의 넓이를 담을 배열 초기화
result = []
for y in range(n):
    for x in range(m):
        if not graph[y][x]:
            continue
        # dfs로 방문한 그림 좌표의 면적을 확인
        area = recur(y, x, 0)
        result.append(area)

# 그림의 개수와 가장 넓은 그림의 넓이를 출력
result.sort()
print(len(result))
if len(result):
    print(result[-1])
# 그림이 하나도 없는 경우 가장 넓은 그림의 넓이는 0
else:
    print(0)
