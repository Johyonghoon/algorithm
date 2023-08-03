import sys
from pprint import pprint

# sys.stdin = open("input.txt")

N, M = map(int, input().split())

# 성 그리기
arr = []
for _ in range(N):
    ls = list(input().replace(".", "0").replace("X", "1"))
    ls = [int(i) for i in ls]
    arr.append(ls)

# 결과값 초기화
result = 0

# x축과 y축 양쪽 다 없는 경우를 먼저 채우면 최소값을 완성할 수 있다.
for y in range(N):
    for x in range(M):
        need_security = True
        for ax in range(M):
            if arr[y][ax]:
                need_security = False
        for ay in range(N):
            if arr[ay][x]:
                need_security = False
        if need_security:
            arr[y][x] = 1
            result += 1

# x축 또는 y축 단독으로 없는 경우 채워주기
for y in range(N):
    need_security = True
    for x in range(M):
        if arr[y][x] == 1:
            need_security = False
    if need_security:
        arr[y][0] = 1
        result += 1

for x in range(M):
    need_security = True
    for y in range(N):
        if arr[y][x] == 1:
            need_security = False
    if need_security:
        arr[0][x] = 1
        result += 1


print(result)
