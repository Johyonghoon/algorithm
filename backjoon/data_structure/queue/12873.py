# 17873번 기념품
# https://www.acmicpc.net/problem/12873

from collections import deque

N = int(input())
q = deque(list(range(1, N+1)))

t = 1
while len(q) != 1:
    q.rotate(-t**3+1)
    q.popleft()
    t += 1

print(q.popleft())

"""
1 2 3
t = 1 => 1 삭제
2 3
t = 2 => 8번째
"""