import sys
input = sys.stdin.readline

"""
N * M 의 배열
K = 테스트 개수
(i, j) ~ (x, y) 범위의 합 구하기

1. 배열 그리기
2. 각 테스트에 대해
3. (i, j) ~ (x, y) 범위 찾기
4. 완전탐색 => 시간초과
5. 누적합하여 각 좌표까지의 합을 구하기
6. (1, 1) ~ (x, y)까지 합하여 (x, y) 좌표에 저장
7. (i, j) ~ (x, y)의 합을 구하려면
8. 누적합의 값이 저장되어 있는 (x, y) - (i-1, y) - (x, j-1) + (i+1 + j+1)
"""

N, M = map(int, input().split())
# N * M 배열 구하기
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

# 누적합
for y in range(N):
    for x in range(M):
        if x > 0:
            graph[y][x] += graph[y][x-1]
        if y > 0:
            graph[y][x] += graph[y-1][x]
        if x > 0 and y > 0:
            graph[y][x] -= graph[y-1][x-1]

# 테스트 개수
K = int(input())
for _ in range(K):
    # 근데 왜 x y 좌표가 바뀌었지?
    j, i, y, x = map(int, input().split())
    # 인덱스는 0부터 시작하지만 좌표는 (1, 1)부터 시작하므로 모두 1만큼 빼준다.
    i, j, x, y = i-1, j-1, x-1, y-1
    # 누적합을 활용하여 해당 범위의 값의 합을 구하기
    result = graph[y][x]
    if i > 0:
        result -= graph[y][i-1]
    if j > 0:
        result -= graph[j-1][x]
    if i > 0 and j > 0:
        result += graph[j-1][i-1]
    print(result)
