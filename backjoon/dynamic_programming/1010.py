# 1010번 다리 놓기
# https://www.acmicpc.net/problem/1010

t = int(input())

while t != 0:
    n, m = map(int, input().split())
    x = [1] * m
    y = [1] * n
    for i in range(m-n, m):
        x[i] = x[i-1] * (i+1)
    for i in range(1, n):
        y[i] = y[i-1] * (i+1)
    print(x[m-1] // y[n-1])
    t -= 1