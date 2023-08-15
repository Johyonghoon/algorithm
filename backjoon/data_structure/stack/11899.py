# 11899번 괄호 끼워넣기
# https://www.acmicpc.net/problem/11899

S = list(input())
stack = []
for brackets in S:
    if brackets == "(":
        stack.append(brackets)
    else:
        if stack:
            if stack[-1] == "(":
                stack.pop()
                continue
        stack.append(brackets)

print(len(stack))
