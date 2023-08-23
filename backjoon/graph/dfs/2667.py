# 2667번 단지번호붙이기
# https://www.acmicpc.net/problem/2667

import sys
sys.setrecursionlimit(10**9)


def recur(ny, nx, cnt):
    # 방문 정보 저장 // 개수 세기
    graph[ny][nx] = 0
    cnt += 1

    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ey, ex = ny + dy, nx + dx
        if 0 <= ey < N and 0 <= ex < N:
            if not graph[ey][ex]:
                continue
            cnt = recur(ey, ex, cnt)

    return cnt


# 지도 정보 입력
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(input()))))

# 단지 집 개수를 저장할 배열 초기화
result = []
# 방문하지 않은 단지를 dfs로 탐색하며 개수 저장
for y in range(N):
    for x in range(N):
        if not graph[y][x]:
            continue
        result.append(recur(y, x, 0))

result.sort()
print(len(result))
[print(i) for i in result]
