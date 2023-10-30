# 2229번 조 짜기
# https://www.acmicpc.net/problem/2229

"""
나이 순서대로 정렬되어 있는 조를 기준으로
순서를 뒤엎지 않고 그룹을 나누어서 계산해라는 뜻인듯 하다.
"""

import sys
sys.setrecursionlimit(10**9)


def recur(idx):
    # N-1번째 인덱스까지 그룹화한 후 더이상 그룹화할 것이 없다는 것을 의미
    if idx == N:
        dp[idx] = 0
        return 0

    # N을 벗어나면 불가능
    if idx > N:
        return -int(1e9)

    # 이미 계산했다면 그 값을 리턴
    if dp[idx] != -1:
        return dp[idx]

    # 그룹에 나만 존재하는 경우부터 가능한 모든 경우까지
    for j in range(1, N+1-idx):
        arr = ability[idx:idx+j]
        score = max(arr) - min(arr)
        dp[idx] = max(dp[idx], recur(idx+j) + score)
        # print(idx, j, dp[idx], score)

    return dp[idx]


N = int(input())
ability = list(map(int, input().split()))
# print(ability)

dp = [-1 for _ in range(N+1)]
recur(0)
print(max(dp))
