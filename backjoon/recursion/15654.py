# 15654번 N과 M 6
# https://www.acmicpc.net/problem/15654

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ls = []
limit = -1

def recur(limit):
    if len(ls) == M:
        print(*ls)
        return
    for i in arr:
        if i in ls:
            continue
        if i < limit:
            continue
        ls.append(i)
        recur(limit)
        limit = i+1
        ls.pop()

recur(limit)
