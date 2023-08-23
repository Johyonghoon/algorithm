# 4803번 트리
# https://www.acmicpc.net/problem/4803

"""
0. 여러 개의 테스트 케이스
1. 트리는 사이클이 없는 연결 요소이므로, 연결되지 않은 1개의 노드 또한 트리로 취급된다.
2. 트리의 사이클을 어떻게 판단할까? 재귀를 할 때 이전 노드가 아니었는데도 연결되어 있다면 사이클?
"""


import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


# 연결된 모든 노드를 방문
def recur(node, prv):
    global isCycle
    visited[node] = 1

    for nxt in edges[node]:
        # 다음 노드가 부모 노드가 아님에도 방문한 노드라면 cycle
        if visited[nxt]:
            # 이미 방문했는데 그게 부모가 아니다? cycle
            if nxt != prv:
                isCycle = True
            continue
        recur(nxt, node)


for tc in range(1, 10**9):
    # n: 정점의 개수 / m: 간선의 개수
    n, m = map(int, input().split())

    # 문제조건) 0, 0이 들어올 경우 종료
    if n == 0 and m == 0:
        break

    edges = [[] for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]
    for _ in range(m):
        n1, n2 = map(int, input().split())
        edges[n1].append(n2)
        edges[n2].append(n1)

    tree = 0
    for idx in range(1, n+1):
        if visited[idx]:
            continue

        isCycle = False
        recur(idx, 0)
        if not isCycle:
            tree += 1

    print(f"Case {tc}:", end=" ")
    if tree:
        if tree == 1:
            print("There is one tree.")
        else:
            print(f"A forest of {tree} trees.")
    else:
        print("No trees.")
