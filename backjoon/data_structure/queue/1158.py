# 1158번 요세푸스 문제
# https://www.acmicpc.net/problem/1158
from collections import deque


N, K = map(int, input().split())
q = deque()
for i in range(1, N+1):
    q.append(i)
result = []
while len(q) != 1:
    cnt = 0
    while True:
        cnt += 1
        temp = q.popleft()
        if cnt == K:
            result.append(temp)
            break
        q.append(temp)

result.append(q.popleft())

print(str(result).replace("[", "<").replace("]", ">"))


