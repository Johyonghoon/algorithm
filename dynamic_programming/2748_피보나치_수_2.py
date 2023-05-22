# 2748번 젠장
# https://www.acmicpc.net/problem/2748
import sys

input = sys.stdin.readline

n = int(input())
d = [0] * n


def fibonacci(x):
    if d[x] != 0:
        return d[x]
    if x == 0 or x == 1:
        return 1
    return fibonacci(x-1) + fibonacci(x-2)

for i in range(n):
    d[i] = fibonacci(i)

print(d[n-1])
