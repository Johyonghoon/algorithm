# 1932번 정수 삼각형
# https://www.acmicpc.net/problem/1932
from pprint import pprint
import sys
input = sys.stdin.readline

# dfs 가 아닌 dp 문제였다.
n = int(input())
tri = []
for _ in range(n):
    tri.append(list(map(int, input().split())))

for idx in range(n-2, -1, -1):
    for j in range(idx+1):
        tri[idx][j] += max(tri[idx+1][j], tri[idx+1][j+1])

print(tri[0][0])



