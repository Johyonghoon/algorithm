# 16198번 에너지 모으기
# https://www.acmicpc.net/problem/16198

import sys
sys.setrecursionlimit(10**9)


def recur(cnt, total):
    global weights, result
    if cnt <= 2:
        result = max(result, total)
        return
    # 문제 조건) 첫 번째와 마지막 에너지 구슬은 고를 수 없다.
    for idx in range(1, cnt-1):
        popped = weights.pop(idx)
        recur(cnt-1, total + weights[idx-1] * weights[idx])
        weights.insert(idx, popped)


N = int(input())
result = 0
weights = list(map(int, input().split()))

recur(N, 0)
print(result)
