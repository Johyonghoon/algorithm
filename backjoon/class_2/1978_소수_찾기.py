# 1978번 소수 찾기
# https://www.acmicpc.net/problem/1978
from collections import defaultdict

n = int(input())
arr = list(map(int, input().split()))
cnt = n

for i in arr:
    if i == 1:
        cnt -= 1
    else:
        for j in range(2, i):
            if i % j == 0:
                cnt -= 1
                break

print(cnt)
