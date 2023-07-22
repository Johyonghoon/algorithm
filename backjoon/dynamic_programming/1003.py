# 1003 피보나치 함수
# https://www.acmicpc.net/problem/1003

t = int(input())
d = [[0, 0] for _ in range(41)]

while t != 0:
    n = int(input())
    d[:2] = [[1, 0], [0, 1]]
    for i in range(2, n+1):
        if d[i] != [0, 0]:
            continue
        for j in range(2):
            d[i][j] = d[i-1][j] + d[i-2][j]
    print(*d[n])
    t -= 1

"""
d[n] = d[n-1] + d[n-2]

d[0] = 1 * d[0] + 0 * d[1]
d[1] = 0 * d[0] + 1 * d[1]
d[2] = 1 * d[0] + 1 * d[1]
d[3] = 1 * d[0] + 2 * d[1]
d[4] = 2 * d[0] + 3 * d[1]
d[5] = 3 * d[0] + 5 * d[1] 
"""