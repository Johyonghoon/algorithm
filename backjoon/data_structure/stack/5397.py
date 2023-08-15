# 5397번 키로거
# https://www.acmicpc.net/problem/5397

import sys
input = sys.stdin.readline

T = int(input())
for tc in range(1, T+1):
    input_data = list(input().strip())
    left = []
    right = []
    for data in input_data:
        if data == "<":
            if left: right.append(left.pop())
        elif data == ">":
            if right: left.append(right.pop())
        elif data == "-":
            if left: left.pop()
        else:
            left.append(data)

    right.reverse()
    print("".join(left) + "".join(right))

