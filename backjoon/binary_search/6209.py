# 6209번 제자리 멀리뛰기
# https://www.acmicpc.net/problem/6209

import sys

input = sys.stdin.readline


def parametric_search():
    global result
    start = 0
    end = d
    cnt = 0

    while start <= end:
        mid = (start + end) // 2
        dist = 0
        cnt = 0
        for idx in range(n+1):
            dist += stone[idx+1] - stone[idx]
            if dist >= mid:
                dist = 0
            else:
                cnt += 1

        if cnt > m:
            end = mid - 1
        else:
            start = mid + 1
            result = max(result, mid)
        # print(result, mid, cnt)


d, n, m = map(int, input().split())
stone = [0, d]
for _ in range(n):
    stone.append(int(input()))
stone.sort()
# print(stone)

result = 0
parametric_search()

print(result)
