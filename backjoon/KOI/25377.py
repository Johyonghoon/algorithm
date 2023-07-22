# 25377번 빵
# https://www.acmicpc.net/problem/25377

N = int(input())
time = 1001
for _ in range(N):
    distance, bread = map(int, input().split())
    if distance > bread:
        continue
    time = min(time, bread)

if time == 1001:
    print(-1)
else:
    print(time)
