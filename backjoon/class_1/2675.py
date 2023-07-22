# 2675번 문자열 반복
# https://www.acmicpc.net/problem/2675

t = int(input())
ls = []
for i in range(t):
    char = ""
    a, b = input().split()
    a = int(a)
    for j in b:
        char += j * a
    ls.append(char)
[print(i) for i in ls]
