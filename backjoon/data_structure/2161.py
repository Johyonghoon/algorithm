# 2161번 카드1
# https://www.acmicpc.net/problem/2161
from collections import deque

N = int(input())
d = deque()
result = []
for i in range(1, N+1):
    d.append(i)

while len(result) != N:
    result.append(d.popleft())
    if len(d) == 0:
        break
    d.append(d[0])
    d.popleft()

print(*result)

