# 2751번 수 정렬하기 2
# https://www.acmicpc.net/problem/2751
import sys

arr = []
n = int(input())
for _ in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
arr.sort()
[print(i) for i in arr]
