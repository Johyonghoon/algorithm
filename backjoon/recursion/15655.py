# 15655번 N과 M 7
# https://www.acmicpc.net/problem/15655

N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
ls = []

def recur():
    if len(ls) == M:
        print(*ls)
        return
    for i in arr:
        ls.append(i)
        recur()
        ls.pop()

recur()


