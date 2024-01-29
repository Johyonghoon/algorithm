# 11060번 점프 점프
# https://www.acmicpc.net/problem/11060

"""
# DFS(백트래킹), BFS 시간초과
# 그럼 DP?
1*N 미로에 1*1 크기의 칸으로 이루어져 있고, 각 칸에는 정수가 하나 쓰여 있다.
i번째 칸에 쓰여있는 수를 A라고 할 때, 재환이는 A 이하만큼 오른쪽으로 떨어진 칸으로 한 번에 점프
ex. 3번째 칸에 쓰여 있는 수가 3이면, 재환이는 4, 5, 6번 칸 중 하나로 점프 가능
"""
import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline


def dfs(idx, cnt):
    global result
    if cnt >= result:
        return

    if idx > N-1:
        return

    if idx == N-1:
        result = min(result, cnt)

    for j in range(jump[idx], 0, -1):
        dfs(idx+j, cnt+1)


def bfs():
    q = deque()
    q.append((0, 0))  # idx, cnt
    while q:
        idx, cnt = q.popleft()
        if idx == N-1:
            print(cnt)
            break

        for j in range(jump[idx], 0, -1):
            if idx + j < N:
                q.append((idx+j, cnt+1))


N = int(input())
jump = list(map(int, input().split()))

# result = int(1e9)
# dfs(0, 0)
# bfs()
# print(result)

dp = [int(1e9) for _ in range(N)]
dp[0] = 0
for idx in range(N-1):
    for j in range(1, jump[idx]+1):
        if idx + j < N:
            dp[idx+j] = min(dp[idx+j], dp[idx] + 1)

if dp[N-1] != int(1e9):
    print(dp[N-1])
else:
    print(-1)
