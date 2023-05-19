# 4158번 CD
# https://www.acmicpc.net/problem/4158
# not solved

import sys
input = sys.stdin.readline


def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    array_n = [input() for i in range(n)]
    array_m = [input() for i in range(m)]
    result = 0

    for k in array_n:
        result += binary_search(array_m, k, 0, m-1)

    print(result)
