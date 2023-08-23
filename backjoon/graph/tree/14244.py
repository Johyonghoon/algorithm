# 14244번 트리 만들기
# https://www.acmicpc.net/problem/14244

"""
1. 리프 노드는 차수가 1인 노드
2. 0번 노드는 반드시 리프 노드인 상태로 시작하면 m-1개만 고려하면 되므로 편하지 않을까
3. 이에 따라, 0-1-2 노드의 연결을 만들어 둔 후 시작한다.
4. 이때, 리프 노드는 2개인 상태로 시작하고,
5. 2개를 초과하는 리프 노드가 필요할 경우, 이미 리프 노드가 아닌 추가 노드에 연결
6. 리프 노드의 개수가 이미 충족할 경우, 리프 노드에 추가 노드를 연결
"""


n, m = map(int, input().split())
edges = [[] for _ in range(n)]

# n=3 인 트리를 기준으로 시작
edges[0].append(1)
edges[1].append(0)
edges[1].append(2)
edges[2].append(1)

leaf = 2  # 현재 리프 노드의 개수
idx = 2

while idx != n-1:
    # 이미 리프 노드의 개수를 충족할 때, 리프 노드에 연결
    if leaf == m:
        edges[idx].append(idx+1)
        edges[idx+1].append(idx)
    # 추가로 리프 노드가 필요할 때, 리프 노드가 아닌 노드에 연결
    elif leaf < m:
        j = idx
        while len(edges[j]) == 1:
            j -= 1
        edges[j].append(idx+1)
        edges[idx+1].append(j)
        leaf += 1
    idx += 1

# 순서대로 출력하므로, 연결된 간선 중 자신보다 작은 수의 노드는 이미 출력되었을 것
for idx, edge in enumerate(edges):
    for j in edge:
        if idx < j:
            print(idx, j)

