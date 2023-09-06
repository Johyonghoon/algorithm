# 10164번 격자상의 경로
# https://www.acmicpc.net/problem/10164
import numpy as np

"""
dp로 풀면 되지 않을까,,,
"""
from collections import deque


# y, x는 출발지, zy, zx는 목적지에 대한 좌표
def bfs(y, x, zy, zx):
    q = deque()
    q.append([y, x])

    while q:
        ny, nx = q.popleft()
        for dy, dx in delta:
            ey = ny + dy
            ex = nx + dx
            if 0 <= ey <= zy and 0 <= ex <= zx:
                # 방문처리를 안하면 계속 같은 지점에 대해 탐색하게 됨
                if dp[ey][ex]:
                    continue
                up = 0
                left = 0
                # ey != 0일 때
                if 1 <= ey:
                    up = dp[ey-1][ex]
                # ex != 0일 때
                if 1 <= ex:
                    left = dp[ey][ex-1]
                # 현재 경로로 올 수 있는 모든 경로 입력
                dp[ey][ex] = up + left
                # print(np.array(dp))
                q.append([ey, ex])


N, M, K = map(int, input().split())

delta = [[1, 0], [0, 1]]
dp = [[0 for _ in range(M)] for _ in range(N)]
dp[0][0] = 1
# K 값이 있다면 중간 좌표를 확인하여 (0, 0) to (dsty, dstx) * (dsty, dstx) to (N, M)
if K:
    K -= 1  # 애초에 전체 번호를 1만큼 빼주고 판단하자(인덱스 탐색을 위해)
    dsty = K // M
    dstx = K % M

    bfs(0, 0, dsty, dstx)
    bfs(dsty, dstx, N-1, M-1)

else:
    bfs(0, 0, N-1, M-1)

print(dp[N-1][M-1])


"""
# Recursion : 시간 초과
import sys
sys.setrecursionlimit(10**8)


def recur(ny, nx, arr):
    global result
    if ny == N-1 and nx == M-1:
        if not K or K in arr:
            result += 1
        return

    for dy, dx in delta:
        ey = ny + dy
        ex = nx + dx
        if 0 <= ey < N and 0 <= ex < M:
            arr.append(graph[ey][ex])
            recur(ey, ex, arr)
            arr.pop()


delta = [[1, 0], [0, 1]]
N, M, K = map(int, input().split())

graph = []
for idx in range(N):
    graph.append(list(range(idx*M, (idx+1) * M)))

# K 값이 있다면
if K:
    K -= 1  # 애초에 전체 번호를 1만큼 빼주고 판단하자(인덱스 탐색을 위해)
    dsty = K // M
    dstx = K % M
    print(dsty, dstx)

result = 0
recur(0, 0, [])
print(result)
"""