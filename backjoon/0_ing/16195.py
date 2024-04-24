"""
m개 이하의 수
0   0   0   0   0
1   1   0   0   0
2   1   1   0   0
3   1   2   1   0
4   0   3   3   1
5   0   0   6   4   1
6   0   0   0   10  5   1
7   0   0
"""

DP = [[0 for i in range(1001)] for j in range(1001)]
DP[1][1] = 1
DP[2][1] = 1
DP[2][2] = 1
DP[3][1] = 1
DP[3][2] = 2
DP[3][3] = 1
for y in range(4, 1001):
    for x in range(y+1):
        DP[y][x] = (DP[y-1][x-1] + DP[y-2][x-1] + DP[y-3][x-1]) % 1_000_000_009

# 디버깅
# for y in range(1001):
#     print(y, *DP[y][:10])

Q = int(input())
for i in range(Q):
    N, M = map(int, input().split())
    result = 0
    for x in range(M+1):
        result += DP[N][x]
    print(result % 1_000_000_009)