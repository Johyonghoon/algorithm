import sys
from pprint import pprint

sys.stdin = open("input.txt")

N, M = map(int, input().split())

# 성 그리기
arr = []
for _ in range(N):
    ls = list(input().replace(".", "0").replace("X", "1"))
    ls = [int(i) for i in ls]
    arr.append(ls)

# x축과 y축 모두
for y in range(N):
    for x in range(M):

