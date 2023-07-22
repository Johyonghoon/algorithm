# 15653번 N과 M 5
# https://www.acmicpc.net/problem/15653

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ls = []

def recur():
    if len(ls) == M:
        print(*ls)
        return
    for i in arr:
        if i in ls:
            continue
        ls.append(i)
        recur()
        ls.pop()

recur()

