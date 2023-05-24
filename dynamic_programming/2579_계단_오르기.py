# 2579번 계단 오르기
# https://www.acmicpc.net/problem/2579

# not solved

n = int(input())
arr = []
d = [0 for _ in range(n)]
for _ in range(n):
    arr.append([int(input()), 1])
print(arr)
for i in range(3, n):
    arr[i] += max(arr[i-1], arr[i-2])
print(arr[n-1])
