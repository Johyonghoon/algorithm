# 11660번 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660
import numpy as np
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[0 for _ in range(N+1)]]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))
# print(np.array(arr))
# prefix = [i for i in arr]

for i in range(1, N+1):
    for j in range(1, N+1):
        arr[i][j] += arr[i-1][j] + arr[i][j-1] - arr[i-1][j-1]
# print(np.array(prefix))

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    # print(prefix[x2][y2], prefix[x2][y1-1], prefix[x1-1][y2], prefix[x1-1][y1-1])
    print(arr[x2][y2] - arr[x2][y1-1] - arr[x1-1][y2] + arr[x1-1][y1-1])
