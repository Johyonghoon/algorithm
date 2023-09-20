# 19949번 영재의 시험
# https://www.acmicpc.net/problem/19949

import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def recur(node, cnt, prv, pprv, arr):
    global result
    if cnt + 10 - node < 5:
        return

    if node == 10:
        if cnt >= 5:
            result += 1
        return

    for idx in range(1, 6):
        if idx == prv and idx == pprv:
            continue
        arr.append(idx)
        if idx == ans[node]:
            recur(node + 1, cnt + 1, idx, prv, arr)
        else:
            recur(node + 1, cnt, idx, prv, arr)
        arr.pop()


ans = list(map(int, input().split()))
result = 0
recur(0, 0, -1, -1, [])
print(result)