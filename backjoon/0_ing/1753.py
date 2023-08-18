# 1753번 최단경로
# https://www.acmicpc.net/problem/1753
import sys
from collections import deque
input = sys.stdin.readline


V, E = map(int, input().split())
K = int(input())
relations = [[] for _ in range(V+1)]
distance = [1_000_000_000 for _ in range(V+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    if u == v:
        continue
    relations[u].append([w, v])

q = deque()
# weight가 작은 값부터 계산해야 다익스트라가 정상적으로 작동한다.
relations[K].sort()
# K distance 초기화
distance[K] = 0
for w, v in relations[K]:
    q.append([K, w, v])

# 혹시 무한 회전을 할 경우를 대비해서 제거
relations[K].clear()

while q:
    n1, weight, n2 = q.popleft()
    distance[n2] = min(distance[n2], distance[n1] + weight)

    relations[n2].sort()
    for w, v in relations[n2]:
        q.append([n2, w, v])
    relations[n2].clear()

for idx in range(1, V+1):
    if idx == K:
        print(0)
    else:
        if distance[idx] == 1_000_000_000:
            print("INF")
        else:
            print(distance[idx])

"""
# 무한 회전 테케 
5 6
1
1 2 2
2 3 1
3 1 2
1 4 5
5 1 2
5 3 2

# 노드 1개 간선 1개 자기 자신에게 들어가는 것도 계산에 반영된다면 최소값이 되지 않을 것
1 1
1
1 1 1

# 노드 3개 간선 1개
3 1
1
1 3 1

# 노드 2개 간선 2개 동일한 방향의 노드가 두 개 있을 때?
2 2
1
1 2 3
1 2 4

# 출발 노드에 연결된 것이 없을 떄?
2 2
1
2 1 3
2 1 1

# 웨이트가 작은 순서대로 입력되지 않았을 떄?
5 5
1
1 3 3
1 2 1
2 3 1
1 4 5
3 4 1

"""