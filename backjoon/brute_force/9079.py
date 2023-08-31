# 9079번 동전 게임
# https://www.acmicpc.net/problem/9079

import numpy as np
from copy import deepcopy


def turn(x):
    if x:
        return 0
    else:
        return 1


def isAnswer(arr, g):
    global result

    # 동전 뒤집기
    for idx in arr:
        for ny, nx in turning[idx]:
            g[ny][nx] = turn(g[ny][nx])
    # print(np.array(g))
    # 현재 상태의 완성 여부 확인
    total = 0
    for ny in range(3):
        total += sum(g[ny])

    if total == 0 or total == 9:
        result = min(result, len(arr))
        return True
    else:
        return False


def recur(node, arr):
    # print(arr)
    if isAnswer(arr, deepcopy(graph)):
        return

    for nxt in range(node+1, 8):
        # 동전 뒤집기
        arr.append(nxt)
        recur(nxt, arr)
        arr.pop()
        # 동전 뒤집지 않기
        recur(nxt, arr)


T = int(input())
for tc in range(1, T+1):
    graph = []
    # H = 0 / T = 1 로 변환
    for _ in range(3):
        input_data = input().replace("H", "0").replace("T", "1")
        graph.append(list(map(int, input_data.split())))

    # 최대로 뒤집는 경우의 수 = 8
    result = 9

    # 뒤집는 경우의 수
    turning = []
    for i in range(3):
        arr1 = []
        arr2 = []
        for j in range(3):
            arr1.append([i, j])
            arr2.append([j, i])
        turning.append(arr1)
        turning.append(arr2)

    arr3 = []
    arr4 = []
    for i in range(3):
        arr3.append([i, i])
        arr4.append([i, 2-i])
    turning.append(arr3)
    turning.append(arr4)

    recur(-1, [])
    if result == 9:
        print(-1)
    else:
        print(result)



