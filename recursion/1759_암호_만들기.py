# 1759번 암호 만들기
# https://www.acmicpc.net/problem/1759

L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
pwd = []
aeiou = ['a', 'e', 'i', 'o', 'u']
limit = 0
result = []

def recur():

    global limit

    if len(pwd) == L:
        mo = []
        for i in pwd:
            if i in aeiou:
                mo.append(i)
        if len(mo) > 0:
            if len(pwd) - len(mo) >= 2:
                result.append(''.join(pwd))
                # [print(i, end="") for i in pwd]
            # print()
        return

    for i in arr:
        if i in pwd:
            continue
        if arr.index(i) < limit:
            continue
        pwd.append(i)
        recur()
        pwd.pop()
        limit = arr.index(i) + 1

recur()
[print(i) for i in result]
