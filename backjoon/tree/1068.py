# 1068번 트리
# https://www.acmicpc.net/problem/1068
import sys

sys.setrecursionlimit(10**9)


def recur(node, prv):
    global cnt

    # R == D 인 경우
    if node == D:
        return

    # 루트 노드의 자식 노드가 1개였는데 삭제했을 경우 본인이 리프 노드가 됨
    if len(tree[node]) == 0:
        if node == R:
            cnt += 1
            return

    # 부모를 포함하여 1개의 간선을 가지는 경우 리프 노드
    if len(tree[node]) == 1:
        if node != R:
            cnt += 1
            return

    for nxt in tree[node]:
        if nxt == prv:
            continue
        recur(nxt, node)


N = int(input())
tree = [[] for _ in range(N)]
arr = list(map(int, input().split()))
R = 0

for child, prnt in enumerate(arr):
    if prnt == -1:
        R = child
        continue
    tree[child].append(prnt)
    tree[prnt].append(child)

D = int(input())

# 삭제해주는 노드와의 관계를 모두 트리에서 제거
for relationship in tree[D]:
    tree[relationship].remove(D)

tree[D].clear()

cnt = 0
# 0번째 인덱스부터 있으므로 영향을 받지 않는 -1 을 prv 로 시작
recur(R, -1)

print(cnt)
