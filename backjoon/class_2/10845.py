# 10845번 큐
# https://www.acmicpc.net/problem/10845
import sys
from collections import deque

input = sys.stdin.readline

d = deque()
N = int(input())
for _ in range(N):
    ls = list(input().split())
    if len(ls) == 2:
        d.append(ls[1])
    else:
        command = ls[0]
        if command == "pop":
            if d:
                print(d.popleft())
            else:
                print(-1)
        elif command == "size":
            print(len(d))
        elif command == "empty":
            if len(d):
                print(0)
            else:
                print(1)
        elif command == "front":
            if d:
                print(d[0])
            else:
                print(-1)
        else:
            if d:
                print(d[-1])
            else:
                print(-1)