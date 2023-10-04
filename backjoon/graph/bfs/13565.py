# 13565번 침투
# https://www.acmicpc.net/problem/13565
"""
# BFS
0 : 전류가 잘 통하는 흰색
1 : 전류가 통하지 않는 검은색
"""
from collections import deque

M, N = map(int, input().split())
graph = []
for _ in range(M):
    graph.append(list(map(int, list(input()))))

q = deque()

for idx in range(N):
    # 전류 전달 정보를 -1로 저장하고 q에 삽입하자
    if graph[0][idx] == 0:
        graph[0][idx] = -1
        q.append([0, idx])

# BFS
delta = [[1, 0], [-1, 0], [0, 1], [0, -1]]
while q:
    ny, nx = q.popleft()
    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < M and 0 <= ex < N:
            if graph[ey][ex] == 0:
                graph[ey][ex] = -1
                q.append([ey, ex])

isTrue = False
for idx in range(N):
    # 전류가 inner side 까지 전달되었는지 확인
    if graph[M-1][idx] == -1:
        isTrue = True
        break

if isTrue:
    print("YES")
else:
    print("NO")


