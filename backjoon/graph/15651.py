# 15651번 N과 M 3
# https://www.acmicpc.net/problem/15651

N, M = map(int, input().split())
arr = []

def recur():
    if len(arr) == M:
        print(*arr)
        return
    for i in range(1, N+1):
        arr.append(i)
        recur()
        arr.pop()

recur()
