# 10828번 스택
# https://www.acmicpc.net/problem/10828
import sys

n = int(input())
stack = []
while n != 0:
    command = sys.stdin.readline().rstrip()
    if command == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif command == "size":
        print(len(stack))
    elif command == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif command == "top":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    else:
        stack.append(command.split()[-1])
    n -= 1
