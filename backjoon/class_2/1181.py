# 1181번 단어 정렬
# https://www.acmicpc.net/problem/1181
import sys

n = int(input())
arr = []
for _ in range(n):
    x = sys.stdin.readline().rstrip()
    arr.append((len(x), x))
arr = list(set(arr))
arr.sort()
for i in arr:
    print(i[1])
