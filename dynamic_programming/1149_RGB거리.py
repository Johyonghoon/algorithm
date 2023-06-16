# 1149 RGB거리
# https://www.acmicpc.net/problem/1149

# N = int(input())
# arr = []
# for _ in range(N):
#     arr.append(list(map(int, input().split())))
# ans = int(1e9)
#
# def recur(idx, color, cost):
#     global ans
#     if idx == N:
#         ans = min(ans, cost)
#         return
#     recur(idx+1, 0, cost + min(recur(idx))
#     recur(idx+1, 1, cost + min(arr[idx][0], arr[idx][2]))
#     recur(idx+1, 2, cost + min(arr[idx][0], arr[idx][1]))
#
# recur(0, 0, 0)
#
#
# print(ans)














"""
# 1트
n = int(input())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for i in range(1, n):
    arr[i][0] += min(arr[i-1][1], arr[i-1][2])
    arr[i][1] += min(arr[i-1][0], arr[i-1][2])
    arr[i][2] += min(arr[i-1][0], arr[i-1][1])

print(min(arr[n-1]))
"""