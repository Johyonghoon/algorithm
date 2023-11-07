# 9252번 LCS 2
# https://www.acmicpc.net/problem/9252


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

i = M
j = N
result = ['' for _ in range(LCS[M][N])]
length = LCS[M][N] - 1
while length >= 0:
    if i-1 >= 0 and LCS[i][j] == LCS[i-1][j]:
        i -= 1
    elif j-1 >= 0 and LCS[i][j] == LCS[i][j-1]:
        j -= 1
    else:
        result[length] = Y[i-1]
        i -= 1
        j -= 1
        length -= 1

print(LCS[M][N])
print(''.join(result))
