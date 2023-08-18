# 24511번 queuestack
# https://www.acmicpc.net/problem/24511
from collections import deque

# 1. 자료구조의 개수
N = int(input())
# 2. 각 인덱스의 자료구조 정보 // 1: stack, 0: queue
queuestack = []
arr = list(map(int, input().split()))
for ds in arr:
    if ds:
        queuestack.append([])
    else:
        queuestack.append(deque())
# 3. 삽입되어 있는 원소
ls = list(map(int, input().split()))
for idx, num in enumerate(ls):
    queuestack[idx].append(num)
# 4. 삽입할 수열의 길이 M
M = int(input())
# 5. 삽입할 원소를 담고 있는 길이 M의 수열 C
C = list(map(int, input().split()))

for idx in range(M):
    print(queuestack)
    queuestack[0].append(C[idx])
    for j in range(M):
        num = 0
        if arr[j]:
            num = queuestack[j].pop()
        else:
            num = queuestack[j].popleft()
        j += 1
        if j != M:
            queuestack[j].append(num)
        else:
            print(num, end=" ")
