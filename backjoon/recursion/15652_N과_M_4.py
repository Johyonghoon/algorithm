# 15652번 N과 M 4
# https://www.acmicpc.net/problem/15652

N, M = map(int, input().split())
arr = []
limit = -1

def recur(limit):
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N+1):
        if i < limit:
            continue
        arr.append(i)
        recur(limit)
        limit = i+1
        arr.pop()

recur(limit)
