# 1018번 체스판 다시 칠하기
# https://www.acmicpc.net/problem/1018
import sys

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

result = int(1e9)
for i in range(n-7):
    for j in range(m-7):
        score_1, score_2 = 0, 0
        for k in range(8):
            for l in range(8):
                if (i + j + k + l) % 2 == 0:
                    if arr[i+k][j+l] == "W":
                        score_1 += 1
                    else:
                        score_2 += 1
                else:
                    if arr[i+k][j+l] == "B":
                        score_1 += 1
                    else:
                        score_2 += 1
        result = min(result, score_1, score_2)

print(result)

"""
import sys

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(sys.stdin.readline().rstrip()))

chessboard_1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
                ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
                ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

result = int(1e9)
for i in range(n-7):
    for j in range(m-7):
        score_1, score_2 = 0, 0
        for k in range(8):
            for l in range(8):
                if arr[i+k][j+l] == chessboard_1[k][l]:
                    score_2 += 1
                else:
                    score_1 += 1
        result = min(result, score_1, score_2)

print(result)

"""