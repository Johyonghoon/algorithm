# 10655번 마라톤 1
# https://www.acmicpc.net/problem/10655

import sys
input = sys.stdin.readline

N = int(input())
coordinate = []
for _ in range(N):
    x, y = map(int, input().split())
    coordinate.append((y, x))

# 다음 좌표와의 차이
dp1 = []
for idx in range(1, N):
    y2, x2 = coordinate[idx]
    y1, x1 = coordinate[idx-1]
    dp1.append(abs(y2-y1) + abs(x2-x1))

# 다다음 좌표와의 차이
dp2 = [0]
for idx in range(2, N):
    y2, x2 = coordinate[idx]
    y1, x1 = coordinate[idx-2]
    dp2.append(abs(y2-y1) + abs(x2-x1))

# print(dp1)
# print(dp2)
mini = int(1e9)
for idx in range(1, N-1):
    mini = min(mini, dp2[idx] - (dp1[idx] + dp1[idx-1]))

print(sum(dp1) + mini)

