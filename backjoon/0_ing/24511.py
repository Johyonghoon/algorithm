# 24511번 queuestack
# https://www.acmicpc.net/problem/24511
import sys
input = sys.stdin.readline
from collections import deque

"""
1. stack의 특성상 마지막 인덱스 push- 마지막 인덱스 pop의 과정이 불필요하게 됨
2. queue의 특성상 제일 우측의 값은 먼저, 새로 들어오는 값은 가장 마지막에 나가게 됨
"""

# 1. 자료구조의 개수
N = int(input())

# 2. 각 인덱스의 자료구조 정보 // 1: stack, 0: queue
arr = list(map(int, input().split()))

# 3. 삽입되어 있는 원소
ls = list(map(int, input().split()))

queuestack = deque()

for idx in range(N-1, -1, -1):
    if arr[idx] == 0:
        queuestack.append(ls[idx])

# 4. 삽입할 수열의 길이 M
M = int(input())
# 5. 삽입할 원소를 담고 있는 길이 M의 수열 C
C = list(map(int, input().split()))

for idx in range(M):
    queuestack.append(C[idx])
    print(queuestack.popleft(), end=" ")



"""
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
    queuestack[0].append(C[idx])
    for j in range(N):
        num = 0
        if arr[j]:
            num = queuestack[j].pop()
        else:
            num = queuestack[j].popleft()
        j += 1
        if j != N:
            queuestack[j].append(num)
        else:
            print(num, end=" ")
"""