# 2875번 대회 or 인턴
# https://www.acmicpc.net/problem/2875

N, M, K = map(int, input().split())
cnt = 0

for k in range(K+1):
    n = N - k
    m = M - K + k
    if n // 2 > m:
        cnt = max(cnt, m)
    else:
        cnt = max(cnt, n//2)

print(cnt)
