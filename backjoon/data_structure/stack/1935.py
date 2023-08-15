# 1935번 후위 표기식 2
# https://www.acmicpc.net/problem/1935

import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().strip())

d = {}
for alphabet in range(N):
    d[chr(ord("A") + alphabet)] = int(input())     # 해당 알파벳에 대한 숫자 정보 저장

# 알파벳에 대한 숫자를 입력하며 후위 표기식 계산
calc = []
for op in arr:
    if op in ["+", "-", "*", "/"]:
        num2 = calc.pop()
        num1 = calc.pop()
        if op == "+":
            num = num1 + num2
            calc.append(num)
        if op == "-":
            num = num1 - num2
            calc.append(num)
        if op == "*":
            num = num1 * num2
            calc.append(num)
        if op == "/":
            num = num1 / num2
            calc.append(num)
    else:
        calc.append(d[op])

print(f"{calc[0]:.2f}")


