# 10250번 ACM 호텔
# https://www.acmicpc.net/problem/10250
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    H, W, N = map(int, input().split())
    if N % H == 0:
        room_num = H * 100 + N // H
    else:
        room_num = N % H * 100 + N // H + 1
    print(room_num)