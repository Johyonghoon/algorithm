# 2295번 세 수의 합
# https://www.acmicpc.net/problem/2295

"""
이게 왜 이분탐색일까...
아직도 잘 모르겠다
"""

import sys

input = sys.stdin.readline

N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
numbers.sort(reverse=True)

seti = set()
for x in range(N):
    for y in range(N):
        seti.add(numbers[x]+numbers[y])

breaky = False
for i in range(N):
    for j in range(N-1, i, -1):
        if (numbers[i] - numbers[j]) in seti:
            print(numbers[i])
            breaky = True
        if breaky:
            break
    if breaky:
        break
