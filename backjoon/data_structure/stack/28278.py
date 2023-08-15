# 28278번 스택 2
# https://www.acmicpc.net/problem/28278

import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    arr = list(map(int, input().split()))

    if len(arr) == 2:
        command, X = arr
        if command == 1:    # push
            if 1 <= X <= 100_000:
                stack.append(X)

    elif len(arr) == 1:
        command = arr[0]
        if command == 2:    # pop
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command == 3:
            print(len(stack))
        elif command == 4:  # isEmpty
            if stack:
                print(0)
            else:
                print(1)
        elif command == 5:  # peek
            if stack:
                print(stack[-1])
            else:
                print(-1)
