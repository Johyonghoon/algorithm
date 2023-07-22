# 2980번 도로와 신호등
# https://www.acmicpc.net/problem/2980

N, L = map(int, input().split())
d = 0
t = 0
for _ in range(N):
    D, R, G = map(int, input().split())
    t += D - d
    d = D
    cycle = t % (R + G)
    if cycle <= R:
        t += R - cycle
print(t + L - d)
