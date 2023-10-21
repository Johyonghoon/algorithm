# 1240번 노드사이의 거리
# https://www.acmicpc.net/problem/1240


def dfs(node, prnt, dist):
    global is_done
    if node == target:
        print(dist)
        is_done = True
        return

    for nxt, d in edges[node]:
        if is_done:
            return
        if nxt == prnt:
            continue
        dfs(nxt, node, dist+d)


N, M = map(int, input().split())
edges = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2, d = map(int, input().split())
    edges[n1].append([n2, d])
    edges[n2].append([n1, d])

for _ in range(M):
    root, target = map(int, input().split())
    is_done = False
    dfs(root, 0, 0)

"""
4 3
2 1 2
4 3 2
1 4 3
1 2
3 2
1 4
"""


