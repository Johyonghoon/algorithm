# 14568번 2017 연세대학교 프로그래밍 경시대회
# https://www.acmicpc.net/problem/14568

candy = int(input())
cnt = 0

for A in range(0, candy+1):
    for B in range(0, candy+1):
        for C in range(0, candy+1):
            if A + B + C == candy:
                if A >= B + 2:
                    if A != 0 and B != 0 and C != 0:
                        if C % 2 == 0:
                            cnt += 1

print(cnt)

"""
n = int(input())
cnt = 0
for i in range(1, n):
    for j in range(i+2, n):
        x = n - i - j
        if x <= 0:
            break
        if x % 2 == 0:
            cnt += 1

print(cnt)
"""