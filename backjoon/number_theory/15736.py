# 15736번 청기 백기
# https://www.acmicpc.net/problem/15736

cnt = 0
n = int(input())
for i in range(1, int(n ** (1/2)) + 1):
    if i ** 2 > 2100000000:
        break
    cnt += 1

print(cnt)
