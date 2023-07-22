# 11047번 동전 0
# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
arr = []
total = 0
for _ in range(n):
    arr.append(int(input()))
arr.reverse()

for i in arr:
    if k // i > 0:
        total += (k // i)
        k = k % i

print(total)