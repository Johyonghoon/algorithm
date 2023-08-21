# 13335번 트럭
# https://www.acmicpc.net/problem/13335

from collections import deque

# n : 트럭의 수 // w : 다리의 길이 // L : 다리의 최대 하중
n, w, L = map(int, input().split())
weight = deque(list(map(int, input().split())))

t = 0
total = 0
done = []
q = deque([0 for _ in range(w)])

while len(done) < n:    # 모든 트럭이 지나갈 때까지 반복
    t += 1
    # 원형 큐처럼 동작
    q.rotate(-1)
    # 다리를 건너 나오게 되는 트럭이 발생할 때
    if q[-1]:
        total -= q[-1]
        done.append(q[-1])
        q[-1] = 0
    # 다리 위의 트럭과 다음 트럭의 무게의 합이 다리 최대 하중을 넘지 않을 때 들어갈 수 있다.
    if weight:
        if total + weight[0] <= L:
            total += weight[0]
            q[-1] = weight.popleft()

    # print("weight", weight)
    # print("cQ", q)

print(t)
