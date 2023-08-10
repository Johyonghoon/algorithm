import sys
input = sys.stdin.readline

stack = []
result = []
isPossible = True
n = int(input())
idx = 1
for _ in range(n):
    num = int(input())
    while True:
        if stack:
            if stack[-1] < num:
                while idx != num:
                    stack.append(idx)
                    result.append("+")
                    idx += 1
            if stack[-1] == num:
                print(stack.pop())
                result.append("-")

                continue
            elif stack[-1] > num:
                isPossible = False
                break

        else:
            stack.append(idx)
            result.append("+")
            idx += 1

if isPossible:
    [print(i) for i in result]
else:
    print(-1)
