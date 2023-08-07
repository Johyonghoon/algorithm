# 18111번 마인크래프트
# https://www.acmicpc.net/problem/18111
import sys
input = sys.stdin.readline

"""
# 시간 초과
모든 땅의 높이에 대한 평균값을 구하여 그 평균값을 버림한 값부터 증가시키며
최소 시간 내에 작업을 마무리할 수 있는 방법을 찾는다.
# try
블럭을 쌓는 것보다 제거하는 것이 시간이 더 많이 드므로 최대 높이부터 낮추어가며 구한다.
"""

# 기본 정보 입력
N, M, B = map(int, input().split())
graph = []
total = 0
for _ in range(N):
    arr = list(map(int, input().split()))
    graph.append(arr)
    total += sum(arr)

# 평균 높이 구하기
avg = int(total / (N * M))

# 평균값에 가까운 높이부터 점차 높여가며 최소 시간을 찾는다.
mini = 1_000_000_000
i = -1
while True:

    # 만약 블록 개수가 부족하다면 중단
    if total + B < (avg + i + 1) * N * M:
        break

    time = 0
    i += 1

    for y in range(N):
        for x in range(M):
            if graph[y][x] < (avg+i):
                time += (avg+i) - graph[y][x]
            elif graph[y][x] > (avg+i):
                time += 2 * (graph[y][x] - (avg+i))

    # 만약 최소 시간을 오버한다면 중단
    if mini >= time:
        mini = time
    else:
        i -= 1
        break

print(mini, avg+i)

