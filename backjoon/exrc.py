from collections import deque

arr = [1, 2, 3, 4, 5]
q = deque(arr)
q.rotate(-2**3+1)
print(q.popleft())
print(q)