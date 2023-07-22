# 1920번 수 찾기
# https://www.acmicpc.net/problem/1920
import sys

input = sys.stdin.readline

n = int(input())
arr_n = set(list(map(int, input().split())))
m = int(input())
arr_m = list(map(int, input().split()))

for i in arr_m:
    if i in arr_n:
        print(1)
    else:
        print(0)