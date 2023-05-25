# 2805번 나무 자르기
# https://www.acmicpc.net/problem/2805

# not solved
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
total, start, end = 0, min(arr), max(arr)

while start <= end:
    h = (start + end) // 2
    print(start, end, h)
    for i in arr:
        if i > h:
            total += i - h
    if total == m:
        print(h)
        break
    elif total > m:
        start = h + 1
    else:
        end = h - 1
    total = 0
