# 2460번 지능형 기차 2
# https://www.acmicpc.net/problem/2460

maxi = 0
total = 0
for _ in range(10):
    off, on = map(int, input().split())
    total += on - off
    maxi = max(maxi, total)
print(maxi)