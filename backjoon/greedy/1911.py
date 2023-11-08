# 1911번 흙길 보수하기
# https://www.acmicpc.net/problem/1911

import sys

input = sys.stdin.readline

N, L = map(int, input().split())
pool = []
for _ in range(N):
    s, e = map(int, input().split())
    pool.append((s, e))
pool.sort()

result = 0
idx = 0
pointer = pool[0][0]
last = pool[-1][1]
while idx < N:
    start, end = pool[idx]

    if pointer < start:
        pointer = start

    cnt = (end - pointer) // L
    if (end - pointer) % L:
        cnt += 1
    pointer += L * cnt
    result += cnt
    idx += 1
    # print(pointer, result, idx)

print(result)
