# 2775번 부녀회장이 될테야
# https://www.acmicpc.net/problem/2775
import sys

input = sys.stdin.readline

def dp(x, y):
    if ls[x][y] != 0:
        return ls[x][y]
    if y == 0:
        return 1
    return dp(x-1, y) + dp(x, y-1)

t = int(input())
while t != 0:
    k, n = [int(input()) for _ in range(2)]
    ls = [[i+1 for i in range(n)]] + [[0 for _ in range(n)] for _ in range(k)]
    for j in range(1, k+1):
        for l in range(n):
            ls[j][l] = dp(j, l)
    print(ls[k][n-1])
    t -= 1
