# 1965번 상자넣기
# https://www.acmicpc.net/problem/1965

"""
# DP
순차적으로 탐색하여 나보다 작은 상자 중에 가장 많은 상자를 담은 상자를 추가
"""

N = int(input())
size = list(map(int, input().split()))
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if size[i] > size[j]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
