# 2292번 벌집
# https://www.acmicpc.net/problem/2292

n = int(input())
cnt = 1
x = 1

if n == 1:
    pass
else:
    while True:
        x += 6 * cnt
        cnt += 1
        if x >= n:
            break

print(cnt)
