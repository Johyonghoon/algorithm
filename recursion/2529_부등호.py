# 2529번 부등호
# https://www.acmicpc.net/problem/2529

k = int(input())
arr = list(input().split())
ls = []
result = []

def recur():
    if len(ls) == k+1:
        num = "".join(map(str, ls))
        result.append(num)
        return
    for i in range(10):
        if len(ls) == 0:
            ls.append(i)
            recur()
            ls.pop()
            continue
        if arr[len(ls)-1] == "<" and ls[-1] < i:
            if i in ls:
                continue
            ls.append(i)
            recur()
            ls.pop()

        elif arr[len(ls)-1] == ">" and ls[-1] > i:
            if i in ls:
                continue
            ls.append(i)
            recur()
            ls.pop()

recur()
print(result[-1])
print(result[0])
