# 14568번 2017 연세대학교 프로그래밍 경시대회
# https://www.acmicpc.net/problem/14568

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
