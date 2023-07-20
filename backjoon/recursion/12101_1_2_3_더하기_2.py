# 12101번 1, 2, 3 더하기 2
# https://www.acmicpc.net/problem/12101

n, k = map(int, input().split())
arr = []
result = []

def recur():
    if sum(arr) == n:
        result.append(tuple(arr))
        return
    for i in range(1, 4):
        if sum(arr) + i > n:
            continue
        arr.append(i)
        recur()
        arr.pop()

recur()

if len(result) < k:
    print(-1)
else:
    for idx, value in enumerate(result[k-1]):
        if idx == len(result[k-1])-1:
            print(value)
        else:
            print(value, end="+")
