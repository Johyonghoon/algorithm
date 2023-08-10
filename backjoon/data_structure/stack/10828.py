# 10828번 스택
# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    arr = list(input().strip().split())
    if len(arr) == 1:
        command = arr[0]
        if command == "pop":
            if stack:
                print(stack.pop())
            else:
                print(-1)
        elif command == "size":
            print(len(stack))
        elif command == "empty":
            if len(stack):
                print(0)
            else:
                print(1)
        elif command == "top":
            if stack:
                print(stack[-1])
            else:
                print(-1)
    else:
        command = arr[0]
        X = arr[1]
        stack.append(X)


