# 1874번 스택 수열
# https://www.acmicpc.net/problem/1874

import sys
from collections import deque
input = sys.stdin.readline

arr = deque()
my_stack = []
ans = ""

n = int(input())
for _ in range(n):
    arr.append(int(input()))

for idx in range(1, n+1):

    # arr[0]의 값이 my_stack 에 없다면 append
    if arr[0] not in my_stack:
        my_stack.append(idx)
        ans += '+\n'

    else:
        if my_stack[-1] != arr[0]:
            break

    # 만약 my_stack 마지막 인덱스의 값이 빼야하는 값이라면 빼주기
    while my_stack[-1] == arr[0]:
        my_stack.pop()
        arr.popleft()
        ans += '-\n'
        if len(my_stack) == 0:
            break

if len(arr) != 0:
    print('NO')
else:
    print(ans)
