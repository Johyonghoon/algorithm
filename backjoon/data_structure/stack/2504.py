# 2504번 괄호의 값
# https://www.acmicpc.net/problem/2504

S = list(input())
brackets = []
isTrue = True

idx = 0
while idx < len(S):
    bracket = S[idx]
    # print(brackets)

    if len(brackets) >= 2:
        if isinstance(brackets[-1], int) and isinstance(brackets[-2], int):
            num2 = brackets.pop()
            num1 = brackets.pop()
            if brackets:
                if brackets[-1] == "{":
                    brackets.append(num1 * num2)
                    continue
            brackets.append(num1 + num2)
            continue

    if bracket.isdigit():
        brackets.append(int(bracket))
    elif bracket == "(" or bracket == "[":
        brackets.append(bracket)
    elif bracket == ")":
        if brackets:
            if brackets[-1] == "(":
                brackets.pop()
                brackets.append(2)
            elif len(brackets) > 1 and isinstance(brackets[-1], int) and brackets[-2] == "(":
                num = brackets.pop() * 2
                brackets.pop()  # 열린 괄호 제거
                brackets.append(num)
            else:
                isTrue = False
        else:
            isTrue = False

    elif bracket == "]":
        if brackets:
            if brackets[-1] == "[":
                brackets.pop()
                brackets.append(3)
            elif len(brackets) > 1 and isinstance(brackets[-1], int) and brackets[-2] == "[":
                num = brackets.pop() * 3
                brackets.pop()  # 열린 괄호 제거
                brackets.append(num)
            else:
                isTrue = False
        else:
            isTrue = False
    idx += 1

for op in brackets:
    if op in ["(", ")", "[", "]"]:
        isTrue = False

if isTrue:
    print(sum(brackets))
else:
    print(0)
