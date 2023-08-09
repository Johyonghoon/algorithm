# 1312번 소수
# https://www.acmicpc.net/problem/1312

"""
A : 피제수(분자)
B : 제수(분모)
(1 <= A, B <= 100_000)
N : 구해야 하는 자리수
(1 <= N <= 1_000_000)

1. 1_000_000번째 소수점 자리
"""

A, B, N = map(int, input().split())
ls = list(str(A * (10 ** N) // B))
print(ls[-1])
