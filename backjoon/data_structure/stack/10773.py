# 10773번 제로
# https://www.acmicpc.net/problem/10773

import sys
input = sys.stdin.readline

stack = []
K = int(input())
for _ in range(K):
    num = int(input())
    # 숫자 입력
    if num != 0:
        stack.append(num)
    # 최근의 수 삭제
    else:
        stack.pop()

print(sum(stack))
