# 17140번 이차원 배열과 연산
# https://www.acmicpc.net/problem/17140

"""
R 연산 : 배열 A의 모든 행에 대해서 정렬을 수행 (행의 개수 >= 열의 개수인 경우 적용)
C 연산 : 배열 A의 모든 열에 대해서 정렬을 수행 (열의 개수 > 행의 개수인 경우 적용)

1. 각각의 수가 몇 번 나왔는지 파악
2. 수의 등장 횟수가 커지는 순 (오름차순 : 개수가 작은 수 -> 개수가 큰 수)
3. 수가 커지는 순으로 정렬 (오름차순 : 작은 수 -> 큰 수)
4. 이후, 배열 A에 정렬된 결과를 넣기
5. 결과를 넣을 때 수와 등장 횟수를 모두 넣으며, 순서는 수가 먼저다.
  ex) [3, 1, 1] -> [3, 1, 1, 2] -> [3, 1, 2, 1, 1, 1]
6. 정렬된 결과를 배열에 다시 넣으면 행/열의 크기가 변한다.
  - R 연산 시 가장 큰 행을 기준으로 모든 행의 크기가 변한다.
  - C 연산 시 가장 큰 열을 기준으로 모든 열의 크기가 변한다.
  - 행/열의 크기가 커진 곳에는 0이 채워진다.
  - 수를 정렬할 때는 0은 무시한다.
    ex) [3, 2, 0, 0] -> [3, 1, 2, 1]
7. 행 또는 열의 크기가 100을 넘어가는 경우에는 처음 100개를 제외한 나머지는 버린다.

배열 A에 들어있는 수와 r, c, k가 주어질 때 A[r][c]에 들어있는 값이 k가 되기 위한 최소 시간?
"""

import sys
from collections import defaultdict
input = sys.stdin.readline


def toggle_axis(r, c, g):
    new_g = [[0 for _ in range(r)] for _ in range(c)]
    for y in range(r):
        for x in range(c):
            new_g[x][y] = g[y][x]
    return new_g


def counting_sort(arr):
    # 수의 개수 구하기
    d = defaultdict(int)
    for num in arr:
        if num:
            d[num] += 1

    # 수의 개수가 같은 것을 구하기
    count_d = dict()
    for k, v in d.items():
        if v not in count_d:
            count_d[v] = set()
        count_d[v].add(k)

    # 수의 개수가 작은 수 중에 작은 수부터 개수 구하기
    cnt = 0
    new_arr = []
    for k, v in sorted(count_d.items()):  # k: 개수 v: 수의 목록
        for num in sorted(list(v)):
            # 배열의 개수는 100개를 넘기지 않는다.
            if cnt == 50:
                break
            new_arr.append(num)
            new_arr.append(k)
            cnt += 1
    return new_arr, cnt * 2


R, C, K = map(int, input().split())
# 인덱스는 0부터 시작하는 것을 보정
R -= 1
C -= 1
graph = []
for _ in range(3):
    graph.append(list(map(int, input().split())))

time = 0
is_answer = False
while time <= 100:
    # 행/열의 길이
    Y = len(graph)
    X = len(graph[0])

    # 목표에 도달했을 때 종료
    if R < Y and C < X:
        if graph[R][C] == K:
            is_answer = True
            break

    # 시간 세기
    time += 1

    # 행의 길이가 열의 길이보다 길거나 같을 때? R 연산
    # 열의 길이가 행의 길이보다 길 때? C 연산
    # x축 배열을 구하기가 귀찮으므로 y, x축을 서로 변경하면 어떨까
    is_toggle = False
    if Y < X:
        graph = toggle_axis(Y, X, graph)
        is_toggle = True
        Y, X = X, Y

    new_graph = []
    lengths = []
    # 배열을 순회하며 개수로 정렬된 수를 저장
    for idx in range(Y):
        sorted_y, length = counting_sort(graph[idx])
        new_graph.append(sorted_y)
        lengths.append(length)

    # 0 추가하기
    max_length = max(lengths)
    for idx in range(Y):
        new_graph[idx] += [0] * (max_length - lengths[idx])

    # 토글되었었다면 다시 뒤집어주기
    if is_toggle:
        new_graph = toggle_axis(len(new_graph), len(new_graph[0]), new_graph)

    graph = new_graph


if is_answer:
    print(time)
else:
    print(-1)
