# 14425번 문자열 집합
# https://www.acmicpc.net/problem/14425

N, M = map(int, input().split())
S = set()
for _ in range(N):
    S.add(input())

cnt = 0
for _ in range(M):
    if input() in S:
        cnt += 1

print(cnt)
