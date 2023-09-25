# 22233번 가희와 키워드
# https://www.acmicpc.net/problem/22233

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
keyword = set()
for _ in range(N):
    keyword.add(input().strip())

used = set()
for _ in range(M):
    arr = input().strip().split(",")
    for word in arr:
        if word in keyword:
            used.add(word)

    print(N - len(used))


