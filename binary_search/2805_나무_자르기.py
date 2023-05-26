# 2805번 나무 자르기
# https://www.acmicpc.net/problem/2805

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

def binary_search(arr, target, start, end):
    result = 0
    while start <= end:
        mid = (start + end) // 2
        total = 0
        for i in arr:
            if i > mid:
                total += i - mid
        if total < target:
            end = mid - 1
        else:
            result = mid
            start = mid + 1
    return result

print(binary_search(arr, m, 0, max(arr)))
