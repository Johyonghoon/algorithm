# 1312번 소수
# https://www.acmicpc.net/problem/1312

A, B, N = map(int, input().split())
ls = list(str(A * (10 ** N) // B))
print(ls[-1])
