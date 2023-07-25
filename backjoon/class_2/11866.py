# 11866번 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

from collections import deque

N, K = map(int, input().split())
d = deque()

for i in range(1, N+1):
    d.append(i)
result = []
cnt = 0

while len(d) != 1:
    cnt += 1
    if cnt == K:
        cnt = 0
        result.append(d.popleft())
        continue
    x = d.popleft()
    d.append(x)
result.append(d[0])

print(str(result).replace("[", "<").replace("]", ">"))
