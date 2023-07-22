# 1476번 날짜 계산
# https://www.acmicpc.net/problem/1476

E, S, M = map(int, input().split())
A, B, C, year = 1, 1, 1, 1

while True:
    if A == E and B == S and C == M:
        print(year)
        break
    A += 1
    B += 1
    C += 1
    year += 1
    if A == 15+1:
        A = 1
    if B == 28+1:
        B = 1
    if C == 19+1:
        C = 1

