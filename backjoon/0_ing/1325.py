# 1325번 효율적인 해킹
# https://www.acmicpc.net/problem/1325

"""
한 번에 해킹으로 여러 개의 컴퓨터를 해킹하려고 한다.
즉, 연결된 그래프의 노드 개수가 가장 많은 그래프를 구하는 문제
A가 B가 신뢰하는 경우에는 B를 해킹하면 A도 해킹
A가 B를 신뢰한다는 정보가 들어옴 (단방향)
단방향이지만, 신뢰를 받는 상대의 컴퓨터를 해킹해야 신뢰하는 사람의 컴퓨터를 해킹할 수 있음
따라서, 입력되는 정보를 반대로 저장해야 함

서로 바라본다면, 어떻게 정보의 개수를 전달할까,,,
연결 정보에 부모가 포함되어 있다면 넘기기!
"""

import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def dfs(node, prv):

    for nxt in edges[node]:
        if nxt == prv:
            need_to_update.append([nxt, prv])
            continue
        # 만약 연결된 그래프를 이미 탐색했다면
        # 그 정보를 부모에게 전달
        if len(links[idx]) > 1:
            links[node] = links[node] | links[nxt]
        # 아니라면 탐색 후 부모에게 전달
        else:
            links[node] = links[node] | dfs(nxt, node)

    return links[node]


# 신뢰 정보 입력
N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    # A가 B를 신뢰하면, B가 A 컴퓨터를 해킹할 수 있다.
    edges[B].append(A)

# 각 노드에서 출발하여 탐색할 수 있는 pc의 개수를 구하기
# 단, 이미 탐색했을 때에는 그 정보를 신뢰 받는 상대에게 전달
links = [{i} for i in range(N+1)]
need_to_update = []
for idx in range(1, N+1):
    if len(links[idx]) > 1:
        continue
    dfs(idx, -1)

# 부모여서 업데이트 하지 못한 정보를 업데이트
for prnt, child in need_to_update:
    links[prnt] = links[prnt] | links[child]

print(links)

link_cnt = []
for link in links:
    link_cnt.append(len(link))

# print(link_cnt)
# 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력
result = []
maxi = max(link_cnt)
for idx, cnt in enumerate(link_cnt):
    if cnt == maxi:
        result.append(idx)

result.sort()
print(*result)

"""
반례
input
2 2
1 2
2 1

ans
1 2

output
1

input
3 3
1 2
2 3
3 1
"""