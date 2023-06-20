# 6131번 완전 제곱수
# https://www.acmicpc.net/problem/6131

N = int(input())
cnt = 0

for B in range(1, 501):
    for A in range(B, 501):
        if A ** 2 == B ** 2 + N:
            cnt += 1
        if A ** 2 - N > B ** 2:
            break

print(cnt)