# 11399번 ATM
# https://www.acmicpc.net/problem/11399

n = int(input())
arr = sorted(list(map(int, input().split())))
arr.reverse()
total = 0

for i in range(n):
    total += arr[i] * (i+1)

print(total)
