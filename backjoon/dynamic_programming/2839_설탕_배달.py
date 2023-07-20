# 2839번 설탕 배달
# https://www.acmicpc.net/problem/2839

n = int(input())
d = [0] + [5001 for i in range(n)]

for i in range(3, n+1):
    if d[i-3] < 5001:
        d[i] = d[i-3] + 1
    if i >= 5:
        if d[i-5] < 5001:
            d[i] = min(d[i], d[i-5] + 1)

if d[n] == 5001:
    print(-1)
else:
    print(d[n])
