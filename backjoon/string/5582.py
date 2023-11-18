# 5582번 공통 부분 문자열
# https://www.acmicpc.net/problem/5582

"""
연속하는 부분문자열을 찾는 문제
연속성이 사라지면 결과를 지워야 한다.
    A   B   R   A   C   A   D   A   B   R   A
E   0   0   0   0   0   0   0   0   0   0   0
C   0   0   0   0   1   0   0   0   0   0   0
A   1   0   0   1   0   2   0   1   0   0   1
D   0   0   0   0   0   0   3   0   0   0   0
A   1   0   0   1   0   1   0   4   0   0   1
D   0   0   0   0   0   0   2   0   0   0   0
A   1   0   0   1   0   1   0   3   0   0   0
B   0   2   0   0   0   0   0   0   4   0   0
R   0   0   3   0   0   0   0   0   0   5   0
B   0   0   1   0   0   0   0   0   1   0   0
C   0   0   0   0   1   0   0   0   0   0   0
R   0   0   1   0   0   0   0   0   0   1   0
D   0   0   0   0   0   0   1   0   0   0   0
A   1   0   0   1   0   1   0   2   0   0   1
R   0   0   1   0   0   0   0   0   0   1   0
A   1   0   0   2   0   1   0   1   0   0   2
"""


X = list(input())
Y = list(input())

N = len(X)
M = len(Y)

# 0번째 인덱스는 비워두기 위함
dp = [[0 for _ in range(N+1)] for _ in range(M+1)]

for y in range(1, M+1):
    for x in range(1, N+1):
        if X[x-1] == Y[y-1]:
            if dp[y-1][x-1]:
                dp[y][x] = dp[y-1][x-1] + 1
            else:
                dp[y][x] = 1

result = 0
for y in range(1, M+1):
    for x in range(1, N+1):
        result = max(result, dp[y][x])

print(result)
