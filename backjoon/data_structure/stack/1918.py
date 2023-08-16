# 1918번 후위 표기식
# https://www.acmicpc.net/problem/1918

# isp = {"(": 3, "*": 2, "/": 2, "+": 1, "-": 1}
icp = {"(": 0, "*": 2, "/": 2, "+": 1, "-": 1}
arr = list(input())

postfix = []
stack = []
for op in arr:
    # 피연산자는 바로 후위 표기식에 추가
    if op.isalpha():
        postfix.append(op)
    # 연산자는 우선순위에 따라 결정
    else:
        if not stack:
            stack.append(op)
        elif op == "(":
            stack.append(op)
        elif op == ")":
            while stack and stack[-1] != "(":
                postfix.append(stack.pop())
            stack.pop()
        else:
            while stack and icp[op] <= icp[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(op)

postfix += reversed(stack)
print("".join(postfix))
