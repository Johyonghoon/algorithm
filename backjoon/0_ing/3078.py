# 3078번 좋은 친구
# https://www.acmicpc.net/problem/3078

import sys
from collections import deque
input = sys.stdin.readline


N, K = map(int, input().split())
students = []
for idx in range(N):
    students.append([len(input().strip()), idx])
students.sort()

q = deque()
idx = 0
result = 0
while idx < N:
    length = students[idx][0]
    if q and q[0][0] != length:
        result += len(q) - 1
        q = deque()
    q.append(students[idx])

    while q and q[-1][1] - q[0][1] > K:
        q.popleft()
        result += len(q) - 1

    idx += 1

while q:
    q.popleft()
    result += len(q)

print(result)

"""
# 시간 초과
# 성적과 학생 이름 정보 입력
students = []
for idx in range(N):
    students.append([idx, input().strip()])

visited = [0 for _ in range(N)]
# K 깊이만큼만 탐색하며 이름 길이가 같은 경우를 찾기
# 성적순으로 탐색하므로, 자신보다 성적이 좋은 경우는 이미 좋은 친구가 본인을 탐색
# 이렇게 탐색하면 최악의 경우 300_000 ** 2 의 시간복잡도가 발생하지 않을까?
cnt = 0
for g1, n1 in students:
    for i in range(1, K+1):
        if g1+i == N:
            break
        g2, n2 = students[g1+i]
        if len(n1) == len(n2):
            cnt += 1
print(cnt)
"""


"""
# 시간 초과
# [이름 길이, 등수] 정보로 저장
students = [[] for _ in range(21)]
for rank in range(N):
    students[len(input().strip())].append(rank)
# 이름 길이, 등수로 정렬
for idx in range(2, 21):
    students[idx].sort()

cnt = 0
for arr in students[2:]:
    for start in range(len(arr)):
        for end in range(start+1, len(arr)):
            if arr[end] - arr[start] <= K:
                cnt += 1
            else:
                break

print(cnt)
"""

