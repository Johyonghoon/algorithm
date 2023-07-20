# 15649번 N과 M 1
# https://www.acmicpc.net/problem/15649

N, M = map(int, input().split())
arr = []

def recur():
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N+1):
        if i in arr:
            continue
        arr.append(i)
        recur()
        arr.pop()

recur()
