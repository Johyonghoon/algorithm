# 15828번 Router
# https://www.acmicpc.net/problem/15828
import sys

input = sys.stdin.readline

N = int(input())
arr = []

while True:
    packet = int(input())
    if packet == -1:
        break
    if packet == 0:
        arr.pop(0)
        continue
    if len(arr) < N:
        arr.append(packet)

if len(arr) == 0:
    print("empty")
else:
    print(*arr)

"""
from collections import deque
import sys

input = sys.stdin.readline
N = int(input())
arr = deque()
packet = 0

while packet != -1:
    packet = int(input())
    if packet == 0:
        arr.popleft()
        continue
    else:
        if len(arr) < N:
            if packet != -1:
                arr.append(packet)


if arr:
    print(*arr)
else:
    print("empty")
"""
