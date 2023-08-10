# 11866번 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866

N, K = map(int, input().split())

# 1 ~ N 까지의 수가 순서대로 담긴 스택 생성
stack = [i for i in range(1, N+1)]
result = []
# stack 길이가 1이 될 때까지
while len(stack) > 1:
    cnt = 1
    # 3칸 이동 후
    while cnt != K:
        cnt += 1
        temp = stack.pop(0)
        stack.append(temp)
    # 스택에서 빼준 후 결과 리스트에 삽입
    result.append(stack.pop(0))

# 마지막 남은 1개의 stack의 수를 결과에 삽입
result.append(stack[0])
print(str(result).replace("[", "<").replace("]", ">"))


"""
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
"""