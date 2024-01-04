# 2670번 연속부분최대곱
# https://www.acmicpc.net/problem/2670

"""
누적곱을 dp로 저장하여 가장 큰 수를 찾고,
가장 큰 수보다 앞의 인덱스에 해당하는 dp 값 중 0이 아닌 가장 작은 수를 나눈다.
누적곱을 구할 때 0이 있다면 필터링 해야 할 듯
"""

import sys
input = sys.stdin.readline

N = int(input())
numbers = [float(input()) for _ in range(N)]
dp = [0 for _ in range(N)]
dp[0] = numbers[0]
for i in range(1, N):
    dp[i] = max(numbers[i], dp[i-1] * numbers[i])

print(f"{max(dp):.3f}")
