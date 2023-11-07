# 9251번 LCS
# https://www.acmicpc.net/problem/9251


X = list(input())
Y = list(input())

N = len(X)
M = len(Y)

LCS = [[0 for _ in range(N+1)] for _ in range(M+1)]
for y in range(M+1):
    for x in range(N+1):
        if x == 0 or y == 0:
            LCS[y][x] = 0
        elif Y[y-1] == X[x-1]:
            LCS[y][x] = LCS[y-1][x-1] + 1
        else:
            LCS[y][x] = max(LCS[y-1][x], LCS[y][x-1])


print(LCS[M][N])
