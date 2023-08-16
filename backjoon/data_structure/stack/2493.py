# 2493번 탑
# https://www.acmicpc.net/problem/2493

"""
1. 탑의 레이저 신호는 좌측으로 향한다.
2. 정방향 탐색하며 자신보다 작은 값이 스택에 저장되어 있다면 스택에서 제거하고,
3. 자신보다 큰 값이 스택에 저장되어 있다면 그 idx+1을 결과에 저장하고 자신을 스택에 저장
"""

import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [0 for _ in range(N)]  # 수신하지 않는 탑이 존재하면 0

stack = []
# 0번째 인덱스는 탑에서 도달하는 곳이 없더라도 0번째 인덱스가 도달되는 영역일 수 있으므로 탐색해야 함
for idx in range(N-1, -1, -1):

    # 비어 있다면 넣기
    if not stack:
        stack.append(idx)
    else:
        # 빛이 아직 도달하지 않은 탑의 정보가 stack에 쌓여 있다.
        # 현재 탑에서 가장 가까운 stack[-1] 영역부터 판단하되,
        # 만약 stack[-1] 보다 작은 값이라면, 그 이후의 탑은 Stack[-1]에 가려져
        # 어차피 도달하지 않으므로 탐색하지 않는다.
        # 이 방법으로 시간 복잡도 O(n) 가 가능해진다.
        while stack and arr[stack[-1]] < arr[idx]:
            result[stack.pop()] = idx+1
        stack.append(idx)
    # print(stack)

print(*result)

"""
0 1 2 3 4
6 9 5 7 4

stack = [1 2 ]
         9 5 7

"""

"""
# 시간 초과
1. 탑의 레이저 신호는 좌측으로 향한다.
2. 따라서, 역순으로 탐색하여 자신보다 큰 탑을 만나게 될 때 정보를 저장할 수 있도록 stack 에 저장
3. 이미 저장되어 있는 스택을 탐색하여 현재 탑보다 작은 경우 stack에서 제거하고 현재 탑 위치 정보 저장


import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
result = [0 for _ in range(N)]

stack = []
for idx in range(N-1, 0, -1):
    for j in stack[::-1]:
        if arr[j] < arr[idx]:
            result[stack.pop()] = idx+1   # 인덱스의 위치는 0부터 시작하기 때문에 1 더하기
        else:
            break   # stack은 내림차순으로 이미 정렬되어 있으므로 탐색할 필요 없음
    stack.append(idx)

print(*result)
"""