# 1874번 스택 수열
# https://www.acmicpc.net/problem/1874

import sys
from collections import deque
input = sys.stdin.readline

arr = deque()
my_stack = []
ans = []

n = int(input())
for _ in range(n):
    arr.append(int(input()))

for idx in range(1, n+1):

    # arr 가 비어있다면 my_stack 이 역순으로 빠져나오며 마무리
    if arr:
        # my_stack가 비어있지 않다면
        if my_stack:
            # arr[0]가 my_stack[-1]보다 크다면 my_stack에 arr[0]이 없음
            if arr[0] > my_stack[-1]:
                my_stack.append(idx)
                ans.append('+')
            elif arr[0] < my_stack[-1]:
                break

        else:
            my_stack.append(idx)
            ans.append('+')

    while my_stack[-1] == arr[0]:
        my_stack.pop()
        arr.popleft()
        ans.append('-')

        if len(my_stack) == 0:
            break

if len(arr) != 0:
    print('NO')
else:
    [print(i) for i in ans]

"""
# 시간초과

for idx in range(1, n+1):

    # arr[0]의 값이 my_stack 에 없다면 append
    if arr[0] not in my_stack:
        my_stack.append(idx)
        ans.append('+')

    else:
        if my_stack[-1] != arr[0]:
            break

    # 만약 my_stack 마지막 인덱스의 값이 빼야하는 값이라면 빼주기
    while my_stack[-1] == arr[0]:
        my_stack.pop()
        arr.popleft()
        ans.append('-')
        if len(my_stack) == 0:
            break
"""