# 10809번 알파벳 찾기
# https://www.acmicpc.net/problem/10809

x = input()
d = [-1 for _ in range(26)]

for i, j in enumerate(x):
    if d[ord(j) - 97] == -1:
        d[ord(j) - 97] = i

print(*d)
